<?php
/// BY ; @TSS_C - CH : LSS_E
/// BY ; @TSS_C - CH : LSS_E

$token = '8514940220:AAFuUfdDz3jt7L5ph1G8VdXznmoPakOlXVU'; // التوكن
$bot = bot('getme',['bot'])->result->username;
$mainadmin ="1063041653"; // ايدي الادمن
$adminuser="vvcvv"; // يوزر الادمن بدون @
$kanal = file_get_contents("admin/kanal/kanal.txt");
function bot($method,$datas=[]){
global $token;
    $url = "https://api.telegram.org/bot".$token."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}

function joinchat($id){
global $mid;
$array = array("inline_keyboard");
$get = file_get_contents("admin/kanal/kanal.txt");
$ex = explode("\n",$get);

		if($get==" "){  
			return true;
		$uns = false;
		}else{
if(true){
for($i=0;$i<=count($ex)-2;$i++){
	$s=$i+1;
	$first_line = $ex[$s];
	

$first_ex = explode("-",$first_line);
$name = $first_ex[0];
$url = $first_ex[1];
     $ret = bot("getChatMember",[
         "chat_id"=>"@$url",
         "user_id"=>$id,
         ]);
$stat = $ret->result->status;

         if((($stat=="creator" or $stat=="administrator" or $stat=="member"))){
      $array['inline_keyboard']["$i"][0]['text'] = $name ." ✅";
$array['inline_keyboard']["$i"][0]['url'] = "https://t.me/$url";
         }else{
$array['inline_keyboard']["$i"][0]['text'] = $name ." ❌";
$array['inline_keyboard']["$i"][0]['url'] = "https://t.me/$url";
$uns = true;
}


}
$array['inline_keyboard']["$i"][0]['text'] = "✅ تحقق";
$array['inline_keyboard']["$i"][0]['callback_data'] = "channel_result";
}

$get = file_get_contents("admin/kanal/kanal.txt");
if($uns == true){
     bot('sendMessage',[
         'chat_id'=>$id,
         'text'=>" <b>❗️اشترك في قناتنا أدناه لمواصلة استخدام البوت👇🏼</b>",
'parse_mode'=>html,
'disable_web_page_preview'=>true,
'reply_markup'=>json_encode($array),
]);  
return false;
}else{
return true;
}

if($uns == false){
return true;
}

}
}

/// BY ; @TSS_C - CH : LSS_E
/// BY ; @TSS_C - CH : LSS_E

$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$text = $message->text;
$cid = $message->chat->id;
$id = $update->inline_query->id;
$name = $message->from->first_name;
$mid = $message->message_id;
$type = $message->chat->type;

$cupdate = $update->callback_query;
$data = $cupdate->data;
$ccid = $cupdate->message->chat->id;
$cmid = $cupdate->message->message_id;
$id = $update->inline_query->id;
$qid = $cupdate->id;

$cty = $message->chat->type;
$reklamaturi = file_get_contents("https://builderuzb.myxvest.ru/reklama/rekturi.php");
$reklamatxt = file_get_contents("https://builderuzb.myxvest.ru/reklama/reklama.txt");
$reklamamanzili = file_get_contents("https://builderuzb.myxvest.ru/reklama/reklamamanzil.txt");
mkdir("admin");
mkdir("admin/kanal");
if(file_get_contents("admin/kanal/kanal.txt")){
	}else{
		if(file_put_contents("admin/kanal/kanal.txt"," "));
}
mkdir("step");
if(!file_exists("step/$cid.txt")){  
    file_put_contents("step/$cid.txt","0");
}
$step=file_get_contents("step/$cid.txt");

mkdir("til");
mkdir("til/$cid");
if(file_get_contents("til/$cid/til.txt")){
	}else{
		if(file_put_contents("til/$cid/til.txt","2"));
}
$til = file_get_contents("til/$cid/til.txt");
$til1 = file_get_contents("til/$ccid/til.txt");
$lichka=file_get_contents("yukla.db");
if($type=="private"){
if(strpos($lichka,"$cid") !==false){
}else{
file_put_contents("yukla.db","$lichka\n$cid");
}
}


$name = json_decode(file_get_contents("https://uzgf.ga/allsaver.php?url=".$text),true)["meta"]["source"];


$name = json_decode(file_get_contents("https://uzgf.ga/allsaver.php?url=".$text),true)["meta"]["title"];
$first_ex = explode("-",$name);
$first_ex1 = explode("-",$name1);
$name = $first_ex[0];
$url = $first_ex[1];


if($til=="1"){
	$yuklanyapti ="⏱️ <b>تحميل الفيديوهات</b>";
	$guruhga_qoshish ="➕ أضفني الى مجموعة ➕";
	$start_text ="<b>مرحبا</b>, من خلال هذا البوت يمكنك التحميل من <b>Instagram, TikTok</b>.\n\n<i>ارسل رابط الفيديو الذي تريد تحميله:</i>";
	$error ="😔 لسوء الحظ ، لم أتمكن من تنزيل ملف الوسائط من هذا الرابط:";
	$result ="<b>تم التحميل بواسطة @$bot ✨</b>";
	$til_1 ="🇦🇪 العربية ✅";
	$til_2 ="🇷🇺 Русский";
	$til_3 ="🇬🇧 English";
	}
	if($til=="2"){
	$yuklanyapti ="⏱️ <b>Ведио загружается...</b>";
	$guruhga_qoshish ="➕ ДОБАВИТЬ В ГРУППУ ➕";
	$start_text ="<b>Здравствуйте</b>, с помощью этого бота вы можете скачивать видео из <b>Instagram, TikTok</b>.\n\n<i>Отправьте ссылку на видео, которую нужно скачать:</i>";
	$error ="😔 <b>К сожалению, я не смог загрузить файл медиа по этой ссылке:</b>";
	$result ="<b>Загружено @$bot</b>";
	$til_1 ="🇺🇿 Oʻzbek";
	$til_2 ="🇷🇺 Русский - ✅";
	$til_3 ="🇬🇧 English";
	}
	if($til=="3"){
	$yuklanyapti ="⏱️ <b>Vedio is loading...</b>";
	$guruhga_qoshish ="➕ ADD TO A GROUP ➕";
	$start_text ="<b>Hello</b>, with this bot you can download videos from <b>Instagram, TikTok</b>.\n\n<i>Send the link to the video you want to download:</i>";
	$error ="😔 <b>Unfortunately, I could not download the media file from this link:</b>";
	$result ="<b>Downloaded by @$bot</b>";
	$til_1 ="🇺🇿 Oʻzbek";
	$til_2 ="🇷🇺 Русский";
	$til_3 ="🇬🇧 English - ✅";
	}
	if($text){
		if($cty == "group" or $cty == "supergroup"){
			}else{
if(joinchat($cid)==true){
	}else{
		exit();
		}
		}
		}
		
		if($text=="/lang" or $text=="/lang@Test_TSSbot"){
bot('sendmessage',[
    'chat_id'=>$cid,
    'text'=>"<b>🇦🇪 الرجاء اختيار اللغة
🇷🇺 Пожалуйста, выберите язык:
🇬🇧 Please select a language:</b>",
    'parse_mode'=>'html',
    'reply_to_message_id'=>$mid,
    'reply_markup'=>json_encode([
    'inline_keyboard'=>[
[['text'=>"$til_1",'callback_data'=>"language==1"]],
[['text'=>"$til_2",'callback_data'=>"language==2"]],
[['text'=>"$til_3",'callback_data'=>"language==3"]],
    ]
    ])
    ]);
}
		/// BY ; @TSS_C - CH : LSS_E
/// BY ; @TSS_C - CH : LSS_E
		
		if(mb_stripos($data, "language==")!==false){
	$ex = explode("==",$data);
	$til_id = $ex[1];
	file_put_contents("til/$ccid/til.txt",$til_id);
	bot('deleteMessage',[
    'chat_id'=>$ccid,
    'message_id'=>$cmid,
]);

$til1 = file_get_contents("til/$ccid/til.txt");
if($til1=="1"){
	$yuklanyapti ="⏱️ <b>تحميل الفيديوهات</b>";
	$guruhga_qoshish ="➕ أضفني الى مجموعة ➕";
	$start_text ="<b>مرحبا</b>, من خلال هذا البوت يمكنك التحميل من <b>Instagram, TikTok</b>.\n\n<i>ارسل رابط الفيديو الذي تريد تحميله:</i>";
	$error ="😔 لسوء الحظ ، لم أتمكن من تنزيل ملف الوسائط من هذا الرابط:";
	$result ="<b>تم التحميل بواسطة @$bot ✨</b>";
	$til_1 ="🇦🇪 العربية ✅";
	$til_2 ="🇷🇺 Русский";
	$til_3 ="🇬🇧 English";
	}
	if($til1=="2"){
	$yuklanyapti ="⏱️ <b>Ведио загружается...</b>";
	$guruhga_qoshish ="➕ ДОБАВИТЬ В ГРУППУ ➕";
	$start_text ="<b>Здравствуйте</b>, с помощью этого бота вы можете скачивать видео из <b>Instagram, TikTok</b>.\n\n<i>Отправьте ссылку на видео, которую нужно скачать:</i>";
	$error ="😔 <b>К сожалению, я не смог загрузить файл медиа по этой ссылке:</b>";
	$result ="<b>Загружено @$bot</b>";
	$til_1 ="🇺🇿 Oʻzbek";
	$til_2 ="🇷🇺 Русский - ✅";
	$til_3 ="🇬🇧 English";
	}
	if($til1=="3"){
	$yuklanyapti ="⏱️ <b>Vedio is loading...</b>";
	$guruhga_qoshish ="➕ ADD TO A GROUP ➕";
	$start_text ="<b>Hello</b>, with this bot you can download videos from <b>Instagram, TikTok</b>.\n\n<i>Send the link to the video you want to download:</i>";
	$error ="😔 <b>Unfortunately, I could not download the media file from this link:</b>";
	$result ="<b>Downloaded by @$bot</b>";
	$til_1 ="🇺🇿 Oʻzbek";
	$til_2 ="🇷🇺 Русский";
	$til_3 ="🇬🇧 English - ✅";
	}

bot('sendmessage',[
    'chat_id'=>$ccid,
    'text'=>"$start_text",
    'parse_mode'=>'html',
    'reply_to_message_id'=>$mid,
    'reply_markup'=>json_encode([ 
   'inline_keyboard'=>[  
[['text'=>"$guruhga_qoshish",'url'=>"http://telegram.me/Test_TSSbot?startgroup=new"]] 
]  
])  
    ]);
	
	}
	
		
		
if($data=="channel_result"){
	
    	bot('deleteMessage',[
    'chat_id'=>$ccid,
    'message_id'=>$cmid,
]);
if(joinchat($ccid)==true){
bot('sendmessage',[
    'chat_id'=>$ccid,
    'text'=>"$start_text",
    'parse_mode'=>'html',
    'reply_to_message_id'=>$mid,
    'reply_markup'=>json_encode([ 
   'inline_keyboard'=>[  
[['text'=>"$guruhga_qoshish",'url'=>"http://telegram.me/Test_TSSbot?startgroup=new"]] 
]  
])  
    ]);
    }
}

if($text=="/start" or $text=="/start@Test_TSSbot"){
bot('sendmessage',[
    'chat_id'=>$cid,
    'text'=>"$start_text",
    'parse_mode'=>'html',
    'reply_to_message_id'=>$mid,
    'reply_markup'=>json_encode([ 
   'inline_keyboard'=>[  
[['text'=>"$guruhga_qoshish",'url'=>"http://telegram.me/Test_TSSbot?startgroup=new"]] 
]  
])  
    ]);
}

$json = json_decode(file_get_contents("https://uzgf.ga/allsaver.php?url=".$text),true)["url"][0]["url"];
$name = json_decode(file_get_contents("https://uzgf.ga/allsaver.php?url=".$text),true)["meta"]["title"];
$name1 = json_decode(file_get_contents("https://uzgf.ga/allsaver.php?url=".$text),true)["meta"]["source"];

$first_ex = explode("-",$name);
$first_ex1 = explode("-",$name1);
$name = $first_ex[0];
$url = $first_ex[1];


if(mb_stripos($text,"tiktok.com/")!==false){
	if($json==null){
bot('sendMessage',[
'chat_id'=>$cid , 
 'reply_to_message_id'=>$mid,
'text'=>"$error

$text",
'parse_mode'=>'html',
'disable_web_page_preview'=>true,
]);
}else{
bot('sendMessage',[
'chat_id'=>$cid , 
'text'=>"$yuklanyapti",
'parse_mode'=>'html',
'reply_to_message_id'=>$mid,
]);
$first_ex = explode("-",$name);
$name = $first_ex[0];
$url = $first_ex[1];
bot('deletemessage',[
'chat_id'=>$cid , 
'message_id'=>$mid+1,
]);
bot('sendVideo',[
'chat_id'=>$cid , 
'video'=>$json,
'caption'=>"$result",
 'parse_mode'=>'html',
 'reply_to_message_id'=>$mid,
 'reply_markup'=>json_encode([ 
   'inline_keyboard'=>[  
[['text'=>"$guruhga_qoshish",'url'=>"http://telegram.me/Test_TSSbot?startgroup=new"]] 
]  
])  
]);
}
}

if(mb_stripos($text,"instagram.com/")!==false){
	if($json==null){
bot('sendMessage',[
'chat_id'=>$cid , 
 'reply_to_message_id'=>$mid,
'text'=>"$error

$text",
'parse_mode'=>'html',
'disable_web_page_preview'=>true,
]);
}else{
bot('sendMessage',[
'chat_id'=>$cid , 
'text'=>"$yuklanyapti",
'parse_mode'=>'html',
'reply_to_message_id'=>$mid,
]);
bot('deletemessage',[
'chat_id'=>$cid , 
'message_id'=>$mid+1,
]);
bot('sendVideo',[
'chat_id'=>$cid, 
'video'=>$json,
'caption'=>"$result",
 'parse_mode'=>'html',
 'reply_to_message_id'=>$mid,
 'reply_markup'=>json_encode([ 
   'inline_keyboard'=>[  
[['text'=>"$guruhga_qoshish",'url'=>"http://telegram.me/Test_TSSbot?startgroup=new"]] 
]  
])  
]);
}
}

$kanal=file_get_contents("admin/kanal/kanal.txt");
$admin_menu = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"📢 إعدادات القناة"]],
[['text'=>"📊 الاحصائيات"],['text'=>"الإذاعة"]],
]
]);
$adchanel = json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"📋 قائمة القنوات"]],
[['text'=>"📢 أضف قناة"],['text'=>"📢 حذف قناة"]],
[['text'=>"🗄 الإدارة"]],
]
]);

