""" Whatever Plugin by Noobs of Telegram i.e. @Nikhil_LoGo_MaKer """

from uniborg.util import pikpul_on_cmd

from pikpulbot import CMD_HELP


@pikpul.on(pikpul_on_cmd(pattern=r"lmoon"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        "ππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππ€π»πππππ€π»π\nππππππππ\nππππππππ\nππππππππ"
    )


@pikpul.on(pikpul_on_cmd(pattern=r"city"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        """ββπ      β           β
       β  β         β    π    β    β        β          β     β   β
π¬π¨π«π’π€π₯π¦πͺπ«
              π²/     lπ\π³π­
           π³/  π l  π \π΄ π¬                       π¬  π΄/            l  π    \π²
      π²/   π     l               \
   π³/πΆ           |   π         \ π΄π΄π΄
π΄/                    |                     \π²"""
    )


@pikpul.on(pikpul_on_cmd(pattern=r"hello"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("πΊβ¨β¨πΊβ¨πΊπΊπΊ\nπΊβ¨β¨πΊβ¨β¨πΊβ¨\nπΊπΊπΊπΊβ¨β¨πΊβ¨\nπΊβ¨β¨πΊβ¨β¨πΊβ¨\nπΊβ¨β¨πΊβ¨πΊπΊπΊ\nββββββββ")


@pikpul.on(pikpul_on_cmd(pattern=r"cheer"))
async def cheer(event):
    if event.fwd_from:
        return
    await event.edit(
        "ππππππ\nβ Cheer Up  π΅\nπ β¨ )) β¨  π\nπβ (( * β£β π\nπβ*π β£β π \nπββββ  ππ For YOU  π°\nππππππ"
    )


@pikpul.on(pikpul_on_cmd(pattern=r"getwell"))
async def getwell(event):
    if event.fwd_from:
        return
    await event.edit("πΉπΉπΉπΉπΉπΉπΉπΉ \nπΉπ·π’ππ·π’π¨πΉ\nπΉπππ΅ππππΉ\nπΉ GetBetter Soon! πΉ\nπΉπΉπΉπΉπΉπΉπΉπΉ")


@pikpul.on(pikpul_on_cmd(pattern=r"sprinkle"))
async def sprinkle(event):
    if event.fwd_from:
        return
    await event.edit(
        "β¨.β’*Β¨*.ΒΈ.β’*Β¨*.ΒΈΒΈ.β’*Β¨*β’ ΖΈΣΖ·\nπΈπΊπΈπΊπΈπΊπΈπΊ\n Sprinkled with loveβ€\nπ·π»π·π»π·π»π·π»\n Β¨*.ΒΈ.β’*Β¨*. ΒΈ.β’*Β¨*.ΒΈΒΈ.β’*Β¨`*β’.β¨\nπΉππΉππΉππΉπ"
    )


CMD_HELP.update(
    {
        "something": "**Something**\
\n\n**Syntax : **`.lmoon`\
\n**Usage :** creates funny emoji with moons.\
\n\n**Syntax : **`.city`\
\n**Usage :** creates funny city emoji.\
\n\n**Syntax : **`.hello`\
\n**Usage :** creates hello text to wish.\
\n\n**Syntax : **`.cheer`\
\n**Usage :** creates funny emoji.\
\n\n**Syntax : **`.getwell`\
\n**Usage :** creates funny emoji to show getwell.\
\n\n**Syntax : **`.sprinkle`\
\n**Usage :** creates funny text emoji."
    }
)
