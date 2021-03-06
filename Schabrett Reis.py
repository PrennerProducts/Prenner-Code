import matplotlib.pyplot as plt

summe = 0
feldliste = []

for feld in range(64):
    reiskorn = 2**feld
    feldliste.append(reiskorn)
    summe += reiskorn
    print(f"Feld {feld+1}. = {reiskorn:>30,} Reiskörner und damint insgesammt" 
         f"{summe:>30,} Reiskörner")
    
gewicht = summe * 0.02 /1000 /1000

print()
print("Wenn ein Reiskorn 0,02 Gramm wiegt, wiegen die gesamten"
f" Reiskörner {gewicht:,.0f} Tonnen")
plt.plot(feldliste)
plt.show()