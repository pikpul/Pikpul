"""Emoji
Available Commands:
.support
Credits to noone
"""


import asyncio

from pikpulbot import CMD_HELP
from pikpulbot.utils import pikpul_on_cmd


@pikpul.on(pikpul_on_cmd("pikpul"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "support":
    await event.edit("for our support group")
    animation_chars = [
        "Click here",
        "[Support Group](https://t.me/Gianicbotsupport)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


CMD_HELP.update(
    {
        "supportgroup": "**Support Group**\
\n\n**Syntax : **`.pikpul`\
\n**Usage :** Creates link for pikpul support group."
    }
)
