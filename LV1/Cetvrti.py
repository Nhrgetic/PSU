def calculate_spam_confidence(mbox):
    try:
        with open(mbox, 'r') as file:
            total_confidence = 0
            count = 0
            
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    try:
                        confidence_value = float(line.split(':')[1].strip())
                        total_confidence += confidence_value
                        count += 1
                    except ValueError:
                        continue
            
            if count == 0:
                print("Nema pronađenih linija sa 'X-DSPAM-Confidence'.")
                return
            
            average_confidence = total_confidence / count
            print(f"Average X-DSPAM-Confidence: {average_confidence}")
    
    except FileNotFoundError:
        print("Greška: Datoteka nije pronađena.")
    except Exception as e:
        print(f"Došlo je do pogreške: {e}")


# Glavni dio programa
datoteka = input("Ime datoteke: ")
calculate_spam_confidence(datoteka)