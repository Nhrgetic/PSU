# Otvorimo datoteku i pročitajmo njen sadržaj
with open('song.txt', 'r') as file:
    tekst = file.read().lower()  # Pretvaramo tekst u mala slova

# Uklonimo interpunkcijske znakove
tekst = tekst.translate(str.maketrans('', '', '.,!?()[]{}":;'))

# Razbijemo tekst na riječi
rijeci = tekst.split()

# Inicijaliziramo rječnik za brojanje riječi
rjecnik = {}

# Brojimo pojavljivanje svake riječi
for rijec in rijeci:
    if rijec in rjecnik:
        rjecnik[rijec] += 1
    else:
        rjecnik[rijec] = 1

# Pronađemo riječi koje se pojavljuju samo jednom
rijeci_jednom = [rijec for rijec, broj in rjecnik.items() if broj == 1]

# Ispisujemo rezultat
print(f"Broj riječi koje se pojavljuju samo jednom: {len(rijeci_jednom)}")
print("Riječi koje se pojavljuju samo jednom:")
for rijec in rijeci_jednom:
    print(rijec)
