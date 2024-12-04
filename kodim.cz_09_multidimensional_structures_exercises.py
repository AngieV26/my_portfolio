vysledky = [
    ["Brunner Radek", [3, 0, 9]],
#                   0
#           00            01
#                    010 011 012 
    ["Urban Jaroslav", [3, 11, 44]], 
    ["Andrle Jakub", [3, 12, 21]], 
    ["Fiala Stanislav", [3, 13, 31]]
]

"""V tabulce jsou 4 bezci (uroven 1). U kazdeho bezce je zapis jeho vysledneho casu ve formatu [h, m, s] (uroven 2). 
A v ramci vnoreneho seznamu se dostaneme teprve na jednotlive hodnoty (uroven 3). Seznam ma tedy vice rozmeru nez tabulka (ta ma 2 urovne) """

vitez = vysledky[0] # takhle seznam zredukujeme o nejvyssi patro, v pormenne je totiz jen jeden zavodnik
cas_viteze = vysledky[0][1] # takhle seznam zredukujeme o dalsi patro
medailiste = vysledky[:3] # v pripade slicingu dojde k zachovani vsech dimenzi, porad mame 3 zavodniky s jejich casy


"""Stříbrná medaile je sice úžasný úspěch, ale kdo by nechtěl vyhrát? Podívejme se, kolik chybělo stříbrnému běžci k vítězství.
Nejprve si vytvoř dvě proměnné, do kterých ulož čas vítěze a čas závodníka se stříbrnou medailí. Oba časy převeď na minuty a ulož jako číslo.
Vypočti rozdíl obou proměnných. Tím zjistíš, kolik minut chybělo stříbrnému závodníku k vítězství."""
cas_viteze = vysledky[0][1]
cas_druheho = vysledky[1][1]
rozdil = []
for x in range (3):
    r = cas_druheho[x] - cas_viteze[x]
    rozdil.append(r)
print(f'Rozdíl v časech prvního a druhého zavodníka je {rozdil[0]} hodin, {rozdil[1]} minut a {rozdil[2]} sekund.')


"""Zadání je podobné jako u předchozího příkladu, ale nyní zkusíme výpočet provést pro všechny závodníky.

Nejprve (pomocí cyklu a metody append()) vytvoř dvourozměrný seznam, kde na nulté pozici vnořeného seznamu je číslo běžce 
a na první pozici je čas běžce v minutách jako desetinné číslo.
Ve druhém kroku (opět pomocí cyklu a metody append()) vytvoř další dvourozměrný seznam, kde na nulté pozici vnořeného seznamu je číslo běžce 
a na první pozici je rozdíl času běžce oproti času vítěze v minutách. Jinak řečeno, bude tam číslo, které udává, o kolik by běžec musel být rychlejší, aby závod vyhrál."""

bezci_min = []
for x in range(len(vysledky)):
    bezec_min = []
    bezec_min.append(vysledky[x][0])
    minuty = round((vysledky[x][1][0] * 60) + vysledky[x][1][1] + (vysledky[x][1][-1] / 60), 2)
    bezec_min.append(minuty)
    bezci_min.append(bezec_min)
print(bezci_min)

bezci_rozdil = []
for x in range(1, 4):
    bezec_rozdil = []
    bezec_rozdil.append(bezci_min[x][0])
    minuty_rozdil = round((bezci_min[x][1] - bezci_min[0][1]), 2)
    bezec_rozdil.append(minuty_rozdil)
    bezci_rozdil.append(bezec_rozdil)
print(bezci_rozdil)