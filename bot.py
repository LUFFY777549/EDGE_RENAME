import asyncio
from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__, idle
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server

# Bot Client
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

        print(f"{me.first_name} (Bot) started ⚡️")
        for id in Config.ADMIN:
            try:
                await self.send_message(id, f"**{me.first_name} (Bot) started ⚡️**")
            except:
                pass

        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(
                    Config.LOG_CHANNEL,
                    f"**__{me.mention} (Bot) restarted!__**\n\n📅 Date: `{date}`\n⏰ Time: `{time}`\n🌐 Timezone: `Asia/Kolkata`\n\n🉐 Version: `v{__version__} (Layer {layer})`"
                )
            except:
                print("Make sure the bot is admin in the log channel")

# Async main to run both clients
async def main():
    bot = Bot()
    userbot = Client(
        name="renamer_userbot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        session_string=Config.SESSION,
        sleep_threshold=15
    )

    await bot.start()
    await userbot.start()

    print("Userbot also started...")
    await idle()

    await bot.stop()
    await userbot.stop()

if __name__ == "__main__":
    asyncio.run(main())
