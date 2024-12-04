import math

"""Následující text převeďte na množinu unikátních znaků, zjistěte počet unikátních znaků a vypište jejich seřazený seznam."""

text = '''Prágl
Prágl, po anglánsku Prague nebo Praha nebo v Cajsku, je taková lochna
v tem kuse hródy někde za čárama naši domoviny, kde se zoncna už
nechláme a kde se prndá po cajzlovsku. A ještě k temu tam majó sicnu
těžcí papaláši, kvůli čemu ho má každé v láfu jako kaktus ve véfuku.
Z Práglu bere kramále aj ten jejich len kerému se péruje Vltava.

O Práglu se taky kóří, pač tam majó hafo retychů pro všecky. Kromě
bůry švédských retychů só aj dva v Olmecu a jeden v Bučovicách.
To my z našeho štatlu radši hážem lulec do kašny na Zelňáku. Když
ale nekdo vopruboval zašrajbčit náš barocké Parnas do cancu retychů
pro všecky, přišmrdolili se ti Švédi s tým, že só proti a hókajó po
celé hródě, že ta vasra v tem se dá chlemtat.
'''
unique_sign_set = set()
for x in text:
    unique_sign_set.add(x) # opakujici honota se znovu neprida

print(unique_sign_set)
print(len(unique_sign_set))

list = list(unique_sign_set)
print(sorted(list))

# mnozina = set(text) rovnou prevede text na mnozinu a dpulicitni hodnoty vyeliminuje
# print(len(mnozina), sorted(mnozina)) --> sorted meni mnozinu primo na seznam


"""Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. 
Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). 
Vypiš obsah slovníku pomocí funkce print()."""

school_report = {"cestina": 1, "matika": 2, "dejepis": 2}
print(school_report) # {'cestina': 1, 'matika': 2, 'dejepis': 2}
print(school_report["cestina"], school_report["matika"], school_report["dejepis"]) # 1 2 2


"""Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujícím slovníku najdeš tři knihy a 
u každé z nich je počet prodaných kusů. Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", 
která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů.
U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100."""

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
sales["Noc, která mě zabila"] = 0 # polozku pridam prostym urcenim noveho indexu (klice) a hodnoty
sales["Vrah zavolá v deset"] += 100 # editace skrze agregaci
print(sales["Vrah zavolá v deset"])


"""V následujícím slovníku jsou uložena čísla lístků tomboly a příslušné výhry.
Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na int!
Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text "Bohužel nevyhráváš nic." 
Pokud číslo ve slovníku je, vypiš uživateli, co vyhrál. """

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
# je dobrou praxi na konci seznamu, slovniku atp napsat carku, nic nedela, ale je to zvyk, dulezita je zejmena pokud piseme vicero retezcu na vicero radku

ticket = int(input("Zadej číso svého soutěžního lístku: "))
if ticket in tombola: # nejsem si jiata, ale in oprator je asi mozne pouzit i na hodnoty pomoci in dict.values()
    print(f"Vyhráváš: {tombola[ticket]}")
else:    
    print("Bohužel nevyhráváš nic.")

print(tombola.values()) # .values vraci seznam hodnot, dict_values(['Láhev kvalitního vína Château Headache', 'Pytel brambor z místního družstva', ..., 'Společenská hra Sázky a dostihy'])


"""Uvažujme vysvědčení, které máme zapsané jako slovník.

Napiš program, který spočte průměrnou známku ze všech předmětů.
Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1."""

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}
mark_sum = 0
for mark in school_report.values():
    mark_sum += mark
mark_avg = mark_sum / len(school_report)
print(mark_avg)

for subject, mark in school_report.items():
    if mark == 1:
        print(subject)


"""Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. 
Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

Napiš program, který spočte celkový počet stran, které Gustav přečetl.
Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
"""
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

pages = 0
rating_above_8 = 0
for x in books:
    pages += x["pages"]
    if x["rating"] >= 8:
            rating_above_8 += 1
print(pages, rating_above_8)


"""V následujícím slovníku je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. 
Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) 
řetězce v klíči je písmeno P."""

plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}

for a, b in plates.items():
    if a[1] == "P":
        print(f"Vozidlo pod SPZ {a} majitele {b} je registrováno v Plzeňském kraji.")

# jina moznost reseni:
for a in plates.keys():
    if a[1] == "P":
        print(f"Vozidlo pod SPZ {a} majitele {plates[a]} je registrováno v Plzeňském kraji.")

"""Pohlédněte na následující reprezentaci receptu. Uložte si tuto strukturu do proměnné recept na začátek nového programu. 
Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru."""

recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

ingredients_price_list = []
ingredients_price_list2 = []
ingredients_price_sum = 0

for ingredient in recept["ingredience"]:
    ingredients_price_list.append(ingredient[2])

for x in ingredients_price_list:
    y = x.split(" ")
    ingredients_price_list2.append(float(y[0]))

for z in ingredients_price_list2:
    ingredients_price_sum += z

print(ingredients_price_sum)

# jine reseni:
price = 0
for ingredient in recept['ingredience']:
    price_currency_split = ingredient[2].split(" ")
    price += float(price_currency_split[0])

print(math.ceil(price))


"""Spolubydlící - cvičení na doma"""

purchase_list = [
    {"Jméno": "Petr", "Položka": "Prací prášek", "Částka": 399},
    {"Jméno": "Ondra", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Petr", "Položka": "Toaletní papír", "Částka": 65},
    {"Jméno": "Libor", "Položka": "Pivo", "Částka": 124},
    {"Jméno": "Petr", "Položka": "Pytel na odpadky", "Částka": 75},
    {"Jméno": "Míša", "Položka": "Utěrky na nádobí", "Částka": 130},
    {"Jméno": "Ondra", "Položka": "Toaletní papír", "Částka": 120},
    {"Jméno": "Míša", "Položka": "Pečící papír", "Částka": 30},
    {"Jméno": "Zuzka", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Pavla", "Položka": "Máslo", "Částka": 50},
    {"Jméno": "Ondra", "Položka": "Káva", "Částka": 300}
]
sum_per_person = {}
for item in purchase_list:
    person = item["Jméno"] # misto klice pouzivam promennou
    value = item["Částka"]
    if person in sum_per_person:
        sum_per_person[person] += value # promennou se da potom indexovat
    else:
        sum_per_person[person] = value
print(sum_per_person) # {'Petr': 539, 'Ondra': 500, 'Libor': 124, 'Míša': 160, 'Zuzka': 80, 'Pavla': 50}

"""Zkus dotáhnout náš program na finanční vypořádání spolubydlících. Z lekce si můžeš zkopírovat kódy, 
které vytvoří slovník s útratami jednotlivých spolubydlících a výpočet průměrné útraty na osobu. Dopiš cyklus, 
který projde slovník sum_per_person a pro každého ze spolubydlících vypíše, kolik by měl doplatit 
(pokud utratil(a) méně než průměr), případně kolik by měl obdržet (pokud utratil(a) více než průměr)."""

total_value = 0
for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")

average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")

for person, value in sum_per_person.items():
    difference = round(average_value - value)
    if difference > 0:
        print(f'{person} musí doplatit {difference} Kč.')
    else:
        print(f'{person} musí dostat zpět {difference * -1} Kč.')