import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
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
barris_ciphra = [{
    21: "A",
    22: "B",
    23: "C",
    31: "D",
    32: 'E',
    33: 'F',
    41: 'G',
    42: 'H',
    43: 'I',
    51: 'J',
    52: 'K',
    53: 'L',
    61: 'M',
    62: 'N',
    63: 'O',
    71: 'P',
    72: 'Q',
    73: 'R',
    74: 'S',
    81: 'T',
    82: 'U',
    83: 'V',
    91: 'W',
    92: 'X',
    93: 'Y',
    94: 'Z'
},
    {
        21: "a",
        22: "b",
        23: "c",
        31: "d",
        32: 'e',
        33: 'f',
        41: 'g',
        42: 'h',
        43: 'i',
        51: 'j',
        52: 'k',
        53: 'l',
        61: 'm',
        62: 'n',
        63: 'o',
        71: 'p',
        72: 'q',
        73: 'r',
        74: 's',
        81: 't',
        82: 'u',
        83: 'v',
        91: 'w',
        92: 'x',
        93: 'y',
        94: 'z'
    }

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
    for i in range(7):

        n = random.randrange(0, 9 )
        a_z = random.randrange(0, 25)
        symb = random.randrange(0, 8)
        for a in range(3):
            passwords.append(complete_charset[0][n])
            passwords.append(Alphabet_a[a_z])
            passwords.append(complete_charset[1][symb])
    rbkname = random.shuffle(passwords)
    new_password = "".join(passwords)
    list.append(new_password)
    return new_password


def Crypt(string):
    new = list(string)
    rbkstr = random.shuffle(new)
    for i in range(10):
        num = random.randrange(0, 255)
        snum = str(num)
    new = snum.join(new)
    test = random.randrange(0, 65536)
    test = str(test)
    new = new.replace(" ", test)
    cryp = list(new)
    PasswGen(cryp)
    cryp = "".join(cryp)
    return cryp


def Crypt2(func_string):
    new = list(func_string)
    for i in range(15):
        num = random.randrange(0, 65536)
        snum = str(num)
    new = snum.join(new)
    test = random.randrange(0, 4294967296)
    test = str(test)
    new = new.replace(" ", test)
    cryp = list(new)
    PasswGen(cryp)
    cryp = "".join(cryp)
    return cryp

def CotCoinData(coin):
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    brw = webdriver.Chrome(chrome_options=opt)
    brw.get("https://www.google.com/")
    brw.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação" + coin)
    brw.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
    cotacao = brw.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
    return f" a cotação da moeda {coin} é de R$" + cotacao
