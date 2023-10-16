sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadejte kód součástky: ")
mnozstvi_poptavky = int(input("Zadejte  množství: "))

if kod_soucastky not in sklad:
    print("Součástka není skladem.")
elif sklad[kod_soucastky] < mnozstvi_poptavky:
    print("Lze prodat pouze omezené množství kusů.")
    del sklad[kod_soucastky]
else:
    print("Poptávku lze uspokojit v plné výši.")
    sklad[kod_soucastky] -= mnozstvi_poptavky

print("Aktuální stav skladu:")
for k, v in sklad.items():
    print(f"{k}: {v}")