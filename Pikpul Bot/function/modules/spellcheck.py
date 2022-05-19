from textblob import TextBlob

from Pikpulbot import CMD_HELP
from Pikpulbot.utils import admin_cmd


@Pikpul.on(admin_cmd(pattern="spellcheck (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    a = input_str

    # print("original text: "+str(a))
    b = TextBlob(a)
    # print("corrected text: "+str(b.correct()))
    c = b.correct()
    await event.edit(
        f"<b><u>Check Completed</b></u> \n\n<b>Original Text</b>:-  <code>{a}</code> \n<b>Corrected Text:-</b> <code>{c}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "spellcheck": "**Spell Checker**\
\n\n**Syntax : **`.spellcheck <text to check>`\
\n**Usage :** Checks for spelling mistakes in given text."
    }
)
