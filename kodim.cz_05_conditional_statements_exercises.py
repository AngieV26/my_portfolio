"""Nechte uživatele zadat svoje uživatelské jméno a poté heslo. Pokud se heslo neshoduje s heslem simsalabim, vypište na výstup: Vstup nepovolen
a zavolejte funkci exit(), aby uživatel neznalý hesla nemohl s programem dál pracovat.

Na konec programu vlož příkaz, který se uživatele zeptá na věk. Pokud je uživatel starší 18 let, vypište na výstup: Smíš vstoupit
Pokud je mladší, vypiš: Vstup povolen od 18 let"""


uzivatelske_jmeno = input("Zadejte své uživatelské jméno: ")
heslo = input("Zadejte své heslo: ")
if heslo != "simsalabim":
    print("Vstup nepovolen")
    exit()
    
vek = int(input("Vyplň svůj věk: "))

if vek >= 18:
    print("Smíš vstoupit")
else:
    print("Vstup povolen od 18 let")


"""A nyní opět pokračujeme v našem rezervačním systému.

Program vstupenky01.py, který jste napsali v předchozí fázi, si uložte jako vstupenky02.py, abychom ho mohli dále rozšířit o výpočet ceny vstupenky.
Jakmile máte v programu načtený věk uživatele, vytvořte si proměnnou plna_cena, do které uložte hodnotu 12.
Vytvořte podmínku, která do proměnné cena uloží cenu spočítanou podle věku uživatele dle následujících pravidel
0 euro pro návštěvníky mladší 6 let,
65% ze základní ceny pro návštěvníky 6 až 26 let (žák, student),
100% ze základní ceny pro návštěvníky 27 až 64 let (dospělý),
50% ze základní ceny pro ostatní (senior).
Nezapomeňte na zaokrouhlování, ať nám cena vyjde v celých centech. Zaokrouhlení na určitý počet desetinných míst se nastavuje druhým nepovinným parametrem funkce round().

Nakonec spočtenou cenu vypište s nějakou hezkou zprávou na výstup."""

print("Divadlo Pěst na oko")
print("Vítejte v online rezervaci vstupenek")
print("Pro vstup do systému je potřeba registrace")

uzivatelske_jmeno = input("Vyplňte své uživatlské jméno: ")
vek_pro_registraci = int(input("Zadejte svůj věk: "))
print(f" Uživatelské jméno: {uzivatelske_jmeno}, {vek_pro_registraci} let")

plna_cena = 12

if vek_pro_registraci < 6:
    cena = 0
elif vek_pro_registraci <= 26:
    cena = plna_cena * 0.65
elif vek_pro_registraci <= 64:
    cena = plna_cena
else:
    cena = plna_cena * 0.5

cena = round(cena, 2)
print(f'Cena vstupenky je {cena} eur.')


"""Založte si program registrace.py. Program nechá uživatele, aby si zvolil uživatelské jméno a heslo. 
Heslo jej nechejte zadat dvakrát a ověřte, že jej uživatel zadal dvakrát stejně. V opačném případě vypište varování, 
že hesla nejsou stejná. Dále ověřte, že heslo je bezpečné, což v tomto případě znamená, že je delší než 8 znaků."""

user_name = input('Zvol si uživatelské jméno: ')
password = input('Zvol si heslo: ')
password_verification = input('Zadej heslo ještě jednou: ')
if password != password_verification:
    print('Zadaná hesla se neshodují!')
else:
    if len(password) > 8:
        print('Heslo je bezpečné.')
    else:
        print('Heslo není bezpečné.')


"""Napište program, který po zadání kalendářního roku vypíše, zda jde o rok přestupný, či nikoliv. 
Letopočet je přestupný, pokud je dělitelný čtyřmi. Roky, které jsou dělitelné 100 jsou ovšem přestupné pouze tehdy, 
jsou-li zároveň dělitelné 400."""

rok = int(input('Zadej kalendářní rok: '))
if rok % 4 == 0 and rok % 100 != 0:
    print('Letopočet', rok, 'je přestupný.')
elif rok % 4 == 0 and rok % 100 == 0 and rok % 400 == 0:    
    print('Letopočet', rok, 'je přestupný.')
else:
    print('Letopočet', rok, 'není přestupný.')
    
# Logicky soucet (or) a logicky soucin (and), soucet je true pokud alespon jedna podminka je true, soucin je true jen pokud jsou vsechny podminky true
# v podminkach overujicich pravdivost (= True, = False), muzeme tuhle cast nekdy uplne vynechat

# soucet:
rain = True
watering_truck = True
if rain or watering_truck:
    wet_street = True
