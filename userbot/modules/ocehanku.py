from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sabar(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Sabar aja lah ya`")
    sleep(0.7)
    await typew.edit("`\Sabar aja lah ya`"
                     "`\Hati kamu itu kan kaya Tango`")
    sleep(0.7)
    await typew.edit("`\Sabar aja lah ya`"
                     "`\Hati kamu itu kan kaya Tango`"
                     "`\Berapa lapis?`")
    sleep(0.7)
    await typew.edit("`\Sabar aja lah ya`"
                     "`\Hati kamu itu kan kaya Tango`"
                     "`\Berapa lapis?`"
                     "`\Ratusan😅`")

CMD_HELP.update({
    
"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sabar`\
    \n↳ : Sabaro\
})            
