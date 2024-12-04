""" Do proměnné a uložte libovolné celé číslo, do proměnné b uložte libovolné desetinné číslo. 
V následujících úlohách každý výsledek uložte do nové proměnné.
Vypočítejte součet a a b.
Vypočítejte součin a a b.
Vypočítejte zbytek po dělení čísla a číslem b.
Celočíselně vydělte číslo a číslem b."""

a = 10
b = 0.5

soucet = a + b
soucin = a * b
zbytek_po_deleni = a % b
deleni = a // b

print(soucet)
print(soucin)
print(zbytek_po_deleni)
print(deleni)


""" Antikvariát Poslední strana nabízí veškeré své tituly za 50 kč.

Uložte název antikvariátu do libovolné proměnné.
Cenu za jeden titul uložte do proměnné cena_za_kus.
Antikvariát má dnes speciální akci, -30% na všechny dostupné tituly! Slevu uložte do proměnné sleva jako desetinné číslo.
Znovu vypočtěte cenu za kus na základě této slevy."""

jmeno_antikvariatu = "Poslední strana"
cena_za_kus = 50
sleva = 0.3
cena_po_sleve = cena_za_kus * (1 - sleva)

print(cena_po_sleve)
print (f"Cena za kus po slevě: {cena_po_sleve} Kč")


""" Karolína bude mít za půl roku svatbu a právě obdržela od agentury ceník služeb. 
Cena za kompletní menu pro dospělou osobu je 990 Kč, pro dítě je to 50 % ceny dospělého.

Uložte cenu za dospělou osobu do proměnné cena_dospely.
Pomocí proměnné cena_dospely vypočítejte cenu za dítě, tu uložte do proměnné cena_dite.
Vypočítejte celkové náklady na jídlo pro 60 dospělých a 8 dětí. Pro výpočet použijte předchozí proměnné.
V ceníku byla chyba, cena za dospělého je ve skutečnosti 1000 Kč. Upravte na základě této informace všechny proměnné."""

menu_dospely = 1000 # oprava hodnoty z 990 na 1000
menu_dite = menu_dospely * 0.5
celkem = menu_dospely * 60 + menu_dite * 8
print (f"{celkem} Kč")


"""Dbejte na to, aby proměnné měly vhodný název dobře naznačující, co je v které z nich uloženo.

Uložte do proměnné velikost_souboru celočíselnou hodnotu udávající počet herců a hereček, kteří hrají v divadle. 
Do proměnné platy spočítejte celkové náklady divadla na platy, víme-li, že průměrný plat v divadle je 22 392 Kč.
Do jiné proměnné s vhodným názvem uložte nějaké desetinné číslo, například velikost slevy na studentské vstupné. 
Do další proměnné uložte nějaký řetězec, například název nějakého představení.
Zatímco jste dělali předchozí cvičení, do divadla přibyli dva noví lidé. Aktualizujte tedy obsah proměnné velikost_souboru a zařiďte, 
aby v proměnné platy byla správná hodnota nákladů."""

velikost_souboru = 24
platy = 22392 * velikost_souboru
studentska_sleva = 0.25
nejnastevovanejsi_predstaveni = "Zkocení zlé ženy"

velikost_souboru_nova = 26
platy = 22392 * velikost_souboru_nova


"""Zaexperimentujte s operátory celočíselného dělení a dělení se zbytkem.

Kolikrát se vejde číslo 72 do 1024? Kolik je zbytek po dělení čísla 1024 číslem 72?
Divadlo má délky představení vždy uloženo v minutách. Například extrémně nudné a zničující představení 
"Smrt v přímém přenosu" trvá 265 minut. Uložte tuto hodnotu do proměnné delka.
Použijte proměnnou delka a spočítejte trvání představení vyjádřeno v hodinách a minutách. 
Do proměnné hodin uložte počet celých hodin a do proměnné minut uložte zbylé minuty."""

print(1024 // 72)
print(1024 % 72)
delka = 265
hodin = (delka // 60)
minut = (delka % 60)
print(f"Delka predstaveni je {hodin} hodiny a {minut} minut")


"""Hlavní sál divadla má k dispozici 350 sedaček. Lze je poskládat do řad po 32 sedadlech tak, aby všechny řady byly úplné? 
Pokud ne, kolik sedaček musíme přikoupit, aby to šlo? Kolik nám takto vznikne celkem řad?"""

sedacky = 350
rada = 32
print(sedacky // rada)
print(sedacky % rada)
#musime prikoupit 2 sedacky a vznikne 11 rad
print(352 // rada)
print(352 % rada)
