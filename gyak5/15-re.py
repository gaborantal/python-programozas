import os
import re

# Amire szükség lesz: basic regex ismeretek
# Help: https://regex101.com/

text = """Akkor nem kell!
Akkor nem kell!!!!!
Akkor nem kell!!
Akkor nem kell!!444!4!4!!!!
Akkor nem kell!!444!4!4!4!4!
"""

# Alap keresés regex segítségével
# Flagek:
# re.I == re.IGNORECASE
# re.M == re.MULTILINE
# re.S == re.DOTALL
# re.X == re.VERBOSE
# re.U == re.UNICODE
# re.L == re.LOCALE
# re.DEBUG
match = re.search(r".+!{2,}$", text, flags=re.MULTILINE | re.IGNORECASE)
print(match)
if match:
    print("Van találat!")
    print(match.groups())
match = re.search(r".+!{100,}$", text, flags=re.MULTILINE | re.IGNORECASE)
if match:
    print("Van találat!")

# Kiegészíteni a regexet

# EMAIL_REGEX = re.compile("^\\S+@\\S+\\.\\S+$")
# EMAIL_REGEX = re.compile(r"^\S+@\S+\.\S+$")
EMAIL_REGEX = re.compile(r"\S+@\S+\.\S+$")
CIMEK = ["Alma@kukac.hamm", "jajj@gmail.com", "cica@vagyok.hu", "kutya.vagyok.hu", "nem tudom mi ez @gmail.com",
         "nem értem", "denever@eset.hu", "Asszem valami cipofuzo23@gmail.com"]

print("---")
for email in CIMEK:
    print(email, "valid:", "igen" if EMAIL_REGEX.search(email) else "nem")
print("---")
for email in CIMEK:
    print(email, "valid:", "igen" if EMAIL_REGEX.match(email) else "nem")
print("---")

with open(os.path.join("szoveg", "cirmatlan_cica.txt"), encoding="utf8") as fp:
    cica_mese = fp.read()

# Csak egy találatot ad vissza
print(re.search("tényle{2,}g", cica_mese, flags=re.U | re.I))

for talalat in re.findall("ténylee+g", cica_mese, re.U | re.I):
    print(talalat)

for talalat in re.finditer("ténylee+g", cica_mese, re.U | re.I):
    print("találat", talalat)

print("---")

# re.sub házi feladat

EMAIL_REGEX = re.compile(r"^(\S+)@(\S+)\.(\S+)$")
for email in CIMEK:
    match = EMAIL_REGEX.match(email)
    if match:
        print(match.groups())
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))

