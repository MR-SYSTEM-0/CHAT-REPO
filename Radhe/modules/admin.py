from pyrogram import filters
from pyrogram.enums import ChatPermissions
from pyrogram.types import Message

from Radhe import Radhe


def get_target_user(message: Message):
    if message.reply_to_message:
        return message.reply_to_message.from_user.id
    elif len(message.command) > 2:
        return message.command[2]
    return None


@Radhe.on_message(filters.group & filters.command("Radhe"))
async def radhe_admin(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("❌ **ωнαт ᴅσ уσυ ωαηт ʈσ ∂σ?**")

    cmd = message.command[1].lower()
    target = get_target_user(message)

    if not target:
        return await message.reply_text(
            "❌ **яєρℓу тσ α υѕєя σя gινє υѕєяι∂/υѕєяηαмє**"
        )

    try:
        if cmd == "mute":
            await message.chat.restrict_member(
                target,
                ChatPermissions()
            )
            await message.reply_text(
                "🔇 **υѕєя мυтє∂ ѕυccєѕѕƒυℓℓγ**"
            )

        elif cmd == "unmute":
            await message.chat.restrict_member(
                target,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True
                )
            )
            await message.reply_text(
                "🔊 **υѕєя υηмυтє∂ ѕυccєѕѕƒυℓℓγ**"
            )

        elif cmd == "ban":
            await message.chat.ban_member(target)
            await message.reply_text(
                "🚫 **υѕєя вαηηє∂ ѕυccєѕѕƒυℓℓγ**"
            )

        elif cmd == "unban":
            await message.chat.unban_member(target)
            await message.reply_text(
                "✅ **υѕєя υηвαηηє∂ ѕυccєѕѕƒυℓℓγ**"
            )

        elif cmd == "kick":
            await message.chat.ban_member(target)
            await message.chat.unban_member(target)
            await message.reply_text(
                "👢 **υѕєя кι¢кє∂ ѕυccєѕѕƒυℓℓγ**"
            )

        elif cmd == "pin":
            if not message.reply_to_message:
                return await message.reply_text(
                    "📌 **яєρℓу тσ α мєѕѕαgє тσ ριη**"
                )
            await message.reply_to_message.pin()
            await message.reply_text("📌 **мєѕѕαgє ριηηє∂**")

        elif cmd == "unpin":
            await message.chat.unpin_all_messages()
            await message.reply_text("📍 **αℓℓ мєѕѕαgєѕ υηριηηє∂**")

        else:
            await message.reply_text("❌ **υηкησωη Rα∂нє ¢σммαη∂**")

    except Exception as e:
        await message.reply_text(f"❌ **єяяσя :** `{e}`")
