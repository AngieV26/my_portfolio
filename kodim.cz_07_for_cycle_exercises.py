"""Mějme seznam hodnocení divadelní hry Plyšáci na útěku , který vypadá takto:

hodnoceni = [7, 9, 6, 7, 9, 8]
Vytvořte program, který projde tento seznam a vypíše každé hodnocení na nový řádek.
Upravte program tak, aby vypisoval výstup v tomto formátu
7/10
9/10
..."""

hodnoceni = [7, 9, 6, 7, 9, 8]

for h in hodnoceni:
    print(f"{h}/10")

"""Založte si program hesla.py a na jeho začátek vložte následující kód obsahující seznam hesel pro přihlášení do nějakého systému.
Pomocí cyklu vypište všechny hesla na obrazovku, každé na jeden řádek.
Upravte váš program tak, aby vypisoval jen bezpečná hesla, tedy taková, jež jsou delší než 8 znaků."""

hesla = [
    "xyz101",
    "punťa",
    "razor-blade",
    "1234",
    "12011986",
    "martin111",
    "trhnisi",
    "hokuspokus",
    "jeník15",
    "kristus-te-spasi",
    "beruška",
    "strčprstskrzkrk",
]
for heslo in hesla:
    if len(heslo) > 7:
        print(heslo)


"""Založte si program cykly02.py a použijte v něm následující seznam měsíců v roce, Všimněte si, že je to seznam seznamů.
Pomocí cyklu projděte tento seznam a vypište na výstup názvy jednotlivých měsíců.
Pomocí dalšího cyklu vypište na výstup počty dní v jednotlivých měsících."""

mesice = [
    ["leden", 31],
    ["únor", 28],
    ["březen", 31],
    ["duben", 30],
    ["květen", 31],
    ["červen", 30],
    ["červenec", 31],
    ["srpen", 31],
    ["září", 30],
    ["říjen", 31],
    ["listopad", 30],
    ["prosinec", 31],
]

for mesic in mesice:
    print(mesic[0])

for mesic in mesice:
    print(mesic[1])

"""Následující seznam obsahuje seznam všech divadelních her, které se hrají v divadle Pěst na oko. Každá hra má svůj název a trvání v minutách.
Pomocí cyklu projděte tento seznam a vypište na výstup názvy všech her.
Vypište na výstup názvy všech her, které trvají více než 120 minut.
Vypište na výstup názvy všech her spolu s jejich trváním v hodinách a minutách."""

hry = [
    ["Ňadro na ňadru na nádru", 180],
    ["Útok plyšových krokodýlů", 95],
    ["Cesta do říše zelí", 128],
    ["Romance na zdymadle", 144],
    ["Zátiší s mimozemšťanem", 135],
    ["Čtyři facky a dortík", 100],
    ["Motorová okurka", 165],
    ["Johnny Noir", 140],
    ["Pražská kavárna vrací úder", 130],
    ["Pět sester ve vratech", 111],
    ["Stařec a krajta", 187],
    ["Růžová nemoc", 210],
    ["Smrt v přímém přenosu", 265],
]

for hra in hry:
    if hra[1] > 120:
        print(hra[0])

for hra in hry:
    hodiny = hra[1] // 60
    minuty = hra[1] % 60
    print(f"Hra {hra[0]} má {hodiny} hod. a {minuty} min.")

"""Napište cyklus, který projde zadaný seznam desetinných čísel a spočítá jejich průměr. Seznam čísel si vytvořte na začátku programu."""

decimal_list = [1.1, 8.7, 4.5, 10.87, 3.58]

dec_sum = 0.0
for dec in decimal_list:
    dec_sum += dec

dec_avg = dec_sum / len(decimal_list)
print(dec_avg)


"Napište cyklus, který projde zadaný seznam celých čísel a najde v něm největší hodnotu."


int_list = [548, -46487, -4588, 1387, 478, 58]

max_int = int()
for int in int_list:
    if int > max_int:
        max_int = int

print(max_int)
