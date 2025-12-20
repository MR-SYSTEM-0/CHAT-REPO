import aiohttp
from io import BytesIO

from pyrogram.types import Message
from Radhe import Radhe

API_URL = "https://last-warning.serv00.net/md.php?url="


@Radhe.on_cmd("download")
async def download_video(_, message: Message):
    if not message.text or len(message.text.split()) < 2:
        return await message.reply_text(
            "**❌ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟɪɴᴋ**\n\n`Radhe download <link>`"
        )

    link = message.text.split(None, 1)[1]

    wait_msg = await message.reply_text(
        "đøωηℓσαđιηg ყσυя яєqυєѕт βαву… ρℓєαѕє ωαιт 🫶"
    )

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL + link) as resp:
                if resp.status != 200:
                    return await wait_msg.edit("❌ **ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴠɪᴅᴇᴏ**")

                data = await resp.read()

        await wait_msg.delete()

        video = BytesIO(data)
        video.name = "radhe_video.mp4"

        await message.reply_video(
            video=video,
            caption="❤️ **ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴠɪᴅᴇᴏ**",
        )

    except Exception as e:
        try:
            await wait_msg.delete()
        except:
            pass
        await message.reply_text(f"❌ **ᴇʀʀᴏʀ:** `{e}`")
