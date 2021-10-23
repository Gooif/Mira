#سالِم
from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>♥️ **اهلا {message.from_user.first_name}** \n
➥  **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) يسمح لك هاذا البوت بتشغيل الصوتيات بالمكالمات الجماعيه الخاصه بالمجموعات !..

الاوامر سهله فقط اتبع التعليمات في خانة [ **الاوامر** في الازرار اسفل الرساله ،

اذا واجهت صعوبه قم بأرسال /help .

**تم تطوير هاذا البوت من قبل الون **
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ اضفني الى مجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                          الاوامر", url="https://t.me/WzUserBoT/10"
                    ),
                    InlineKeyboardButton(
                        "𝗢𝘄𝗻𝗲𝗿 ♪ ", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "قناة مطور البوت", url=f"https://t.me/NvvvM"
                    ),
                    InlineKeyboardButton(
                        " قناة تحديثات البوت", url=f"https://t.me/XkkkU")               
                 ],[
                    InlineKeyboardButton(
                        "𝗔 𝗟 𝗢 𝗡 𝗘", url="https://t.me/C1CIC"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✔ **ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ**\n<b> **الوقت:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناة البوت",url=f"https://t.me/XkkkU"
                    ),
                    InlineKeyboardButton(
                        "قناة المطور",url=f"https://t.me/NvvvM"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>☢ ʜᴇʟʟᴏ {message.from_user.mention()}, ᴘʟᴇᴀsᴇ ᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ sᴇᴇ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ ʏᴏᴜ ᴄᴀɴ ʀᴇᴀᴅ ғᴏʀ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✔ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.mention()}, welcome to help menu ✨
\n📙كيف تستخدمني ؟
\n1. اولا اضفني الى مجموعتك 
2. ارفعني مشرف مع جميع الصلاحيات بدون صلاحية الاخفاء
3. اضف البوت المساعد @{ASSISTANT_NAME} ثم ارسل امر -  /userbotjoin.
3. تأكد ان المكالمه او الدردشه الصوتيه شغاله قبل بدا تشغيل الموسيقى ،
\n💁🏻‍♂️ **اوامر الاعضاء**
\n /play بالرد على الاغنيه او المقطع الصوتي 
/stream (بالرد على ملف صوتي) - تشغيل ملف صوتي
/playlist - عرض قائمة الاغاني في قائمة الانتظار
/song (اسم الاغنيه) - يحمل لك الاغنيه من اليوتيوب
/search (اسم الفيديو) - يبحث لك الفيديو باليوتيوب
/vsong (اسم الفيديو) - يحمل لك الفيديو بصيغة اسرع
\n👷🏻‍♂️ **اوامر المشرفين**
\n/player - لعرض لوحة اعدادات مشغل الموسيقى
/pause - ايقاف الاغنيه 
/resume - استئناف الاغنيه
/skip - لتخطي الاغنيه الحاليه
/end - لايقاف جميع الاغاني
/userbotjoin - دعوة البوت المساعد الى المجموعة
/reload - تحديث الملفات
/cache - ذاكرة التخزين المؤقت
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/musicplayer (on / off) - disable / enable music player in your group
\n🎧 **اوامر التشغيل في القنوات**
\n/cplay - لتشغيل الاغنيه في الدردشة الصوتيه 
/cplayer - لعرض قائمة التشغيل 
/cpause - لتوقف المؤقت للاغنيه
/cresume - لتشغيل الاغنيه 
/cskip - لتخطي الاغنيه الحاليه
/cend - لايقاف الاغاني 
/admincache - تحديث الملفات للاداره
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناة البوت",url=f"https://t.me/XkkkU"
                    ),
                    InlineKeyboardButton(
                        " قناة المطور",url=f"https://t.me/NvvvM"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "المطور ",url=f"t.me/c1cic"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "✈ `سرعة البوت!!`\n"
        f"✅ `{delta_ping * 1000:.3f} ᴍs`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 حالة البوت :\n"
        f"➤ **وقت التشغيل:** `{uptime}`\n"
        f"➤ **بداية التشغيل:** `{START_TIME_ISO}`"
    )
