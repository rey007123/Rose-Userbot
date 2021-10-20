import random
import sys
import time

@register(outgoing=True, pattern='^.hayyo(?: |$)(.*)')
async def typewriter(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik('**Ikan Cucut \Ur so Cute \I love u**')
