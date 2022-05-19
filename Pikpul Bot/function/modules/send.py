import asyncio
from datetime import datetime

from Pikpulbot import CMD_HELP
from Pikpulbot.utils import Pikpul_on_cmd, sudo_cmd

Pikpulthumb = "./resources/IMG_20200929_103719_628.jpg"


@Pikpul.on(Pikpul_on_cmd(pattern="send ?(.*)"))
@Pikpul.on(sudo_cmd(pattern="send ?(.*)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    the_plugin_file = "./fridaybot/modules/{}.py".format(input_str)
    end = datetime.now()
    (end - start).seconds
    men = f"Plugin Name - {input_str}.py \nUploaded By Pikpul"
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        thumb=Pikpulthumb,
        caption=men,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    await asyncio.sleep(5)
    await event.delete()


CMD_HELP.update(
    {
        "send": "**Send**\
\n\n**Syntax : **`.send <plugin name>`\
\n**Usage :** sends the plugin."
    }
)
