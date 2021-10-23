from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from helpers.decorators import authorized_users_only, errors
from callsmusic.callsmusic import client as USER
from config import SUDO_USERS


@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>قم برفعي واعطني الصلاحيات اولا 😡!!</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "helper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, " ➥ • لقد انضممت الى هنا لتشغيل الموسيقى ، استمتعو بوقتكم ♪  ")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>البوت المساعد موجود بالفعل في المجموعة</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 حدث خطا !! 🛑 \n لم يستطيع البوت الانضمام الى المحادثه بسبب الضغط ، تأكد ان {user.first_name}  مشرف ولديه الصلاحيات ولم يقوم احد بحظره "
            "\n\nOr manually add Asisstant to your Group and try again</b>",
        )
        return
    await message.reply_text(
        "<b>لقد انضم البوت الى المجموعة الخاصة بك </b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>المستخدم لا يستطيع المغادره اوله !! ."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")

# Idon'tknowwhatisthis
