import random
import sys
import time

@register(outgoing=True, pattern='^.hayyo(?: |$)(.*)')
async def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik('**Ikan Cucut \Ur so Cute \I love u**')
