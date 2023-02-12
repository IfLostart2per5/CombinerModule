import random
import time
Alphabet_A = [
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
Alphabet_a = [
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
complete_charset =[
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
        '-',
        '&',
        '*',
        "("
    ]
    
]
def Conbinator(list):
    name = []
    for i in range(9):
        x = random.randrange(0, 25)
        name.append(Alphabet_A[x])
    rbkname = random.shuffle(name)
    new_name= "".join(name)
    list.append(new_name)
    return new_name

def winLoop():
    t = 1
    while t > 0:
        time.sleep(1)
def Combinator_n(list):
    name = []
    for i in range(11):
        x = random.randrange(0, 25)
        name.append(Alphabet_a[x])
    rbkname = random.shuffle(name)
    new_name = "".join(name)
    list.append(new_name)
    return new_name

def PasswGen(list):
    passwords = []
    for i in range(10):
        n = random.randrange(0, 9 )
        a_z = random.randrange(0, 25)
        symb = random.randrange(0, 8)
        for a in range(5):
            passwords.append(complete_charset[0][n])
            passwords.append(complete_charset[1][symb])
        rbkname = random.shuffle(passwords)
        new_password = "".join(passwords)
        list.append(new_password)
        return new_password



