import random
import time
AlfabetoA = [
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
Alfabetoa = [
    "a",
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]
complete_charset = ([[

    "a",
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
],
    [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9'
    ],
    [
        '!',
        '@',
        '#',
        '$',
        '%',
        '¨',
        '&',
        '*',
        "("
    ]
    
])
def Conbinator(lista):
    name = []
    for i in range(9):
        x = random.randrange(0, 25)
        name.append(AlfabetoA[x])
    rbkname = random.shuffle(name)
    nome_atualizado = "".join(name)
    lista.append(nome_atualizado)
    return nome_atualizado

def winLoop():
    t = 1
    while t > 0:
        time.sleep(1)
def Combinator_n(lista):
    name = []
    for i in range(11):
        x = random.randrange(0, 25)
        name.append(Alfabetoa[x])
    rbkname = random.shuffle(name)
    nome_atualizado = "".join(name)
    lista.append(nome_atualizado)
    return nome_atualizado

def PasswGen(lista):
    senhas = []
    for i in range(11):
        n = random.randrange(0, 9 )
        a_z = random.randrange(0, 25)
        symb = random.randrange(0, 8)

        senhas.append(complete_charset[1][n])
        senhas.append(complete_charset[0][a_z])
        senhas.append(complete_charset[2][symb])
        rbkname = random.shuffle(senhas)
        senha_atualizada = "".join(senhas)
        lista.append(senha_atualizada)
        return senha_atualizada

testes = []
PasswGen(testes)
