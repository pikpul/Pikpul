
import json
import os

from uniborg.util import Pikpul_on_cmd


@pikpul.on(pikpul_on_cmd(pattern="sch ?(.*)", allow_sudo=True))
async def sp_search(event):
    search_str = event.pattern_match.group(1)

    await event.edit("**Searching for " + search_str + " ...**")

    command = "sp --json " + search_str + " > out.json"

    os.system(command)

    f = open("out.json", "r").read()

    data = json.loads(str(f))

    msg = "**Search Query** \n`" + search_str + "`\n**Results**\n"

    for element in data:
        msg = msg + "⁍ [" + element["title"] + "](" + element["link"] + ")\n\n"

    await event.edit(msg
