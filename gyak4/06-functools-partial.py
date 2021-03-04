import functools


def termek_adatok(kategoria, termek_neve, ar, leiras):
    print("Termék neve:", termek_neve)
    print("Kategória:", kategoria)
    print(f"Ára: {ar} Ft")
    print(leiras)
    print("---")

termek_adatok("Plüss micimackó", "plüss", 1200, "A legjobb plüss Micimackó")

# Partial, első paraméterek megadása
szamitogep_adatok = functools.partial(termek_adatok, "Szamitogep")
szamitogep_adatok("Acer Predator", 250000, "Nagyon komoly gamer laptop, Minecraft 120 fps!!!")

# Partial, az utolsó paraméterek megadása
leiras_nelkuli_termek = functools.partial(termek_adatok, leiras="Nincs leírás")
leiras_nelkuli_termek("plüss", "Malacka plüss", 1000)

# Partial, első és utolsó paraméterek megadása
szamitogep_leiras_nelkuli_termek = functools.partial(termek_adatok, "Szamitogep", leiras="Nincs leírás")
szamitogep_leiras_nelkuli_termek("Acer Predator", 250000)
