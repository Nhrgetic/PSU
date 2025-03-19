import pandas as pd
import numpy as np

mtcars = pd.read_csv("mtcars.csv")

# 1. Kojih 5 automobila ima najveću potrošnju? (mpg - miles per gallon, manja vrednost znači veću potrošnju)
potrosnja = mtcars.sort_values(by="mpg")
print("Pet automobila sa najvecom potrosnjom:")
print(potrosnja[["car","mpg"]].head(5))

# 2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
cyl_8_potrosnja = mtcars[mtcars["cyl"] == 8].sort_values(by="mpg", ascending=False)
print("\nTri automobila sa 8 cilindara i najmanjom potrosnjom:")
print(cyl_8_potrosnja[["car","mpg"]].tail(3))

# 3. Kolika je srednja potrošnja automobila sa 6 cilindara?
srednja_potrosnja_6_cyl = mtcars[mtcars["cyl"] == 6]["mpg"].mean()
print("\n")
print(f"Srednja potrosnja automobila sa 6 cilindara: {srednja_potrosnja_6_cyl:.2f} mpg")

# 4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
srednja_potrosnja_4_cyl = mtcars[(mtcars["cyl"] == 4) & (mtcars["wt"] * 1000 >= 2000) & (mtcars["wt"] * 1000 <= 2200)]["mpg"].mean()
print(f"\nSrednja potrosnja automobila s 4 cilindra i tezinom izmedu 2000 i 2200 lbs: {srednja_potrosnja_4_cyl:.2f} mpg")

# 5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem?
rucni = (mtcars["am"] == 1).sum()
automatik = (mtcars["am"] == 0).sum()
print(f"\nAutomobila s rucnim mjenjacem: {rucni}, automatskim: {automatik}")

# 6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
sto_konja = mtcars[(mtcars["am"] == 0) & (mtcars["hp"] > 100)].shape[0]
print(f"\nBroj automobila s automatskim mjenjacem i snagom preko 100 KS: {sto_konja}")

# 7. Kolika je masa svakog automobila u kilogramima? (1 wt jedinica = 1000 lbs, 1 lb ≈ 0.453592 kg)
mtcars["wt_kg"] = mtcars["wt"] * 1000 * 0.453592
print("\nMasa automobila u kilogramima:")
print(mtcars[["car","wt", "wt_kg"]])