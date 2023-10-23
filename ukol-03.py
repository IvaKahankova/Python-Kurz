import json

with open("body.json", "r", encoding="utf-8") as soubor:
    data = json.load(soubor)


prospech = {jmeno: "Pass" if body >= 60 else "Fail" for jmeno, body in data.items()}


with open("prospech.json", "w", encoding="utf-8") as soubor:
    json.dump(prospech, soubor, ensure_ascii=False)

print(prospech)


