import math
import statistics

"""Uložte si do proměnné jmeno svoje jméno. Pomocí volání vhodných metod jej převeďte nejdříve na malá písmena a poté na velká písmena."""
jmeno = "Kdovík"
jmeno = jmeno.lower()
print(jmeno)
jmeno = jmeno.upper()
print(jmeno)


"""Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto: hodnoty = ['12', '1', '11', '-11']"""
hodnoty = ['12', '1', '7', '-11']
cislo = int(hodnoty[2]) # 3. cislo stringu na int
vysledek = cislo + 4
hodnoty[2] = str(vysledek) # vysledek souctu vracim na 3. pozici seznamu jako str
print(hodnoty) # tisknu nove honoty


"""K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal takto hodnoty = '12.1 1.68 7.45 -11.26'
Určitě se vám budou hodit metody split a join."""

hodnoty = '12.1 1.68 7.45 -11.51'
hodnoty_solo = hodnoty.split(' ')
print(hodnoty_solo) # splitnutim retezce vznikne list
posledni_cislo = float(hodnoty_solo[-1])
vysledek_2 = posledni_cislo + 0.25 # nebo posledni_cislo += 0.25
hodnoty_solo[-1] = str(vysledek_2)
print(hodnoty_solo)
hodnoty = ' '.join(hodnoty_solo) # do joinu pisu znak, kterym se mi maji polozky v listu spojit
print(hodnoty)


"""Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto číslo zaokrouhlené nejdříve nahoru, 
potom dolů a potom běžným Pythonovským zaokrouhlováním."""

decimal_input = input("Zadej desetinné číslo: ")
decimal = float(decimal_input.replace(",", "."))
print(math.ceil(decimal))  # 4
print(math.floor(decimal))  # 3
print(round(decimal))


"""Uvažujme vysvědčení studenta, které máme uložené jako seznam.
Uvažuj, že student se hlásí na školu, která vybírá studenty podle průměru. Pro školu jsou ale důležité pouze předměty český jazyk, anglický jazyk, matematika a fyzika. 
Vypočítej průměr studenta z daných předmětů s využitím modulu statistics. 
Na začátku vytvoř prázdný seznam a následně pomocí cyklu vlož do nového seznamu známky ze čtyř vyjmenovaných předmětů. Nakonec použij metodu statistics.mean() k výpočtu průměru. 
Dále zkus využít funkce, které jsou zmíněné v textu, k výpočtu nejlepší a nejhorší známky z daných předmětů."""

school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]
marks = []
for mark in school_report:
    if mark[0] in ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]:
        marks.append(mark[1])
print(marks)
print(statistics.mean(marks))
print(f"Nejhorší známka {max(marks)}")
print(f"Nejlepší známka {min(marks)}")


"""Ve statistice existuje ukazatel zvaný modus, který vrátí nejčastější hodnotu v datech. V modulu statistics existuje funkce mode(), která umí modus spočítat. 
Funkce mode() má navíc vychytávku, umí pracovat i s řetězci. 
Uvažuj data v seznamu votes, což je hlasování zaměstnanců malé firmy o tom, jakou akci podniknou během jejich vánočního večírku. 
Použij funkce mode() ke zjištění, pro jakou aktivitu hlasovalo nejvíce zaměstnanců. Funkce má jeden parametr - seznam, ze kterého má určit nejčastější prvek."""

votes = [
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
    ]
print(statistics.mode(votes)) # v pripade, ze je v seznamu ve stejnem zastoupeni dve a vice polozek, statistics.mode vybere prvni z nich


"""Níže máš seznam akcí, které se konaly v zasedačce jedné firmy. 
Napiš program, který zjistí následující:
Kolik se uskutečnilo pohovorů?
V jakých jazycích se mohou zaměstnanci firmy vzdělávat?
Při řešení můžeš využít operátor in a slicing, případně metodu split()"""

akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]
pohovor = 0
for a in akce:
    if "pohovor" in a:
        pohovor += 1
print(f"Počet pohovorů v dany den je {pohovor}")

jazykovy_kurz = []
for b in akce:
    if "jazykový kurz" in b:
        kurz = b.split(" - ")
        if kurz[1] not in jazykovy_kurz:
            jazykovy_kurz.append(kurz[1])
print(f"Frima nabizi jazykove kurzy: {", ".join(jazykovy_kurz)}")