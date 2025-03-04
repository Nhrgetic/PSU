try:
    Ocjena = float(input("Unesite ocjenu u rasponu 0.0 do 1.0: "))
    if 0.0<= Ocjena <= 1.0:

        if float(Ocjena) >= 0.9:
            print("A")

        if float(Ocjena) >= 0.8:
            print("B")

        if float(Ocjena) >= 0.7:
            print("C")

        if float(Ocjena) >= 0.6:
            print("D")

        if float(Ocjena) < 0.6:
            print("F")
    else:
        print("Ocjena nije unutar intervala")

except ValueError:
    print("Unesite broj!")