if($text=="🗄 الإدارة" or $text=="/panel" or $text=="/admin"){
    	if($cid==$mainadmin){
    	unlink("step/$cid.txt");
bot('sendmessage',[
    'chat_id'=>$cid,
    'text'=>"🗄 <b>مرحبًا بك في لوحة الإدارة!</b>",
    'parse_mode'=>'html',
    'reply_markup'=>$admin_menu,
]);
}else{
bot('sendmessage',[
    'chat_id'=>$cid,
    'text'=>"☹️ <b>أنت لست مسؤول</b>",
    'parse_mode'=>'html',
]);
}
}
if($text == "📩 الإذاعة" and $cid == $mainadmin){
 bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"*👥 إعادة توجيه الرسائل للمستخدمين!*",
'parse_mode'=>'markdown',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"🗄 الإدارة"]],
]
])
]);
file_put_contents("step/$cid.txt","forward");
}

if($step == "forward" and $cid == $mainadmin){
if($text == "🗄 الإدارة"){
unlink("step/$cid.txt");
}else{ 
	$lichka = file_get_contents("yukla.db");
$ids=explode("\n",$lichka);
foreach($ids as $id){
$user = bot('forwardMessage', [
'chat_id'=>$id,
'from_chat_id'=>$mainadmin,
'message_id'=>$mid,
]);unlink("step/$cid.txt");
}

if($user){
bot('sendmessage',[
'chat_id'=>$mainadmin,
'text'=>"*✅ الرسالة وصلت!*",
'parse_mode'=>"markdown",
'reply_markup'=>$admin_menu,
]);     
unlink("step/$cid.txt");
}
}
}