else:
    wet_street = False
print(wet_street)

# soucin:
wet_street = False
go_out = True
if wet_street and go_out:
    wet_shoes = True
else:
    wet_shoes = False
print(wet_shoes)

# kombinace:
rain = True
watering_truck = False
go_out = True
if (rain or watering_truck) and go_out: #prednost se stejne jako v pocitani urcuje zavorkou, jinak ma prednost and pred or
    wet_shoes = True
else:
    wet_shoes = False
print(wet_shoes)


"""Požádejme uživatele, ať zadá celé číslo. Napiš program který zjistí, zda je číslo dělitelné 3 i 4 současně.

Tip: nezapomeňte si zadané číslo převést na int. 
Tip 2: K ověření dělitelnosti použij operátor % - zbytek po celočíselném dělení a zkontroluj, zda je výsledek 0. 
Například 15 % 5 vrací 0, protože 15 je dělitelné 5."""

cislo = int(input('Zadej číslo: '))
if cislo % 3 == 0 and cislo % 4 == 0:
    print(f'Číslo {cislo} je delitelné 3 i 4.')
else:
    print(f'Číslo {cislo} není delitelné 3 a 4 zároveň.')    


"""Matematické gymnázium nabízí aplikaci, která sděluje informaci o povinnosti vykonání přijímací zkoušky. 
Požádejte uživatele o zadání známky z matematiky a průměru všech známek na posledním vysvědčení. 
Pokud má zájemce průměr známek nižší než 1.8 a z matematiky nejhůře dvojku, vypište text: "Přijmeme vás bez přijímací zkoušky.". 
V opačném případě vypište "Musíte splnit přijímací zkoušku."."""

mark = int(input('Zadej známku z matematiky z posledního vysvědčení: '))
avg = list(input('Zadej průměr všech známek na posledním vysvědčení: '))
if avg[1] == ',':
    avg[1] = '.'
else:
    avg = avg
avg = float(''.join(avg))

if avg < 1.8 and mark <= 2:
    print("Přijmeme vás bez přijímací zkoušky.")
else:
    print("Musíte splnit přijímací zkoušku.")


"""Na obrázku vidíte rozložení čísel na klasické Francouzské ruletě. Ruleta obsahuje čísla 0 - 36. 
Každé číslo s výjimkou nuly je buď sudé nebo liché a zároveň červené nebo černé. 
Pro čísla 1 až 10 a 19 až 28 platí, že lichá čísla jsou červená a sudá jsou černá. 
Pro zbytek platí obrácené pravidlo, tedy lichá jsou černá a sudá červená. Nula není ani lichá ani sudá, ani černá ani červená.

Napište program, kterému uživatel zadá číslo a program odpoví, jestli jde o číslo sudé nebo liché, černé nebo červené, 
nebo je to nula."""

number = int(input('Zadej číslo od 0 do 36: '))
if number == 0:
    print(f'Číslo {number} je zlená nula')
elif (number <= 10 or (number >= 19 and number <= 28)) and number % 2 != 0:
    print(f'Číslo {number} je liché a červené')
elif (number <= 10 or (number >= 19 and number <= 28)) and number % 2 == 0:
    print(f'Číslo {number} je sudé a černé')
elif number % 2 != 0:
    print(f'Číslo {number} je liché a černé')
elif number % 2 == 0:
    print(f'Číslo {number} je sudé a červené')


"""Divadlo Pěst na oko pořádá soutěž o lístky na premiéru nového představení Zločin v podmínce. 
Pro účast v soutěži musí zájemce splnit následující dvě podmínky:

Sdílel alespoň 5 příspěvků divadla na sociálních sítích.
Letos navštívil(a) alespoň 5 představení.
Současně platí, že soutěžit můžou všichni členové Klubu přátel Divadla Pěst na oko, i kdyby podmínky nesplnili.

Tvým úkolem je vytvořit program, který se uživatele zeptá na všechny potřebné informace (stačí odpověď ano/ne) 
a vyhodnotí, zda se může zúčastnit soutěže."""

condition_1 = input("Sdílel/a jsi alespoň 5 příspěvků divadla na sociálních sítích? [ano/ne] ")
condition_2 = input("Navštívil/a jsi v letošním roce alespoň 5 představení divadla? [ano/ne] ")
club_membership = input("Jsi členem Klubu přátel divadla Pěst na oko? [ano/ne] ")

if (condition_1 == "ano" and condition_2 =="ano") or club_membership == "ano":
    print(f"Můžeš se soutěže zúčastnit")
else:
    print(f"Nemůžeš se soutěže zúčastnit")