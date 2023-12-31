class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def get_info(self):
        return f"Auto - Registrační značka: {self.registracni_znacka}, Typ: {self.typ_vozidla}"


auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

# Dotaz na uživatele
zadana_znacka = input("Zadej značku vozidla (Peugeot nebo Škoda): ")


if zadana_znacka.lower() == "peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif zadana_znacka.lower() == "škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
else:
    print("Neplatná značka vozidla.")