if($text == "📢 إعدادات القناة" and $cid==$mainadmin ){
	unlink("step/$cid.txt");
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>📢 أنت في قسم إدارة القناة!
📋 اختر أحد الأقسام أدناه!</b>",
'parse_mode'=>"html",
'reply_markup'=>$adchanel,
]);
}
if($text=="📋 قائمة القنوات" and $cid == $mainadmin){
 if($kanal==" "){
 bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>📋 لا توجد قائمة قنوات متاحة</b>",
'parse_mode'=>'html',
]);
}else{
$soni = substr_count($kanal,"\n");

bot('sendMessage',[
'chat_id'=>$cid,
'text'=>"<b>👇القنوات المربوطة بالبوت:
$kanal

📝إجمالي عدد القنوات: $soni ta</b>",
'parse_mode'=>'html',
 ]);
}
}
if($text == "📢 أضف قناة" and $cid == $mainadmin){
    file_put_contents("step/$cid.txt","new_channel");
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>📡 أرسل رابط قناتك للإضافة!
🔰 على سبيل المثال: اسم القناة مستخدم القناة 
🌍 LSS_E [لمسات برمجية] -LSS_E //اسم القناة والمعرف بدون@

$kanal",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"📢 إعدادات القناة"]],
]
])
]);
}

