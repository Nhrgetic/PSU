putanja = r'C:\Users\Nino\Downloads\SMSSpamCollection.txt'

with open(putanja, 'r', encoding='utf-8') as f:
    linije = f.readlines()

#brojanje rijeci
ham_rijeci = []
spam_rijeci = []
spam_usklicnik = 0

for linija in linije:
    if '\t' not in linija:
        continue

    tip, poruka = linija.strip().split('\t', 1)

    # broj rijeci u poruci s razmakom
    broj_rijeci = len(poruka.split())

    if tip == 'ham':
        ham_rijeci.append(broj_rijeci)
    elif tip == 'spam':
        spam_rijeci.append(broj_rijeci)
        if poruka.endswith('!'):
            spam_usklicnik += 1

print(f"Prosječan broj riječi u ham porukama: {sum(ham_rijeci) / len(ham_rijeci):.2f}")
print(f"Prosječan broj riječi u spam porukama: {sum(spam_rijeci) / len(spam_rijeci):.2f}")
print(f"Broj spam poruka koje završavaju uskličnikom: {spam_usklicnik}")
