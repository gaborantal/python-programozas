import os
import pathlib

netflix_data_folder = os.path.join("csv_fajlok", "netflix_yearly_data")

p = pathlib.Path(netflix_data_folder)
print("p:", p)
print("abszolút útvonal:", p.absolute())
print("név:", p.name)
print("szülő:", p.parent)
print("nagyszülő:", p.parent.parent)
print("létezik:", p.exists())
print("cwd:", p.cwd())
print("posix:", p.as_posix())
print("uri:", p.absolute().as_uri())

for fajl in p.glob("**/*.csv"):
    print(fajl)
    # összeolvasztás

p = p.parent

foka = p.joinpath("teszt_foka.txt")
print("létezik:", foka.exists())
with foka.open("w") as fp:
    fp.write("Seals can sleep underwater and usually only come on land to escape predators like whales and sharks, as well as to mate, give birth, feed and moult.")
print("létezik:", foka.exists())
# A teljes útvonal megadása szükséges
# foka.rename("foka_teny.txt")

