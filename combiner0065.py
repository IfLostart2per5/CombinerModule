import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

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
complete_charset = [
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

class WebFunctions:
    def __init__(self):
        pass

    def Translate(self, text, lang=None):
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        self.brw = webdriver.Chrome(options=opt)
        self.brw.get("https://translate.google.com")
        self.brw.find_element('xpath',
                         '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button').click()
        time.sleep(0.7)
        if lang is not None:
            self.brw.find_element('xpath',
                            '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[2]/input').send_keys(
                lang)
        else:
            self.brw.find_element('xpath',
                                  '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[2]/input').send_keys(
                "Português")
        self.brw.find_element('xpath',
                         '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[2]/input').send_keys(
            Keys.ENTER)
        self.brw.find_element('xpath',
                         '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys(
            text)
        translated = self.brw.find_elements(By.CLASS_NAME, 'ryNqvb')
        return translated

    def CotCoinData(self, coin1, coin2):
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        self.brw = webdriver.Chrome(options=opt)
        self.brw.get("https://www.google.com/")
        self.brw.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
            f"cotação {coin1}-{coin2}")
        self.brw.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
            Keys.ENTER)
        cotacao = self.brw.find_element('xpath',
                                   '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute(
            'data-value')
        cot = round(float(cotacao), 2)
        cot = str(cot)
        cot = cot.replace(".", ",")
        return f" a cotação da moeda {coin1} para {coin2} é de {coin2} {cot}"

def winLoop():
    t = 1
    while t > 0:
        time.sleep(1)

class RandGens:
    def __init__(self):
        pass
    def Combinator_N(self, list=None):
        name = []
        for i in range(9):
            x = random.randrange(0, 25)
            name.append(Alphabet_A[x])
        _ = random.shuffle(name)
        new_name = "".join(name)
        if list is not None:
            return list.append(new_name)
        else:
            return new_name


    def NumGen(self, list=None):
        self.name = []
        for i in range(9):
            x = random.randrange(0, 9)
            self.name.append(complete_charset[0][x])
        self._ = random.shuffle(self.name)
        self.new_name = "".join(self.name)
        if list is not None:
            return list.append(self.new_name)
        else:
            return self.new_name





    def Combinator_n(self, list=None):
        self.name = []
        for i in range(11):
            x = random.randrange(0, 25)
            self.name.append(Alphabet_a[x])
        self._ = random.shuffle(self.name)
        self.new_name = "".join(self.name)
        if list is not None:
            return list.append(self.new_name)
        else:
            return self.new_name


    def PasswGen(self, list=None):
        self.passwords = []
        for i in range(7):

            self.n = random.randrange(0, 9)
            self.a_z = random.randrange(0, 25)
            self.symb = random.randrange(0, 8)
            for a in range(3):
                self.passwords.append(complete_charset[0][self.n])
                self.passwords.append(Alphabet_a[self.a_z])
                self.passwords.append(complete_charset[1][self.symb])
        self._ = random.shuffle(self.passwords)
        self.new_password = "".join(self.passwords)
        if list is not None:
            return list.append(self.new_password)
        else:
            return self.new_password

    def EmailGen(self, list=None):
        print("""Remember of this indexes
         index 0 = google domain (@gmail.com)
        index 1 = microsoft hotmail domain (@hotmail.com) 
        index 2 = microsoft outlook domain (@outlook.com) 
        index 3 = yahoo domain (@yahoo.com)""")
        index = int(input("insert a number of 0 to 3: "))
        extensions = [
            "@gmail.com",
            "@hotmail.com",
            "@outlook.com",
            "@yahoo.com"
        ]
        self.emails = [

        ]
        self.Combinator_n(self.emails)
        emailAddExtension = self.emails[0] + extensions[index]
        if list is not None:
            self.email = list.append(emailAddExtension)
        else:
            return self.email

