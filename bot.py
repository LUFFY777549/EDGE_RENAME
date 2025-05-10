from pyrogram import Client, __version__, idle
from config import Config
from datetime import datetime
from pytz import timezone
from aiohttp import web
from route import web_server
import asyncio

bot = Client(
    name="renamer_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    workers=200,
    plugins={"root": "plugins"},
    sleep_threshold=15,
)

userbot = Client(
    name="renamer_userbot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.SESSION,
    sleep_threshold=15
)

async def start():
    await bot.start()
    me = await bot.get_me()
    bot.mention = me.mention
    bot.username = me.username
    bot.uptime = Config.BOT_UPTIME

    if Config.WEBHOOK:
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", 8080).start()

    print(f"{me.first_name} (Bot) started ⚡️")
    for id in Config.ADMIN:
        try:
            await bot.send_message(id, f"**{me.first_name} (Bot) started ⚡️**")
        except:
            pass

    if Config.LOG_CHANNEL:
        try:
            curr = datetime.now(timezone("Asia/Kolkata"))
            date = curr.strftime('%d %B, %Y')
            time = curr.strftime('%I:%M:%S %p')
            await bot.send_message(
                Config.LOG_CHANNEL,
                f"**__{me.mention} (Bot) restarted!__**\n\n📅 Date: `{date}`\n⏰ Time: `{time}`\n🌐 Timezone: `Asia/Kolkata`\n\n🉐 Version: `v{__version__}`"
            )
        except:
            print("Bot must be admin in log channel.")

    await userbot.start()
    print("Userbot also started...")

    await idle()

    await bot.stop()
    await userbot.stop()

if __name__ == "__main__":
    asyncio.run(start())
