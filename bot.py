from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server
import asyncio

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="renamer_bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.uptime = Config.BOT_UPTIME
        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", 8080).start()
        print(f"{me.first_name} (Bot) ɪꜱ ꜱᴛᴀʀᴛᴇᴅ.....⚡️")
        for id in Config.ADMIN:
            try:
                await self.send_message(id, f"**{me.first_name} (Bot) ɪꜱ ꜱᴛᴀʀᴛᴇᴅ.....⚡️**")
            except:
                pass
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(
                    Config.LOG_CHANNEL,
                    f"**__{me.mention} (Bot) Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`"
                )
            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Bᴏᴛ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")

class UserBot(Client):
    def __init__(self):
        super().__init__(
            name="renamer_userbot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            session_string=Config.SESSION or None,
            workers=100,
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        print(f"{me.first_name} (Userbot) ɪꜱ ꜱᴛᴀʀᴛᴇᴅ.....⚡️")
        for id in Config.ADMIN:
            try:
                await self.send_message(id, f"**{me.first_name} (Userbot) ɪꜱ ꜱᴛᴀʀᴛᴇᴅ.....⚡️**")
            except:
                pass
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(
                    Config.LOG_CHANNEL,
                    f"**__{me.mention} (Userbot) Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`"
                )
            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Uꜱᴇʀʙᴏᴛ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")

async def main():
    bot = Bot()

    if Config.SESSION:  # Only start userbot if session is not empty
        userbot = UserBot()
        await asyncio.gather(bot.start(), userbot.start())
    else:
        await bot.start()

    await asyncio.Event().wait()

# Run the bot and userbot
if __name__ == "__main__":
    asyncio.run(main())