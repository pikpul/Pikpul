from asyncio import wait

from pikpulbot import CMD_HELP
from pikpulbot.utils import pikpul_on_cmd


@pikpul.on(pikpul_on_cmd("repeat ?(.*)"))
async def _(event):
    message = event.text[10:]
    count = int(event.text[8:10])
    repmessage = message * count
    await wait([event.respond(repmessage) for i in range(count)])
    await event.delete()


CMD_HELP.update(
    {
        "repeat": "**Repeat**\
\n\n**Syntax : **`.repeat <number of times to repeat> <text to repeat>`\
\n**Usage :** repeats the given text with given number of times."
    }
)
