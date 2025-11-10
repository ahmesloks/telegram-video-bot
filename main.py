import os
import logging
import asyncio
import tempfile
from pathlib import Path
from functools import wraps
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import yt_dlp

# ---------- الإعداد ----------
BOT_TOKEN = os.environ.get('8514940220:AAFuUfdDz3jt7L5ph1G8VdXznmoPakOlXVU')  # ضع توكن البوت في متغير بيئة
CHANNEL_USERNAME = os.environ.get('CHANNEL_USERNAME', '@english_quotes_ar')  # القناة المطلوبة للاشتراك

# تذكير: البوت يجب أن يكون عضوًا/مشرفًا في القناة حتى تتمكن من التحقق من الاشتراك

# ---------- إعداد اللوق ----------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------- مساعد: تحقق من الاشتراك ----------
def require_channel_member(func):
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        user = update.effective_user
        chat_id = user.id
        try:
            # نتحقق إن كان المستخدم مشتركًا
            member = await context.bot.get_chat_member(CHANNEL_USERNAME, chat_id)
            if member.status in ('left', 'kicked'):
                # ليس مشتركًا — نطالب بالاشتراك
                keyboard = [
                    [InlineKeyboardButton('فتح القناة', url=f'https://t.me/{CHANNEL_USERNAME.lstrip("@")}')],
                    [InlineKeyboardButton('تحقق الآن ✅', callback_data='check_sub')]
                ]
                await update.message.reply_text(
                    '🔒 للاستخدام، يجب أن تكون مشتركًا في القناة أولاً.',
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )
                return
        except Exception as e:
            logger.exception('خطأ عند التحقق من العضوية')
            # لا نمنع الاستخدام في حال فشل التحقق، لكن نخبر المستخدم
            await update.message.reply_text(
    "⚠️ فشل التحقق من الاشتراك تلقائياً. تأكد أن البوت مشرف في القناة.\n\nخطأ: {}".format(e)
            )
            return
        return await func(update, context, *args, **kwargs)
    return wrapper

# ---------- أوامر بسيطة ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = (
        'أهلاً! أرسل رابط فيديو من YouTube أو TikTok أو Instagram وسأحاول تنزيله وإرساله لك.

'
        'ملاحظة: يجب أن تكون مشتركًا في القناة ليعمل البوت.'
    )
    await update.message.reply_text(txt)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('أرسل رابط الفيديو وسأقوم بالتحميل. يدعم YouTube, TikTok, Instagram عبر yt-dlp.')

# ---------- زر التحقق ----------
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'check_sub':
        user = query.from_user
        try:
            member = await context.bot.get_chat_member(CHANNEL_USERNAME, user.id)
            if member.status not in ('left', 'kicked'):
                await query.edit_message_text('✅ تم التحقق — أنت مشترك! أرسل الرابط الآن.')
            else:
                await query.edit_message_text('❌ لم يتم العثور على اشتراكك. اشترك ثم اضغط تحقق.')
        except Exception as e:
            logger.exception('خطأ عند التحقق داخل callback')
            await query.edit_message_text('⚠️ فشل التحقق — تأكد أن البوت مشرف في القناة.')

# ---------- دالة تحميل الفيديو بواسطة yt-dlp ----------
async def run_yt_dlp(url: str, out_dir: str) -> Path:
    loop = asyncio.get_event_loop()
    # خيارات بسيطة: نطلب أفضل صيغة فيديو+صوت ثم نبني ملف .mp4
    ydl_opts = {
        'outtmpl': os.path.join(out_dir, 'video.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        # تحديد الحد الأقصى للوقت ومعالجة الأخطاء
        'retries': 1,
    }

    def _download():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            # نحاول معرفة اسم الملف الناتج
            filename = ydl.prepare_filename(info)
            # yt-dlp قد يضع امتداد مختلف بعد الدمج
            # حاول إيجاد ملف mp4 أو الملف الفعلي
            base = os.path.splitext(filename)[0]
            for ext in ['mp4','mkv','webm','flv','mp3']:
                candidate = f"{base}.{ext}"
                if os.path.exists(candidate):
                    return candidate
            # fallback: ابحث عن أي ملف يبدأ بالـ base
            for p in Path(out_dir).glob('video.*'):
                return str(p)
            return filename

    filename = await loop.run_in_executor(None, _download)
    return Path(filename)

# ---------- معالجة الرسائل: تنزيل ثم إرسال ----------
@require_channel_member
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    url = text
    await update.message.reply_text('⏳ جارِ التحضير للتحميل — قد يستغرق عدة ثوانٍ إلى دقائق.')

    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            downloaded = await run_yt_dlp(url, tmpdir)
        except Exception as e:
            logger.exception('خطأ أثناء التحميل')
            await update.message.reply_text(f'❌ فشل التحميل: {e}')
            return

        # تحقق من حجم الملف
        max_size_bytes = 49 * 1024 * 1024  # 49 ميجا تقريبا (حد تحمِل البوت)
        size = downloaded.stat().st_size
        if size > max_size_bytes:
            await update.message.reply_text(
                '⚠️ الملف الناتج أكبر من الحد المسموح (≈49MB). سأرسل رابط التحميل المحلي كملف غائب أو يمكنك استخدام خدمة استضافة لرفع الملف.'
            )
            try:
                await update.message.reply_text('ها هو الملف (كمستند) — إن لم يُرسل فأبلغني')
                await update.message.reply_document(document=open(downloaded, 'rb'))
            except Exception:
                # قد يفشل الإرسال بسبب الحجم — نخبر المستخدم بخيار بديل
                await update.message.reply_text('🚫 لا يمكن إرساله عبر البوت بسبب الحجم. استخدم خدمة رفع خارجية (مثل transfer.sh أو Google Drive).')
            return

        # إذا الحجم مناسب نرسل
        try:
            # نرسل كفيديو أولاً
            await update.message.reply_video(video=open(downloaded, 'rb'))
        except Exception as e:
            logger.exception('فشل إرسال الفيديو، سنحاول الإرسال كمستند')
            try:
                await update.message.reply_document(document=open(downloaded, 'rb'))
            except Exception as e2:
                logger.exception('فشل إرسال كمستند')
                await update.message.reply_text(f'❌ لم يتمكن البوت من إرسال الملف: {e2}')

# ---------- نقطة الدخول ----------
async def main():
    if not BOT_TOKEN:
        raise RuntimeError('TELEGRAM_BOT_TOKEN غير مُعرَّف في متغيرات البيئة')

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_cmd))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # تشغيل البوت باستخدام polling (سهل للـ Render)
    await app.initialize()
    await app.start()
    logger.info('البوت يعمل — بدء polling...')
    await app.updater.start_polling()
    # إبقاء العملية حية
    await asyncio.Event().wait()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info('إيقاف البوت')
