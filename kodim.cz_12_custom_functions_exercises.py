import random

"""Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek."""
def mult(cislo_1, cislo_2):
    return(cislo_1 * cislo_2)

print(f'Funkce mult vrací {mult(10, 3)}')


"""Převod kilometrů na míle a zpět
Napište dvě funkce: kilometry_na_mile(kilometry) a mile_na_kilometry(mile), které provedou převod mezi kilometry a mílemi."""

def kilometry_na_mile(km): # parametr funkce znaci jenom pozici, ale neni to promenna, naopak ve vypoctu ho pak muzeme promennou nahradit
    return km * 0.621371192

def mile_na_kilometry(mile):
    return mile * 1.609
km = int(input('Zadej počet kilometrů: '))
mile = int(input('Zadej počet mil: '))

print(f'{km} km je: {round(kilometry_na_mile(km), 2)} mil, {mile} mil je: {mile_na_kilometry(mile)} km')

"""Převod rychlosti kilometrů za hodinu na míle za hodinu a zpět
Napište funkce: kmh_na_mph(kmh) a mph_na_kmh(mph), které umožní převod rychlosti mezi kilometry za hodinu a míli za hodinu."""
# 0,621371 mph = 1,609344 kmph

def kmh_na_mph(kmph):
    return kmph * 0.621371

def mph_na_kmph(mph):
    return mph * 1.609344

print(kmh_na_mph(12))
print(mph_na_kmph(14))


"""Převod teploty ze stupňů Celsia na Fahrenheit a zpět
Vytvořte dvě funkce: celsia_na_fahrenheit(teplota) a fahrenheit_na_celsia(teplota), které umožňují převod teploty mezi stupni 
Celsia a stupni Fahrenheit."""

def celsia_na_fahrenheit(teplota):
    return (9 * teplota) / 5 + 32 
    
def fahrenheit_na_celsia(teplota):
    return 5 * (teplota - 32) / 9

"""Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.
Zadej slovo: ahoj
********
* ahoj *
******** """

def frame():
    print("**" + len(user_input) * "*" + "**")
    print("* ", user_input, " *", sep="") 
    print("**", len(user_input)* "*", "**", sep="") # carka narozdil od plus dela mezery mezi elementy ** ***** **, proto sep

user_input = input('Zadej libovolne slovo:')

frame()


"""Bonus: Znak, kterým se má text obalit, bude zadán také jako parametr."""
def frame2(sign):
    print(2 * sign + len(user_input) * sign + 2 * sign)
    print(sign, " ", user_input, " ", sign, sep="")
    print(2 * sign + len(user_input) * sign + 2 * sign)

user_input = input('Zadej libovolne slovo:')

frame2('&')


"""Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. 
Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.
Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5."""
def month_of_birth(birth_number):
    month = int(birth_number[2:4]) # pozor na slicing, druha hodnota je exclusive
    if month > 50:
        month_result = month - 50
    else:
        month_result = month
    return month_result

birth_number = input('Zadej rodné číslo: ')
print(f'Měsíc narození je: {month_of_birth(birth_number)}')


"""Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. 
Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. 
Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True)."""

def total_price(persons, breakfast=False):
    osoba_noc = 850
    osoba_snidane = 125
    # if breakfast == False: 
    #     return persons * osoba_noc
    # else:
    #     return persons * (osoba_noc + osoba_snidane)

    if breakfast: 
    # tohle je uber python zapis, takhle se vzdycky se ptame jestli je proměnna true, tzn cokoliv jineho nez False, None, 0 a prazdne kontejnery jako [], {}, (), "" (prazdny retezec)
        return persons * (osoba_noc + osoba_snidane) 
    
    return persons * osoba_noc
        
#   return persons * (osoba_noc + osoba_snidane) - else tu vubec nemusi byt

    
result = total_price(10, True)
print(result)


"""Vypište seznam čísel každé na nový řádek zarovnané vpravo na délku nejdelšího čísla.
Návod:
    Zjistěte kolik znaků zabírá nejdelší číslo ze seznamu
    Napište funkci, která dostane řetězec a délku, na kterou má text vyplnit zleva mezerami
    Bonus: funkce bude mít volitelný parametr, jakým znakem má text vyplňovat"""

numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
length = 0
for a in numbers:
    if len(str(a)) > length:
        length = len(str(a))
print(length) # 9

def nubmers_framed(string: str, length: int, optional_sign=' '):
    print((optional_sign * (length - len(string))) + string)

for b in numbers:
    nubmers_framed(str(b), 9, '*')


"""Napiš funkci, která bude jednoduchou simulací rulety. Budeme uvažovat pouze možnost sázení na řady. Uživatel si může vybrat jednu ze tří řad:
první řada (hodnoty 1, 4, 7 atd.),
druhá řada (hodnoty 2, 5, 8 atd.),
třetí řada (hodnoty 3, 6, 9 atd.).

Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.
Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky. Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36. 
Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.
Funkce roulette vrací hodnotu výhry. Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, v opačném případě nevyhrává nic jeho sázka propadá."""

rada1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
rada2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
rada3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

row_and_bet = input('Uveď číslo řady, na kterou sázíš a kolik. Hodnoty odděl mezerou. ')
row_and_bet = row_and_bet.split(' ')
row = int(row_and_bet[0])
bet = int(row_and_bet[1])

def roulette(row_number, bet):
    number = random.randint(0, 36)
    if row_number == 1 and number in rada1:
        win = 2 * bet
        print(f'Padlo číslo {number}, vyhráváš {win}.')
    elif row_number == 2 and number in rada2:
        win = 2 * bet
        print(f'Padlo číslo {number}, vyhráváš {win}.')
    elif row_number == 3 and number in rada3:
        win = 2 * bet
        print(f'Padlo číslo {number}, vyhráváš {win}.')
    else:
        win = 0
        print(f'Padlo číslo {number}, prohráváš vše.')

roulette(row, bet)


"""Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena. Stačí, když první a poslední písmeno je na své pozici zachováno.
Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny znaky kromě prvního a posledního.
Nápověda: random.shuffle()"""

def letter_shuffle(word: str):
    word = list(word)
    slice = word[1:-1]
    random.shuffle(slice)
    word[1:-1] = slice
    return(', '.join(word))

print(letter_shuffle('tuberkulóza'))


"""Super bonus: Napiš program, který takovou funkci využije na delší text více slov."""
longer_text = '''Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena. Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny znaky kromě prvního a posledního.'''
def text_shuffle(text: str):
    text_list = text.split(' ')
    shuffled_text_list = []
    for word in text_list:
        word = list(word)
        if ',' or '.' in word: # tecka a carka mi v tom delaji bordel lepi se ke slovou, takhle je osetrim, ale jen pro tenhle konkretni text, funkce neni univerzalni
            slice = word[1:-2]
            random.shuffle(slice)
            word[1:-2] = slice
        else:
            slice = word[1:-1]
            random.shuffle(slice)
            word[1:-1] = slice
        shuffled_text_list.append(''.join(word))
    print(' '.join(shuffled_text_list))

text_shuffle(longer_text)
