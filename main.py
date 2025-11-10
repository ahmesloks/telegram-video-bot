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
BOT_TOKEN = os.environ.get('8514940220:AAFuUfdDz3jt7L5ph1G8VdXznmoPakOlXVU')
CHANNEL_USERNAME = os.environ.get('CHANNEL_USERNAME', '@english_quotes_ar')

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
            member = await context.bot.get_chat_member(CHANNEL_USERNAME, chat_id)
            if member.status in ('left', 'kicked'):
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
            await update.message.reply_text(f'⚠️ فشل التحقق من الاشتراك تلقائياً.\nخطأ: {e}')
            return
        return await func(update, context, *args, **kwargs)
    return wrapper

# ---------- أوامر ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'أهلاً! أرسل رابط فيديو من YouTube أو TikTok أو Instagram وسأقوم بتنزيله وإرساله لك.\n'
        '🔒 يجب أن تكون مشتركًا في القناة ليعمل البوت.'
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'أرسل رابط الفيديو وسأقوم بالتحميل. يدعم YouTube, TikTok, Instagram عبر yt-dlp.'
    )

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

# ---------- تحميل الفيديو ----------
async def run_yt_dlp(url: str, out_dir: str) -> Path:
    loop = asyncio.get_event_loop()
    ydl_opts = {
        'outtmpl': os.path.join(out_dir, 'video.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'retries': 1,
    }

    def _download():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            base = os.path.splitext(filename)[0]
            for ext in ['mp4','mkv','webm','flv','mp3']:
                candidate = f"{base}.{ext}"
                if os.path.exists(candidate):
                    return candidate
            for p in Path(out_dir).glob('video.*'):
                return str(p)
            return filename

    filename = await loop.run_in_executor(None, _download)
    return Path(filename)

# ---------- معالجة الرسائل ----------
@require_channel_member
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    await update.message.reply_text('⏳ جارِ التحضير للتحميل — قد يستغرق عدة ثوانٍ إلى دقائق.')

    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            downloaded = await run_yt_dlp(url, tmpdir)
        except Exception as e:
            logger.exception('خطأ أثناء التحميل')
            await update.message.reply_text(f'❌ فشل التحميل: {e}')
            return

        max_size_bytes = 49 * 1024 * 1024
        size = downloaded.stat().st_size

        try:
            if size <= max_size_bytes:
                with open(downloaded, 'rb') as f:
                    await update.message.reply_video(video=f)
            else:
                await update.message.reply_text('⚠️ الملف كبير جدًا لإرساله مباشرة (أكثر من 49MB).')
                with open(downloaded, 'rb') as f:
                    await update.message.reply_document(document=f)
        except Exception as e:
            logger.exception('فشل الإرسال')
            await update.message.reply_text(f'❌ لم يتمكن البوت من إرسال الملف: {e}')

# ---------- نقطة الدخول ----------
async def main():
    if not BOT_TOKEN:
        raise RuntimeError('TELEGRAM_BOT_TOKEN غير مُعرَّف في متغيرات البيئة')

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_cmd))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await app.run_polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info('إيقاف البوت')
