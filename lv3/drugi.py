import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mtcars = pd.read_csv("mtcars.csv")

# 1. Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara.
mpg_means = mtcars.groupby("cyl")["mpg"].mean()
plt.figure(figsize=(8, 5))
plt.bar(mpg_means.index.astype(str), mpg_means.values, color=["blue", "green", "red"])
plt.xlabel("Broj cilindara")
plt.ylabel("Prosjecna potrosnja (mpg)")
plt.title("Potrosnja automobila s 4, 6 i 8 cilindara")
plt.show()

# 2. Pomoću boxplot-a prikažite na istoj slici distribuciju težine automobila s 4, 6 i 8 cilindara.
plt.figure(figsize=(8, 5))
mtcars.boxplot(column="wt", by="cyl", grid=False)
plt.xlabel("Broj cilindara")
plt.ylabel("Tezina (1000 lbs)")
plt.title("Distribucija tezine automobila")
plt.suptitle("")  # Uklanjanje autom. podnaslova
plt.show()

# 3. Pomoću odgovarajućeg grafa pokušajte odgovoriti na pitanje imaju li automobili s ručnim mjenjačem veću potrošnju od automobila s automatskim mjenjačem?
mpg_transmission = mtcars.groupby("am")["mpg"].mean()
plt.figure(figsize=(8, 5))
plt.bar(["Automatski", "Rucni"], mpg_transmission.values, color=["orange", "purple"])
plt.xlabel("Tip mjenjaca")
plt.ylabel("Prosjecna potrosnja (mpg)")
plt.title("Povezanost mjenjaca i potrosnje")
plt.show()

# 4. Prikažite na istoj slici odnos ubrzanja i snage automobila za automobile s ručnim odnosno automatskim mjenjačem
plt.figure(figsize=(8, 5))
manual = mtcars[mtcars["am"] == 1]
auto = mtcars[mtcars["am"] == 0]
plt.scatter(manual["hp"], manual["qsec"], color="purple", label="Rucni")
plt.scatter(auto["hp"], auto["qsec"], color="orange", label="Automatski")
plt.xlabel("Snaga (hp)")
plt.ylabel("Ubrzanje (qsec)")
plt.title("Odnos ubrzanja i snage automobila")
plt.legend()
plt.show()
