from pyrogram import filters, Client as Mbot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import DUMP_GROUP

subscribed_users = set()


@Mbot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    channel_username = "FilmPrimiere"  
    
    try:
        chat_member = await client.get_chat_member(channel_username, message.from_user.id)
        
        if chat_member.status in ["member", "administrator", "creator"]:
            if message.from_user.id not in subscribed_users:
                subscribed_users.add(message.from_user.id)
                await message.reply("Спасибо")
        else:
            await message.reply(f"Привет 👋👋 {message.from_user.mention()}!\n Я — твой личный бот Telegram. Я умею загружать контент из разных социальных сетей. В данный момент поддерживаю Instagram и TikTok. 📸🎵") 

    except Exception as e:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Подписаться", url=f"https://t.me/{channel_username}")
                ]
            ]
        )
        await message.reply("Подпишитесь на наш канал, чтобы продолжить.", reply_markup=keyboard)
        
@Mbot.on_message(filters.command("help") & filters.incoming)
async def help(Mbot, message):
          await message.reply("Это удобный бот, поэтому вы можете просто отправить сюда свой ролик из Instagram и разместить ссылки :) \n например: `https://www.instagram.com/reel/CZqWDGODoov/?igshid=MzRlODBiNWFlZA==`\n `post: ` `https://www.instagram.com/reel/CuCTtORJbDj/?igshid=MzRlODBiNWFlZA==`")
