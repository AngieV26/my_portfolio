
"""Náš vůbec první program nebude dělat nic víc, než vypisovat text na obrazovku.

Založte si program vstup-vystup.py. V tomto programu pomocí funkce print() vypište na obrazovku Divadlo Pěst na oko. Program spusťte a vyzkoušejte, že dělá co má.
Upravte tento program tak, že do proměnné nazev uložíte název nějakého divadelního představení a do proměnné cas uložte čas konání tohoto představení. 
Nyní pomocí funkce print() nechte program vypsat na obrazovku na jeden řádek název představení a čas konání, např. Zkrocení zlé ženy - 19:30.
Upravte dále program tak, že do proměnné hodina uložíte hodinu konání představení (jako celé číslo) a do proměnné minuta minutu konání, také jako celé číslo. 
Zařiďte, aby výstup programu vypadal takto: Zkrocení zlé ženy - 19:30."""

print("Divadlo Pěst na oko")
nazev = "Facka"
cas = "18:30"
print(f"{nazev} - {cas}") # pripadne jako print(nazev + "-" + cas)

hodina = 18
minuta = 30

print(f"{nazev} - {str(hodina)}:{str(minuta)}")
print(f"{nazev} - {(hodina)}:{(minuta)}")


"""Teď už budeme chtít, aby náš program dokázal získat vstup od uživatele.

Napište program jmeno.py, který získá jméno a příjmení od uživatele voláním funkce input(). Vypište je na obrazovku podobně jako v předchozím cvičení.
Nechte uživatele zadat také věk. Pozor na to, že funkce input() vždy vrací řetězec, ale my chceme v proměnné vek mít číslo. 
Použijte tedy funkci int(), abyste převedli uživatelem zadaný řetězec na číslo. Opět vypište na obrazovku jméno, příjmení a věk tak jako v předchozí verzi."""

jmeno_prijmeni = input("Zadejte své jméno a příjmení: ")
print(jmeno_prijmeni)

vek = int(input("Zadejte svůj věk: ")) #p repis promenne na jiny typ vek = int(vek) je bezna praxe, je vhodne to ovsem zakomentovat

print('Jméno a příjmení', jmeno_prijmeni, 'Věk:', vek)
print(f"Jméno a příjmení: {jmeno_prijmeni}, Věk: {vek} let")


"""Divadlo požaduje systém pro online rezervaci vstupenek na pořádaná představení. Váš první úkol na této zakázce je vytvořit registraci pro nové uživatele tohoto systému.

Založte si program vstupenky01.py. Bude to první verze našeho programu pro nákup vstupenek.
Napište program tak, aby nejprve vypsal na obrazovku Divadlo Pěst na oko na první řádek, na druhý řádek chceme vypsat Vítejte v online rezervaci vstupenek 
a na třetí řádek Pro vstup do systému je potřeba registrace.
Na dalším řádku požádejte uživatele o jeho uživatelské jméno a poté o jeho věk. Ten si uložte do nějaké proměnné jako číslo."""

print("Divadlo Pěst na oko")
print("Vítejte v online rezervaci vstupenek")
print("Pro vstup do systému je potřeba registrace")

uzivatelske_jmeno = input("Vyplňte své uživatlské jméno: ")
vek_pro_registraci = int(input("Zadejte svůj věk: "))
print(f" Uživatelské jméno: {uzivatelske_jmeno}, {vek_pro_registraci} let")


"""Napište program kostky.py, který bude simulovat hod dvěma klasickými šestistěnnými kostkami. Jeho výstup bude součet bodů na těchto dvou kostkách.

Nápověda: Generování náhodných čísel dělá funkce random.randint().
Pokud chcete ve vašem programu použít modul random, musíte na jeho úplném začátku napsat příkaz"""

import random
kostka_1 = random.randint(1, 6)
kostka_2 = random.randint(1, 6)

print(kostka_1 + kostka_2)

hod = random.randint(1, 6) + random.randint(1, 6)
print(hod)


"""Napište program generator.py, který si od uživatele vyžádá dvě celá čísla - dolní mez a horní mez - a vypíše na výstup náhodné číslo v zadaných mezích."""
prvni_cislo = int(input("Zadej minimum: "))
druhe_cislo = int(input("Zadej maximum: "))
print(f"Náhodné čílso mezi {prvni_cislo} a {druhe_cislo} je {random.randint(prvni_cislo, druhe_cislo)}")

# moznosti jak zapsat vystup je mimo f-string mnoho
cena = 150
print("Cena je", cena, "Kč.")
print("Cena je", cena, "Kč.", sep="**") # vstup sep je argumentem funkce print a dovoluje nam si definovat oddeleni entit jinak nez jako mezeru, ktera je v zapise s carkou jako default
# print("Cena je ", cena, " Kč.", sep="") tohle mezeru rusi a musim ji pak pripsat k retezcum

# volitelnym argumentem funkce print() je taky end, kterym se nastavuje, jak se ma vypis funkci print() ukoncit
# deafultne je to znak nového radku end='\n', ale toto chovani muzeme upravit, aby nam napriklad slo vypsat vice volani funkce print() na jeden radek

print("hurá", end="! ")
print("hurá", end="! ")
print("hurá", end="! ")
print()
# Tento program vypise vse na jeden radek. Prazdny print() vypise sve vychozi ukonceni, tj. novy radek.

# v neposledni rade muzeme hodnoty promenne prevest na string a pouzit +
print("Cena je " + str(cena) + " Kč")
cena = str(cena)
print("Cena je " + cena + " Kč.")