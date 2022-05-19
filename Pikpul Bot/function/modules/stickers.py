"""Make / Download Telegram Sticker Packs without installing Third Party applications
Available Commands:
.kang [Optional Emoji]
.packinfo
.getsticker"""
import asyncio
import datetime
import math
import os
import zipfile
from collections import defaultdict
from io import BytesIO

from PIL import Image
from telethon.errors import MessageNotModifiedError
from telethon.errors.rpcerrorlist import StickersetInvalidError
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import (
    DocumentAttributeSticker,
    InputStickerSetID,
    InputStickerSetShortName,
    MessageMediaPhoto,
)

from pikpulbot import ALIVE_NAME, CMD_HELP
from pikpulbot.utils import edit_or_reply, pikpul_on_cmd, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Who is this"
FILLED_UP_DADDY = "Invalid pack selected."


@pikpul.on(pikpul_on_cmd(pattern="kang ?(.*)"))
@pikpul.on(sudo_cmd(pattern="kang ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("PLease, Reply To A Sticker / Image To Add It Your Pack")
        return
    if not event.is_reply:
        await moods.edit("Reply to a photo to add to my personal sticker pack.")
        return
    reply_message = await event.get_reply_message()
    sticker_emoji = "😎"
    input_str = event.pattern_match.group(1)
    if input_str:
        sticker_emoji = input_str
    moods = await edit_or_reply(
        event, "`Hello, This Sticker Looks Noice. Mind if I steal it`"
    )
    user = await bot.get_me()
    if not user.username:
        user.username = user.id
    pack = 1
    userid = event.sender_id
    # packname = f"PIKPUL PACK"
    # packshortname = f"PIKPUL_{userid}_ns"  # format: Uni_Borg_userid
    if userid == 5033872287:
        packname = f"@Nikhil_LoGo_MaKerPacks 🎭"
        packshortname = "Nikhil_LoGo_MaKerPack"
    else:
        packname = P"@{user.username} KangPack {pack}"
        packshortname = f"PIKPUL_{userid}_Pack"
    await moods.edit("`This Sticker is Gonna Get Stolen.....`")

    is_a_s = is_it_animated_sticker(reply_message)
    file_ext_ns_ion = "@PikpulOT.png"
    file = await borg.download_file(reply_message.media)
    uploaded_sticker = None
    if is_a_s:
        file_ext_ns_ion = "AnimatedSticker.tgs"
        uploaded_sticker = await borg.upload_file(file, file_name=file_ext_ns_ion)
        if userid == 5033872287:
            packname = f"Nikhil_LoGo_MaKer Ka Pack"
            packshortname = "Nikhil_LoGo_MaKer"
        else:
            packname = f"@{user.username} KangPack {pack}"
            packshortname = f"PIKPUL_{userid}"  # format: Uni_Borg_userid
    elif not is_message_image(reply_message):
        await moods.edit("Invalid message type")
        return
    else:
        with BytesIO(file) as mem_file, BytesIO() as sticker:
            resize_image(mem_file, sticker)
            sticker.seek(0)
            uploaded_sticker = await borg.upload_file(
                sticker, file_name=file_ext_ns_ion
            )

    await moods.edit("`Inviting This Sticker To Your Pack 🚶`")

    async with borg.conversation("@Stickers") as bot_conv:
        now = datetime.datetime.now()
        dt = now + datetime.timedelta(minutes=1)
        if not await stickerset_exists(bot_conv, packshortname):
            await moods.edit("`Creating a new pack!`")
            await silently_send_message(bot_conv, "/cancel")
            if is_a_s:
                response = await silently_send_message(bot_conv, "/newanimated")
            else:
                response = await silently_send_message(bot_conv, "/newpack")
            if "Yay!" not in response.text:
                await moods.edit(f"**Error**! @Stickers replied: {response.text}")
                return
            response = await silently_send_message(bot_conv, packname)
            if not response.text.startswith("Alright!"):
                await moods.edit(f"**Error**! @Stickers replied: {response.text}")
                return
            w = await bot_conv.send_file(
                file=uploaded_sticker, allow_cache=False, force_document=True
            )
            response = await bot_conv.get_response()
            if "Sorry" in response.text:
                await moods.edit(f"**Error**! @Stickers replied: {response.text}")
                return
            await silently_send_message(bot_conv, sticker_emoji)
            await silently_send_message(bot_conv, "/publish")
            response = await silently_send_message(bot_conv, f"<{packname}>")
            await silently_send_message(bot_conv, "/skip")
            response = await silently_send_message(bot_conv, packshortname)
            if response.text == "Sorry, this short name is already taken.":
                await moods.edit(f"**Error**! @Stickers replied: {response.text}")
                return
