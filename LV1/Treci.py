brojevi = []

while True:

    unos = input("Unesite broj ili done za kraj zadatka: ")
    if unos.lower() == "done":
        break
    try:
        brojevi.append(int(unos))
    except ValueError:
        print("Unesite broj!")

if brojevi:

    print(f"Broj unesenih od korisnika:  {len(brojevi)}")
    print(f"Srednja vrijednost: {sum(brojevi) / len(brojevi)}")
    print(f"Minimalna vrijednost:{min(brojevi)}")
    print(f"Minimalna vrijednost:{max(brojevi)}")
    print(f"Soritrana lista: {(brojevi)}")
else:
    print("Niste unijeli brojeve!")