class Cryptograph:
    def __init__(self):
        pass
    def Crypt(self, string, decrypt=None):

        print("""ALERT!
            This function (Crypt Level 1) is being developed, and because it is not complete, so,
             DO NOT USE FOR REAL PRODUCTIONS, chances are your file will be decrypted easily if you
            use it while it is not complete.""")
        rdg = RandGens()

        self.new = list(string)
        self._ = random.shuffle(self.new)
        for i in range(10):
            num = random.randrange(0, 255)
            snum = str(num)
        self.new = snum.join(self.new)
        test = random.randrange(0, 65536)
        test = str(test)
        self.new = self.new.replace(" ", test)
        self.cryp = list(self.new)
        rdg.PasswGen(self.cryp)
        cryp = "".join(self.cryp)
        return cryp


    def Crypt2(self, func_string):
        print("""ALERT!
            This function (Crypt Level 2) is being developed, and because it is not complete, so,
             DO NOT USE FOR REAL PRODUCTIONS, chances are your file will be decrypted easily if you
            use it while it is not complete.""")
        rdg = RandGens()
        self.new = list(func_string)
        for i in range(15):
            num = random.randrange(0, 65536)
            snum = str(num)
        self.new = snum.join(self.new)
        self.test = random.randrange(0, 4294967296)
        self.test = str(self.test)
        self.new = self.new.replace(" ", self.test)
        self.cryp = list(self.new)
        rdg.PasswGen(self.cryp)
        self.cryp = "".join(self.cryp)
        return self.cryp

domain_at = "@"
domain_com = ".com"
senhas_idiotas = [
    "12345678",
    "12345677",
    "12345777",
    "12345677",
    '123456789',
    'password1',
    '1234567890',
    "joaoGostosao",
    "manuSafada"
]


class Cadastro:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

        if len(self.senha) >= 8:
            pass
        else:
            raise Exception("A senha precisa ter no minimo 8 caracteres!")
        if domain_at not in self.email:
            raise Exception("Email inválido!")
        if domain_com not in self.email:
            raise Exception("Email inválido!")
        for passw in senhas_idiotas:
            if passw == self.senha:
                raise Exception("Senha muito fácil!")
    rdg = RandGens()

    a = rdg.NumGen()

    def AccountLog(self):
        rdg = RandGens()
        user = Cadastro(self.nome, self.email, self.senha)
        if os.path.isdir("logstests"):
            os.mkdir(f"./logstests/{self.a}")
        else:
            os.makedirs(f"./logstests")
        unfile = f"logstests/{self.a}/accountdata_id-{self.a}.py"
        dataaccount = open(unfile, 'w', encoding="utf-8")
        info = {"Nome": user.nome,
                "Email": user.email,
                "Senha": user.senha,
                "Identificador": rdg.PasswGen()
                }
        flid = {
            "Id do arquivo": self.a
        }
        if os.path.isfile("logstests/flidbase.py"):
            idfl = open("./logstests/flidbase.py", "a", encoding="utf-8")
            ident = {
                "Nome": self.nome,
                "Flid": self.a
            }
            idfl.write(f"""
           
            Identifier = {ident}
            """)
        else:
            idfile = f'logstests/flidbase.py'
            idfl = open(idfile, "w")
            idfl.write(f"base = {flid}")
        dataaccount.write(f"""
        dataAccount = {info}""")

