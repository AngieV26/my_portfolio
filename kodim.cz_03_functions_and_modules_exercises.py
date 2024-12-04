import math
import random

"""Uložte si do proměnné nazev řetězec s názvem "Divadlo Pěst na oko". Pokud použijeme designové písmo nad hlavní vchod budovy, jeden znak (i mezera) bude široký 30 cm. 
Použijte funkci len() abyste zjistili počet znaků v názvu divadla a spočítejte délku nápisu v centimetrech."""

nazev = "Divadlo Pěst na oko"
delka_nazvu = len(nazev)
delka_napisu = delka_nazvu * 30
print(f"{delka_napisu} cm")


"""Divadlo chce mít ceny vstupenek jak v eurech tak v celých korunách. Uložte do proměnné eura cenu studentské vstupenky (65% z 12 euro). 
Použijte funkci round() a do proměnné koruny spočítejte kolik činí studentské vstupné v korunách, jestliže kurz eura je 24 korun."""

studentska_vstupenka_euro = 12 * 0.65
studentksa_vstupenka_koruny = round(studentska_vstupenka_euro * 24)
print(studentska_vstupenka_euro * 24)
print(f"{studentksa_vstupenka_koruny} Kč")


"""Importujte modul math a vyzkoušejte si funkci math.ceil(), která slouží k zaokrouhlování směrem nahoru. 
Proveďte zaokrouhlování z předchozího cvičení na celé koruny směrem nahoru."""

print(f"{math.ceil(studentska_vstupenka_euro * 24)} Kč")

"""Na informačním panelu v předsálí divadla se zobrazují informace o náhodných představeních. 
Pro tento panel potřebujeme generátor náhodných čísel, který bude generovat čísla představení mezi 1 až 24. 
Importujte modul random a použijte funkci randint() pro vygenerování několika náhodných čísel z tohoto rozsahu. Vygenerované číslo vypište na obrazovku."""


cislo_predstaveni = random.randint(1, 24)
print(f"{cislo_predstaveni}")
# pro generovani vice cisel je potreba zkopirovat oba radky, ne jen print
# muzeme pouzit taky cyklus
for i in range(10): 
    # range vraci rozsah od nuly po predposledni cislo, horni hranice je exclusive, prijma 3 argumenty: od(vc), po(bez), po kolika(po jedne, po dvou atp)
    # pokud ma range prvni agrument vyssi nez druhy a posledni argument v zapornem cisle bude odpocitavat, pouzit se da i funkce reversed v obou pripadech bude vyloucena hodnota vice vpravo
    number = random.randint(1, 24)
    print (number)


"""Zkuste vymyslet (za použití funkcí, které už znáte) příkaz, který zaokrouhlí číslo v proměnné cislo na celé číslo klasickým zaokrouhlováním.
Pokud si chcete svoje řešení otestovat, můžete si obsah proměnné cislo vygenerovat náhodně funkcí random.uniform(). 
Ta má stejné vstupy jako funkce random.randint(), generuje ale desetinná čísla."""

zaokrouhlene_cislo = round(3.5)
print(zaokrouhlene_cislo)
zaokrouhlene_cislo = round(2.5)
print(zaokrouhlene_cislo)

cislo = str(random.uniform(0, 10))
print(cislo)
if '.5' in cislo:
    zaokrouhlene_cislo = math.ceil(float(cislo))
else:
    zaokrouhlene_cislo = round(float(cislo))
print(zaokrouhlene_cislo)


# jine reseni
cislo = random.uniform(0, 10)
print(f"Původní číslo: {cislo}")

desetinna_cast = cislo - math.floor(cislo)
print(desetinna_cast)
if desetinna_cast == 0.5:
    zaokrouhlene_cislo = math.ceil(cislo)
else:
    zaokrouhlene_cislo = round(cislo)

print(f"Zaokrouhlené číslo: {zaokrouhlene_cislo}")