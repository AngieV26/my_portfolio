"""Nastudujte si na České Wikipedii jak se převádějí stupně Fahrenheita na stupně Celsia a napište program, který takový převod provede. 
Váš program se zeptá uživatele na teplotu ve stupních Fahrenheita a vypíše její ekvivalent ve stupních Celsia."""
# referencni hodnoty upraveny na 32 °F pro bod mrazu vody a 212 °F bod varu vody
# jeden stupen na Fahrenheitove teplotni skale lze odecist jako 5/9

stupne_f = int(input("Napiš teplotu v °F: "))
stupne_c = 5 * (stupne_f - 32) // 9
print(f"{stupne_f} °F je {stupne_c} °C")


"""Napiš kód, který zpracuje seznam čísel a vypíše jejich součet (bez použití funkce sum())."""
les = [4, 23, 9, 0] # les je ohraniceny soubor entit

kosik = 0 #do kosiku vkládáme houby a neseme je z lesa

for houba in les: #jednu houbu po druhe nachazim a vkladam ji do kosiku
    kosik += houba
print(kosik)

# les = [4, 23, 9, "b", 0, "a"] s timhle python uz pocitat nemuze, programator musi mit jisotu ze datove typy v seznamu koresponduji s funkcemi, ktere pouzivame


"""Napiš kód, který zpracuje seznam čísel a vypíše největší prvek v tomto seznamu (bez použití funkce max())."""

seznam = [4, 2, 15, 10, 458]

nejvetsi = seznam[0]

for cislo in seznam: # pro kazde cislo v seznamu
    if cislo > nejvetsi: # porovnej cislo s nejvetsim
        nejvetsi = cislo # pokud je cislo vetsi nez nejvetsi, nehrad nejvetsi za toto cislo
print(nejvetsi)


"""Napiš kód, který zpracuje seznam čísel a vypíše pouze sudá čísla z tohoto seznamu."""

seznam_1 = [-4, 2, 15, 10, 458]
sude_cislo = []

for cislo_1 in seznam_1:
    if cislo_1 % 2 == 0:
        sude_cislo.append(cislo_1)
print(f"sude cislo: {sude_cislo}")


"""Napiš kód, který zpracuje seznam čísel a vytvoří nový seznam se sudými čísly a nový seznam s lichými čísly z původního seznamu."""
puvodni_seznam = [-10, 159, 58, 47, 51, 154, 85, 10]
sude_cislo_2 = []
liche_cislo_2 = []
for cislo_2 in puvodni_seznam:
    if cislo_2 % 2 == 0:
        sude_cislo_2.append(cislo_2)
    else:
       liche_cislo_2.append(cislo_2)
print(f"suda cisla: {sude_cislo_2}")
print(f"licha cisla: {liche_cislo_2}")


"""Napiš kód, který zpracuje seznam a vytvoří nový seznam bez duplikátů. Výsledné pořadí prvků musí být zachováno."""
seznam_duplicity = [-10, 2, 159, 58, 10, 159, 87, 47, 51, 154, 2, 85, 10]

seznam_bez_duplicit = []
for cislo_3 in seznam_duplicity:
    if cislo_3 not in seznam_bez_duplicit:
        seznam_bez_duplicit.append(cislo_3)
print(seznam_bez_duplicit) # kdybychom chtely mit seznam serazeny pouzijeme print(sorted(seznam_bez_duplicit)) nebo print(sorted(seznam_bez_duplicit, reverse=True)) --> desc


"""V následujícím seznamu máš seznam rodných čísel pacientů, kteří navštívili v jeden konkrétní den lékařskou ordinaci.

Kolik přišlo mužů a kolik žen?
Kdy se narodil nejstarší a kdy nejmladší pacient?
Pokud nevíš, jak funguje rodné číslo, vysvětlení je níže:

Rodné číslo je identifikační číslo, které slouží k jednoznačné identifikaci osoby. V České republice se rodné číslo skládá z 10 číslic a jednoho lomítka, 
které ho rozděluje na části.

Prvních 6 číslic udává datum narození v pořadí rok (2 číslice), měsíc (2 číslice) a den (2 číslice). 
Například pro narození 2. února 1990 by prvních 6 číslic mělo být 900202. Zbytek rodného čísla (tj. část za lomítkem) slouží k identifikaci konkrétní osoby.
Ženy mají k číslu měsíce přičteno 50, např. 845128/6219 je číslo patřící ženě."""

rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081"
]
rok = []
for rodne_cislo in rodna_cisla:
    rok.append(rodne_cislo[0:2])

print(f'Nejstarší člověk se narodil v roce 19{min(rok)} a nejmladší 19{max(rok)}.')

zeny = 0
for mesic_cislo in rodna_cisla:
    if int(mesic_cislo[2:4]) > 50:
        zeny += 1

print(f'Přišla {zeny} žena a {len(rodna_cisla) - zeny} mužů.')