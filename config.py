import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", 7414019)
    API_HASH  = os.environ.get("API_HASH", "d463ed3d695f5cd4164029405ad8388e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8302777365:AAG4tnaqg0Eza96fRI_k__SPXPXvmdfAC4Y")
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Zoro")
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority")
    SESSION = os.environ.get("SESSION", "AQGP6NEAMjnEQNxbYGDn_twdSjnlvf5yHF3eAuNOZZiq2O1Ef_05xA5ZdsOljSnhhMxKYPVHNWhA4xQ4LESNJlaI8hwaat8wiQlsmwxNKvBct75bng4HPBXQhBSSCMk2gZC9Pk-cn4bFv639uda7vQ_ZvqLl2WKyHm6XHPbbp8kqr77p763BvuTL3zpaRUG-UGVu0YBa9S2cdncqDjFX7T4yqmQ4VZfPk6L3qZrweiFlZcpZw3j4GYZ7jm-Zxgail1WfQd5mZJsOtyfp1eE_GA9275XEf1nZQNQCb0liw-F3qIIKnlC1NMssxY_dbi1cxSwKxNCE2-7ZGpv0uXVYDPrsFVhV3gAAAAGloin3AA")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/0624f0e874718a066a3f6.mp4")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7073835511').split()]
    FORCE_SUB_1 = os.environ.get("FORCE_SUB_1", "EdgeBotSupport")
    FORCE_SUB_2 = os.environ.get("FORCE_SUB_2", "EdgeBots")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1002155818429))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002155818429"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """
<b>ʜᴇʏ {}!✨

🫧 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ!
ᴡʜɪᴄʜ ᴄᴀɴ ᴍᴀɴᴜᴀʟʟʏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴀʟsᴏ ᴄᴀɴ sᴇᴛ ᴘʀᴇғɪx ᴀɴᴅ sᴜғғɪx ᴏɴ ʏᴏᴜʀ ғɪʟᴇs.⚡️

✨ ᴛʜɪs ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ <a href=https://github.com/GeekLuffy/>ʟᴜꜰꜰʏ</a>
──────────────────
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴏᴡ ᴛᴏ ᴜsᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</b>
"""

    DONATE_TXT = """<b>
👋 ʜᴇʏ ᴛʜᴇʀᴇ {},

Jᴜsᴛ ᴡᴀɴᴛᴇᴅ ᴛᴏ ᴅʀᴏᴘ ᴀ ǫᴜɪᴄᴋ ᴛʜᴀɴᴋs ʏᴏᴜʀ ᴡᴀʏ! Iɴ ᴏᴜʀ ᴛɪɴʏ ᴄᴏʀɴᴇʀ ᴏғ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ʙᴏᴛs, ʜᴀᴠɪɴɢ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ ғᴇᴇʟs ʟɪᴋᴇ ɢᴇᴛᴛɪɴɢ ᴀ ᴡᴀʀᴍ ʜᴜɢ.

Nᴏ ɴᴇᴇᴅ ᴛᴏ sᴛʀᴇss ᴀʙᴏᴜᴛ ᴅᴏɴᴀᴛɪᴏɴs – ʏᴏᴜʀ ʟɪᴛᴛʟᴇ sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ᴄʟɪᴄᴋs ᴍᴇᴀɴ ᴛʜᴇ ᴡᴏʀʟᴅ ᴛᴏ ᴜs.

Bɪɢ ᴛʜᴀɴᴋs ғᴏʀ ʙᴇɪɴɢ ᴛʜᴇ sᴜᴘᴘᴏʀᴛ sᴜᴘᴇʀsᴛᴀʀ ɪɴ ᴏᴜʀ sᴍᴀʟʟ, ʙᴜᴛ ᴀᴡᴇsᴏᴍᴇ, sᴘᴀᴄᴇ!🌟</b>"""

    HELP_TXT = """<b>ᴇᴅɢᴇ ʀᴇɴᴀᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs🫧
 
ᴇᴅɢᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ɪꜱ ᴀ ᴠᴇʀʏ ʜᴀɴᴅʏ ᴀɴᴅ ʜᴇʟᴘғᴜʟ ʙᴏᴛ  ᴛʜᴀᴛ ʜᴇʟᴘꜱ ʏᴏᴜ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ.

<u>ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇs:</u>
➲ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴʏ ғɪʟᴇs.
➲ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ᴍᴇᴛᴀᴅᴀᴛᴀ.
➲ ᴜᴘʟᴏᴀᴅ ɪɴ ᴅᴇsɪʀᴇ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
➲ ᴄᴀɴ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴘʀᴇғɪx & sᴜғғɪx.
➲ ʀᴇɴᴀᴍᴇ ғɪʟᴇs ᴠᴇʀʏ ǫᴜɪᴄᴋʟʏ.
</b>  
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @GeekLuffy🙏🥲
    ABOUT_TXT = """<b>
» ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href=https://t.me/GeekLuffy>ʟᴜꜰꜰʏ</a>
» ɢɪᴛʜᴜʙ :  <a href=https://github.com/GeekLuffy/>ʟᴜꜰꜰʏ</a>
» ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a>
» ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>ᴘʏᴛʜᴏɴ</a>
» ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href=https://t.me/Monkey_d_luufy>ᴇᴅɢᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ</a>
» ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Anime_Edge>ᴀɴɪᴍᴇ ᴇᴅɢᴇ</a>
» ᴍᴀɪɴ ɢʀᴏᴜᴘ : <a href=https://t.me/straw_hat_piratess>ꜱᴛʀᴀᴡʜᴀᴛ ᴘɪʀᴀᴛᴇꜱ</a></b>"""

    META_TXT = """
**ᴍᴀɴᴀɢɪɴɢ ᴍᴇᴛᴀᴅᴀᴛᴀ ғᴏʀ ʏᴏᴜʀ ᴠɪᴅᴇᴏs ᴀɴᴅ ғɪʟᴇs**

**ᴠᴀʀɪᴏᴜꜱ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

- **ᴛɪᴛʟᴇ**: Descriptive title of the media.
- **ᴀᴜᴛʜᴏʀ**: The creator or owner of the media.
- **ᴀʀᴛɪꜱᴛ**: The artist associated with the media.
- **ᴀᴜᴅɪᴏ**: Title or description of audio content.
- **ꜱᴜʙᴛɪᴛʟᴇ**: Title of subtitle content.
- **ᴠɪᴅᴇᴏ**: Title or description of video content.

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ:**
➜ /metadata: Turn on or off metadata.

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ꜱᴇᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

➜ /settitle: Set a custom title of media.
➜ /setauthor: Set the author.
➜ /setartist: Set the artist.
➜ /setaudio: Set audio title.
➜ /setsubtitle: Set subtitle title.
➜ /setvideo: Set video title.

**ᴇxᴀᴍᴘʟᴇ:** /settitle Your Title Here

**ᴜꜱᴇ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴇɴʀɪᴄʜ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴡɪᴛʜ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ᴍᴇᴛᴀᴅᴀᴛᴀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ!**
"""