class MathCB:
    def __init__(self):
        pass
    class Triangle:
        def __init__(self, ol, oa, h):
            self.ca = oa
            self.co = ol
            self.h = h
    def sqrt(self, x):
        return x ** (1/2)
    def cbrt(self, x):
        return x ** (1/3)
    def frrt(self, x):
        return x ** (1/4)
    def ftrt(self, x):
        return x ** (1/5)
    def sxrt(self, x):
        return x ** (1/6)


    def f_hipo(self, tria):
        if type(tria) is self.Triangle:
            cato, cata = getattr(tria, "co"), getattr(tria, "ca")
            hipotenusa = self.sqrt(cato ** 2 + cata ** 2)
            hipotenusa = round(hipotenusa, 3)
            return hipotenusa
        elif type(tria) is list:
            cato, cata = tria[0], tria[1]
            hipotenusa = self.sqrt(cato ** 2 + cata ** 2)
            hipotenusa = round(hipotenusa, 3)
            return hipotenusa
        elif type(tria) is dict:
            cato, cata = tria['co'], tria['ca']
            hipotenusa = self.sqrt(cato ** 2 + cata ** 2)
            hipotenusa = round(hipotenusa, 3)
            return hipotenusa
        elif type(tria) is tuple:
            cato, cata = (tria[0], tria[1])
            hipotenusa = self.sqrt(cato ** 2 + cata ** 2)
            hipotenusa = round(hipotenusa, 3)
            return hipotenusa
        else:
            raise Exception("O objeto colocado não é algo iterável")

    def fnrr(self, compare1, valuep, compare2):
        if valuep - compare1 < compare2 - valuep:
            return f"""the more near square root of {valuep} is {compare1}
    with the problem: {valuep} - {compare1} = {valuep - compare1}
    and the diference to the another root: {compare2} - {valuep} = {compare2 - valuep}
    """
        else:

            return f"""the more near square root of {valuep} is {compare2}
    with the problem: {compare2} - {valuep} = {compare2 - valuep}
    and the diference to the another root: {valuep} - {compare1} = {valuep - compare1}"""

    def sen(self, tria):

        if type(tria) is self.Triangle:
            cato, hipo = getattr(tria, "co"), getattr(tria, "h")
            return cato / hipo
        elif type(tria) is list:
            cato, hipo = tria[1], tria[2]
            return cato / hipo
        elif type(tria) == dict:
            cato, hipo = tria['co'], tria['h']
            return cato / hipo
        elif type(tria) == tuple:
            cato, hipo = (tria[1], tria[2])
            return cato / hipo
        else:
            raise Exception("O objeto colocado não é algo iterável")


    def cos(self, tria):

        if type(tria) is self.Triangle:
            cata, hipo = getattr(tria, "ca"), getattr(tria, "h")
            return cata / hipo
        elif type(tria) is list:
            cata, hipo = tria[1], tria[2]
            return cata / hipo
        elif type(tria) == dict:
            cata, hipo = tria['ca'], tria['h']
            return cata / hipo
        elif type(tria) == tuple:
            cata, hipo = (tria[1], tria[2])
            return cata / hipo
        else:
            raise Exception("O objeto colocado não é algo iterável")


    def tg(self, tria):
        if type(tria) is self.Triangle:
            cato, cata = getattr(tria, "co"), getattr(tria, "ca")
            return cato / cata
        elif type(tria) is list:
            cato, cata = tria[0], tria[1]
            return cato / cata
        elif type(tria) == dict:
            cato, cata = tria['co'], tria['ca']
            return cato / cata
        elif type(tria) == tuple:
            cato, cata = (tria[0], tria[1])
            return cato / cata
        else:
            raise Exception("O objeto colocado não é algo iterável")

    def sec(self, tria):
        return 1 / self.cos(tria)
    def cossec(self, tria):
        return 1 / self.sen(tria)
    def cotg(self, tria):
        return 1 / self.tg(tria)

    def CART(self, triang):
        hypotenuse = self.f_hipo(triang)
        sine = self.sen(triang)
        cosine = self.cos(triang)
        secant = self.sec(triang)
        cosecant = self.cossec(triang)
        cotangent = self.cotg(triang)
        print(f""" 
        hypoenuse of this triangle is {hypotenuse},
        sine of this triangle is {sine},
        cosine of this triangle is {cosine}, 
        the secant of this triangle is {secant}, 
        the cosecant of this triangle is {cosecant}, 
        the cotangent of this triangle is {cotangent}
        """)
    def pw(self, base, expo):
        return base ** expo



