import random
import time
Alfabeto = [
    "A",
    "B",
    'C',
    'D',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]
def Conbinator(lista):
    name = []
    for i in range(9):
        x = random.randrange(0, 25)
        name.append(Alfabeto[x])
    rbkname = random.shuffle(name)
    nome_atualizado = "".join(name)
    lista.append(nome_atualizado)
    return nome_atualizado

def winLoop():
    t = 1
    while t > 0:
        time.sleep(1)