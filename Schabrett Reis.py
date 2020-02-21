summe = 0
for feld in range(64):
    reiskorn = 2**feld
    summe = summe + reiskorn
    print("feld {}. = {:>30,} Reiskörne und damint insgesammt {:>30,} Reiskörner" \
        .format(feld+1,reiskorn,summe))
gewicht = summe * 0.02 /1000 /1000
print()

print("Wenn ein Reiskorn 0,02 Gramm wiegt, wiegen die gesamten")
print("Reiskörner {:,.0f} Tonnen".format(gewicht))