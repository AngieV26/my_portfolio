"""Vypište v pořadí třetí pohyb z uvedeného seznamu.
Vypište všechny pohyby kromě prvních dvou.
Vypište kolik je všech pohybů dohromady.
Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný."""

pohyby = [1200, -250, -800, 540, 721, -613, -222]

print(pohyby[2])
print(pohyby[2:])
print(len(pohyby))
print(min(pohyby))
print(max(pohyby))
print(sum(pohyby))

"""Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. Otestujte jej na seznamech různých délek."""

s = [0, 2, 4, 6]
v = sum(s) / len(s)
print(v)

"""Postupujte obdobně jako v úložce Průměr, ale tentokrát sestavte výraz pro výpočet rozpětí, 
tedy rozdílu mezi minimální a maximální hodnotou."""

v = max(s) - min(s) #pokud ma byt rozptyl vzdy kladny muzeme ho zabalit do abs() funkce v = abs(max(s) - min(s))
print(v)

"""Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. 
V takovém případě vyberte jako střed číslo blíže ke konci seznamu."""

seznam = [1200, -250, -800, 721, -613, -222, 15, 84]
#           0     1     2    3     4     5    6   7
middle = len(seznam) // 2
print(seznam[middle]) # vytiskni jako vysledek hodnotu listu seznam, jejiz index se rovna hodnote promenne middle


"""Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu."""

seznam = [1200, -250, -800, 721, -613, -222, 15, 84]
middle = (len(seznam) - 1) // 2 
print(seznam[middle]) 

"""Máme data o písemce, která obsahovala 4 otázky. Za každou otázku mohl student (studentka) získat max. 10 bodů. 
Výsledky studentů jsou v následující tabulce."""

"""Student	Otázka 1	Otázka 2	Otázka 3	Otázka 4
A	9	7	8	5
B	5	3	6	6
C	8	4	9	7
D	8	5	4	8
E	10	6	10	7
Ulož si známky studentů do dvourozměrného seznamu."""

seznam = [
          [9, 7, 8, 5],
          [5, 3, 6, 6],
          [8, 4, 9, 7],
          [8, 5, 4, 8],
          [10, 6, 10, 7]
    ]

"""Spočítej známku jednotlivých studentů. Známku urči podle celkového počtu bodů ze všech příkladů. Bodovací tabulku najdeš níže."""
seznam_studentu = ['A', 'B', 'C', 'D', 'E']
for body in seznam:
    pocet_bodu = sum(body[0:4]) # tady by indexace asi ani nebyla treba
    if pocet_bodu >= 36:
        znamka = 1
    elif pocet_bodu >= 32:
        znamka = 2
    elif pocet_bodu >= 26:
        znamka = 3
    elif pocet_bodu >= 20:
        znamka = 4
    else:
        znamka = 5
    print(znamka)

"""Body	Známka
36 a více	1
32 a více	2
26 a více	3
20 a více	4
méně než 20	5

Vypočítej průměrné body z jednotlivých otázek. Ze které otázky dostali studenti v průměru nejvíce bodů? A ze které naopak nejméně?"""

seznam = [
          [9, 7, 8, 5],
          [5, 3, 6, 6],
          [8, 4, 9, 7],
          [8, 5, 4, 8],
          [10, 6, 10, 7]
    ]    

otazka_1 = 0
otazka_2 = 0
otazka_3 = 0
otazka_4 = 0
for a, b, c, d in seznam:
    otazka_1 += a
    otazka_2 += b
    otazka_3 += c
    otazka_4 += d

otazky = [otazka_1, otazka_2, otazka_3, otazka_4]
for promenna in otazky:
    prumer = promenna / len(seznam)
    print(prumer)

seznam = [
          [9, 7, 8, 5],
          [5, 3, 6, 6],
          [8, 4, 9, 7],
          [8, 5, 4, 8],
          [10, 6, 10, 7]
    ]
otazecky = []
for x in range(4):
    sloupecek = []
    for y in range(5):
        sloupecek.append(seznam[y][x])
    print(f'Průměr bodů z otázky {x + 1} je : {sum(sloupecek) / (len(sloupecek))}')

print(f'Průměr bodů z otázky {x + 1} je : {sum(sloupecek) / (len(sloupecek))}')



"""Následující tabulka obsahuje průměrné roční teploty v České republice za roky 2001 až 2010 (zdroj: Český hydrometeorologický ústav).

rok	teplota °C
2001	7.8
2002	8.7
2003	8.2
2004	7.8
2005	7.7
2006	8.2
2007	9.1
2008	8.9
2009	8.4
2010	7.2
Vytvořte reprezentaci této tabulky pomocí seznamu seznamů. Zde existují dvě možnosti. Nejprve vytvořte seznam, který obsahuje řádky tabulky jako dvouprvkové seznamy 
a uložte jej do proměnné radky. Poté vytvořte seznam, který obsahuje sloupce tabulky, tedy dva seznamy po deseti prvcích. Uložte jej do proměnné sloupce.

Pro obě tyto reprezentace vyřešte následující úkoly

Získejte teplotu na třetím řádku tabulky.
Získejte rok na pátém řádku tabulky.
Získejte poslední řádek tabulky jako seznam.
Vytvořte tabulku bez prvních dvou řádků.
Vytvořte tabulku pouze z prvních dvou řádků.
Vytvořte tabulku obsahující jen řádky 5, 6, 7, 8 (myšleno při "lidském" číslování, tj. od 1).
Použitím proměnné sloupce vypište seznam teplot seřazený vzestupně podle velikosti. Šlo by to i pomocí proměnné radky, ale to ještě neumíme."""

seznam_radky = [
    [2001,	7.8],
    [2002,	8.7],
    [2003,	8.2],
    [2004,	7.8],
    [2005,	7.7],
    [2006,	8.2],
    [2007,	9.1],
    [2008,	8.9],
    [2009,	8.4],
    [2010,	7.2],
]
print(seznam_radky[2][1])
print(seznam_radky[4][0])
print(seznam_radky[9])
print(seznam_radky[2:])
print(seznam_radky[:2])
print(seznam_radky[4:8])