import random


class KoPapirOllo:
    def __init__(self, nev):
        self.valasztas = None
        self.gep = None
        self.nev = nev
        self.gyozelem = 0
        self.vereseg = 0
        self.dontetlen = 0

    def jatszunk_meg(self):
        i = input(f"Játszunk még, {self.nev}? ")
        return i.lower() in ["i", "y", "yes", "igen", "nana"]

    def jatekos_valaszt(self):
        i = input("Mit választasz? (kő/papír/olló) ")
        i = i.lower()
        if i in ["kő", "ko", "k"]:
            return "ko"
        if i in ["papír", "papir", "p"]:
            return "papir"
        if i in ["olló", "ollo", "o"]:
            return "ollo"

    def gep_valaszt(self):
        return random.choice(("ko", "papir", "ollo"))

    def jatek(self):
        self.valasztas = self.jatekos_valaszt()
        self.gep = self.gep_valaszt()
        print(f"A te választásod {self.valasztas}, a gép választása pedig {self.gep}")
        if self.valasztas == self.gep:
            print("Döntetlen, necces volt.")
        if self.valasztas == "ko" and self.gep == "ollo":
            print("Játékos nyert")
        if self.valasztas == "ko" and self.gep == "papir":
            print("Gép nyert")
        if self.valasztas == "papir" and self.gep == "ollo":
            print("Gép nyert")
        if self.valasztas == "papir" and self.gep == "ko":
            print("Játékos nyert")
        if self.valasztas == "ollo":
            if self.gep == "ko":
                print("Gép nyert")
            if self.gep == "papir":
                print("Játékos nyert")

    def statisztika(self):
        print(f"Összes játék: {self.gyozelem + self.vereseg + self.dontetlen}")
        print("Győzelem", self.gyozelem)
        print("Vereség", self.vereseg)
        print("Döntetlen", self.dontetlen)

    def akarmi(self):
        return None

    def akarmi2(self, param):
        print(len(param))
        print(param)
        print(param)
        print(param)


def main():
    print("Üdv a kő-papír-olló játékban.")
    nev = input("Add meg a neved: ")
    game = KoPapirOllo(nev)

    jatek = True
    while jatek:
        game.jatek()
        jatek = game.jatszunk_meg()


if __name__ == '__main__':
    main()