if($step=="new_channel" and $cid==$mainadmin and $text!=="📢 إعدادات القناة"){
if(mb_stripos($kanal,"$text")){
	
}else{
file_put_contents("admin/kanal/kanal.txt","$kanal\n$text");
unlink("step/$cid.txt");
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>📡 تمت إضافة قناتك بنجاح إلى البوت!
🤖 إدارة البوت على قناتك الآن!</b>",
'parse_mode'=>'html',
'reply_markup'=>$adchanel,
]);
}
}
if($text == "📢 حذف قناة" and $cid == $mainadmin){
file_put_contents("step/$cid.txt","delete");
$ids = explode("\n",$kanal);
$soni = substr_count($kanal,"\n");

bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>📡إرسال رابط القناة لحذف القناة!

🔰 على سبيل المثال:
LSS_E [ لمسات برمجية ] -LSS_E

القنوات المتصلة بالبوت:
$kanal

📝إجمالي عدد القنوات: $soni ta
</b>",
'parse_mode'=>'html',
'reply_markup'=>json_encode([
'resize_keyboard'=>true,
'keyboard'=>[
[['text'=>"📢 إعدادات القناة"]],
]
])
]);
}

if($step == "delete" and $cid==$mainadmin and $text!=="📢 إعدادات القناة"){
if(mb_stripos($kanal,"$text")!==false){
$k = str_replace("\n".$text."","",$kanal);
file_put_contents("admin/kanal/kanal.txt",$k);
unlink("step.txt");
bot('sendmessage',[
'chat_id'=>$cid,
'text'=>"<b>🔰 تم حذف القناة بنجاح!✅</b>",
'parse_mode'=>'html',
'reply_markup'=>$adchanel,
]);
}
}
if($text == "📊 الاحصائيات" or $text == "/stat"){
    	if($cid==$mainadmin){
    $us = file_get_contents("yukla.db");
    $allus = substr_count($us, "\n");
    bot('sendMessage',[
    'chat_id' => $cid,
    'text'=>"📊 <b>إحصائيات البوتات
👤 عدد أعضاء البوت:: $allus ta</b>",
    'parse_mode'=>'html',
    'reply_markup'=>json_encode([
    'inline_keyboard'=>[
[['text'=>"🔁 تحديث",'callback_data'=>"stat_new"]]
    ]
    ])
    ]);
    }else{
bot('sendmessage',[
    'chat_id'=>$cid,
    'text'=>"☹️ <b>يمكن للمسؤول فقط رؤية الإحصائيات</b>",
    'parse_mode'=>'html',
]);
    }
}
if($data == "stat_new"){
    	if($ccid==$mainadmin){
    $us = file_get_contents("yukla.db");
    $allus = substr_count($us, "\n");
    bot('editMessageText',[
'chat_id'=>$ccid,
'message_id'=>$cmid,
    'text'=>"✅ <b>تم تحديث إحصائيات البوت
👤 عدد أعضاء البوت: $allus ta</b>",
    'parse_mode'=>'html',
    'reply_markup'=>json_encode([
    'inline_keyboard'=>[
[['text'=>"🔁 تحديث",'callback_data'=>"stat_new"]]
    ]
    ])
    ]);
    }else{
    	bot("answerCallbackQuery",[
        "callback_query_id"=>$qid,
        "text"=>"☹️ يمكن للمسؤول فقط رؤية الإحصائيات",
        "show_alert"=>true,
        ]);
    }
}

/// BY ; @TSS_C - CH : LSS_E
/// BY ; @TSS_C - CH : LSS_E
