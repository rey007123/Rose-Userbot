from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.cobadulu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1.2)
    await typew.edit("**Coba**")
    sleep(1.2)
    await typew.edit("**dicoba**")
    sleep(1.2)
    await typew.edit("**Testes**")

CMD_HELP.update({
    "coba":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.cobadulu`\
