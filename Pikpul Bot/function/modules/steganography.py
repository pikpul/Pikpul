import os

from cryptosteganography import CryptoSteganography
from telethon.tl.types import MessageMediaPhoto

from pikpulbot import CMD_HELP
from pikpulbot.utils import pikpul_on_cmd, sudo_cmd

sedpath = "./pikpuldevs/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@pikpul.on(pikpul_on_cmd(pattern=r"stegano ?(.*)"))
@pikpul.on(sudo_cmd(pattern=r"stegano ?(.*)", allow_sudo=True))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    await event.edit("hmm... Hiding Text Inside Image...")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("No input found!  --__--")
        return
    crypto_steganography = CryptoSteganography("hell")
    crypto_steganography.hide(img, "./fridaydevs/stegano.png", text)
    file_name = "stegano.png"
    ok = "./pikpuldevs/" + file_name
    await borg.send_file(
        event.chat_id,
        ok,
        force_document=True,
        allow_cache=False,
    )
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


@Pikpul.on(Pikpul_on_cmd(pattern=r"unstegano"))
@Pikpul.on(sudo_cmd(pattern=r"unstegano", allow_sudo=True))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    await event.edit("hmm... Searching for Text Inside The Image...")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    crypto_steganography = CryptoSteganography("hell")
    secret = crypto_steganography.retrieve(img)

    await event.edit(
        f"<b><u>Decrypted Text Successfully</b></u> \n<b>text</b>:-  <code>{secret}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "steganography": "**Steganography**\
\n\n**Syntax : **`.stegano <text> <Reply To A image>`\
\n**Usage :** Hides Given Text Inside Image.\
\n\n**Syntax : **`.unstegano <Reply To The image>`\
\n**Usage :** Reveals Hidden Text From Image.\
\n\n**Example :** `.stegano hello this is secret message` <replying to an image>.\
\n\n**What is Steganography :** Steganography is the art and science of writing hidden messages in such a way that no one, apart from the sender and intended recipient, suspects the existence of the message, a form of security through obscurity. Additionally this plugin also enhance the security of the steganography through data encryption. The data concealed is encrypted using AES 256 encryption, a popular algorithm used in symmetric key cryptography."
    }
)
