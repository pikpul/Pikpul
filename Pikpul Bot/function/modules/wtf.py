"""Emoji
Available Commands:
.wtf"""


import asyncio

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@pikpul.on(friday_on_cmd("wtf"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
        "What",
        "What The",
        "What The F",
        "What The F Brah",
        "[What The F Brah](https://te.legra.ph/file/82d85673ef6c8c8d4a4eb.jpg)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])


CMD_HELP.update(
    {
        "wtf": "**wtf**\
\n\n**Syntax : **`.wtf`\
\n**Usage :** Creates wtf expression with text."
    }
)
