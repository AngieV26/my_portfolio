import random

"""Uložte do proměnné jmeno svoje celé jméno a nechte vypsat jeho třetí, pátý a sedmý znak. 
Vyzkoušejte, co se stane, když budete chtít znak na pozici, která překračuje délku řetězce."""

jmeno = "Míla Nováčková"
print(f"{jmeno[2]} {jmeno[4]} {jmeno[6]}") #  záleží jestli počtáme od 1 nebo od nuly (prgramatorsky)
# print(jmeno[16]) #IndexError: string index out of range

"""Vytvořte nějaký seznam celých čísel, například počty diváků na několika po sobě jdoucích představeních.
Vytvořte nějaký seznam desetinných čísel, například zaplněnost divadla v několika po sobě jdoucích představeních.
Vytvořte nějaký seznam řetězců, například seznam názvů několika divadelních představení, která divadlo hraje. Uložte tento seznam do proměnné hry. 
Uložte do nějaké proměnné druhou položku tohoto seznamu.
Do proměnné hodnoceni uložte seznam hodnocení, které obdržela divadelní hra "Plyšáci na útěku" v různých recenzních časopisech. 
Hodnocení je vždy dvouprvkový seznam obsahující název recenzního časopisu jako řetězec a samotné hodnocení jako číslo mezi 1 až 10."""

pocet_divaku = [5, 8, 10, 14, 26]
zaplnenost_divadla = [0.18, 0.21, 0.36, 0.41, 0.66]
hry = ["Facka a placka", "Dařbuján a Pandrhola", "Bolek a Lolek"]
nejnastevovanejsi = hry[1] # 1 protoze zaciname od nuly
hodnoceni = [["Divadelní revue", 8], ["Skvost jeviště", 4], ["Řechtanda", 10]]


"""Ověřování hesla se někdy dělá tak, že se vás systém ptá pouze na některé jeho znaky. Napište program, který má uloženo heslo, které musí uživatel zadat. 
Pak se jej postupně zeptejte například na druhý, pátý a sedmý znak hesla. Propusťte uživatele pouze tehdy, zadá-li všechny tyto znaky správně.

Příklad použití pro heslo czechitas:

Zadej 2. znak hesla: z
Zadej 5. znak hesla: h
Zadej 7. znak hesla: t

Vstup povolen
Zadej 2. znak hesla: e
Zadej 5. znak hesla: h
Zadej 7. znak hesla: t

Vstup zamítnut
Bonus bonusu: Program náhodně vygeneruje na jaké tři písmena hesla se bude ptát."""

heslo = "simsalabim"
#        0123456789

znak1 = random.randint(1, len(heslo))
print(znak1)
overeni_1 = input(f"Zadej {znak1}. znak hesla: ")
if overeni_1 != heslo[znak1 - 1]:
    print("Vstup zamítnut")
    exit()

znak2 = random.randint(1, len(heslo))
overeni_2 = input(f"Zadej {znak2}. znak hesla: ")
if overeni_2 != heslo[znak2 - 1]:
    print("Vstup zamítnut")
    exit()

znak3 = random.randint(1, len(heslo))
overeni_3 = input(f"Zadej {znak3}. znak hesla: ")
if overeni_3 != heslo[znak3 - 1]:
    print("Vstup zamítnut")
    exit()

print("Úspěch")

#nebo: 

heslo = "czechitas"

znak = input("Zadej druhý znak hesla: ")
if znak != heslo[1]:
    print("Chyba")
    exit()
znak = input("Zadej pátý znak hesla: ")
if znak != heslo[4]:
    print("Chyba")
    exit()
znak = input("Zadej sedmý znak hesla: ")
if znak != heslo[6]:
    print("Chyba")
    exit()
print("Úspěch!")
