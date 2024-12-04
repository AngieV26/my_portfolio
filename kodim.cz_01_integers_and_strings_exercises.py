""" Jeden lístek do divadla "Pěst na oko" stojí 12 euro. Spočítejte měsíční příjem divadla ze vstupného přichází-li průměrně 
174 návštěvnic a návštěvníků na jedno představení a divadlo hraje 15 představení měsíčně. Výsledek vypište na obrazovku. """
print(174 * 12 * 15)
print((174 * 12) * 15)


""" Divadlo se rozhodlo prodávat studentské vstupné ve výši 65% plného vstupného. Jak se změní měsíční příjem divadla pokud víme, 
že polovina návštěvníků jsou studentky a studenti? """
print (12 * 15 * 174 / 2 * 0.65) # destinna cisla se pisi s teckou


""" Vypište řetězec obsahující jméno divadla.
Vypište řetězec obsahující jméno divadla tak, že sečtete dohromady jednotlivá slova toho jména.
Zkuste vynásobit řetězec celým číslem. Jaký jste dostali výsledek?
Vypište řetězec který vypadá takto: '111111000000', ale místo šesti jedniček a šesti nul obsahuje 256 jedniček a 256 nul."""
print("Pěst na oko")
print("Pěst" + " " + "na " + "oko") # mezery muzeme psat samostane i jako soucast jinych retezcu
print(("Pěst na oko" + " ") * 5)
print("1" * 256 + "0" * 256)


""" Takzvané Shannonovo číslo má hodnotu 10^123 a udává kolik nejméně lze odehrát různých šachových partií. 
Vytvořte řetězec, který obsahuje toto číslo zapsané běžným způsobem pomocí cifer. Například 10^3 je 1000, 10^6 je 1000000 atd.
Čísla s mnoha nulami je v Česku zvykem zapisovat tak, že každé tři nuly následuje mezera. 
Jeden milión se tedy zapíše jako 1 000 000. Vytvořte řetězec, který obsahuje Shannonovo číslo z předchozího cvičení zapsané v tomto formátu. """
print("1" + "0" * 123) # 10^2 je 100, 2 nuly, takze 10^123 bude mít 123 nul
print(str(10 ** 123)) # jine reseni
print("1" + " 000" * 41) # tady mocnime tretinovym exponencialem protoze mame misto jedne nuly v retizku nuly 3
