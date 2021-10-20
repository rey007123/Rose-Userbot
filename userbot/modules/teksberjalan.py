import random
import sys
import time
from userbot.events import register

@register(outgoing=True, pattern='^.hayyo(?: |$)(.*)')
async def typewriter(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
typewriter('Ikan Cucut\nur so Cute\nI love u')
