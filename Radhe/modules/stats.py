from pyrogram import filters, Client
from pyrogram.types import Message

from Radhe import OWNER, Radhe
from Radhe.database.chats import get_served_chats
from Radhe.database.users import get_served_users


@Radhe.on_cmd("stats")
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())

    await message.reply_photo(
        photo="https://i.ibb.co/WhK0nJc/file-3603.jpg",
        caption=(
            f"ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} :\n\n"
            f"➻ **ᴄʜᴀᴛs :** {chats}\n"
            f"➻ **ᴜsᴇʀs :** {users}"
        ),
    )
