import dataclasses
import random

# Python 3.7 óta
@dataclasses.dataclass()
class Varazslo:
    nev: str
    haj_szin: str
    haj_meret: str
    szem_szin: str

    def __str__(self):
        return f"Varazslo(nev={self.nev}, haj_szin={self.haj_szin}, haj_meret={self.haj_meret}, szem_szin={self.szem_szin}"

    def varazsol(self):
        if "Ron" in self.nev:
            return "Leviossz" + ("á" * random.randint(6, 15))
        return "Leviósza"


if __name__ == '__main__':
    harry = Varazslo("Harry Potter", "barna", "rövid", "zöld")
    ron = Varazslo("Ron Weasly", "vörös", "rövid", "vörös")
    hermione = Varazslo("Hermione Granger", "barna", "hosszú", "barna")

    print(ron.varazsol())
    print(hermione.varazsol())
