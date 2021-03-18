import collections

# Named tuples
Varazslo = collections.namedtuple("Ember", ['nev', 'haj_szin', 'haj_meret', 'szem_szin'])

harry = Varazslo("Harry Potter", "barna", "rövid", "zöld")
ron = Varazslo("Ron Weasly", "vörös", "rövid", "vörös")
hermione = Varazslo("Hermione Granger", "barna", "hosszú", "barna")

print(harry)
print("név", harry.nev)
print("név", harry[0])
print("harry dict", harry._asdict())
print("---")

print(ron)
ron = ron._replace(szem_szin="barna")
print(ron)
print("---")

malfoy_dict = {'nev': 'Draco Malfoy', 'haj_szin': 'szőke', 'haj_meret': 'rövid', 'szem_szin': 'kék'}
malfoy = Varazslo(**malfoy_dict)
print(malfoy)

piton_list = ["Perselus Piton", "fekete", "félhosszú", "barna"]
piton = Varazslo._make(piton_list)
print(piton)

# Ki kicsoda játék készítése
