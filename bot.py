import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "19680279"))
API_HASH = environ.get("API_HASH", "a32f974ade51b2dc74e8db4bb049ad01")
BOT_TOKEN = environ.get("BOT_TOKEN", "5696473308:AAGOzVTP8kG8tXC5xCEDkXA-YM4ugHmwcPc")
SESSION = environ.get("SESSION", "AQENGJcAGwbyuqFNUEXViILuLIbCWHXWTIOb-_Ufi_bJh0DneeWK4DloXqrjNjF7YNvLVC3IWMVVDZR5mRPLsY_tqBqQ_aAXBq7joJ8jhjmDicZLkPNOPSUNjUs_wHrC9mYrrZImrhesTPZGAxKmS8B2Jc048e9vTysnlOIhbosYcKK0oCvcXr16B-fEuRuJLQESKZs5qQg19kQZ4bT9rR8rsc3LfOLjr85zPe1jWn48uEgaQLaaeqgiWxmFk46osoxKO4ZxyRSm76X9lBHgXbUEC3uxgTXYI3zsJg7aAeN7tNygk3rNsCbJGw-cRJRbpYYNrTte20-Snj5NYGo20I1lR46qeQAAAAFGYPP_AA")
TIME = int(environ.get("TIME", "300"))
GROUPS = []
for grp in environ.get("-1001607435590").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("1129673243 5394954571").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
