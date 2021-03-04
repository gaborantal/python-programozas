from masik_almodul import *

# string_to_number nem letezik, mivel a csillag import nem tudja, hogy mit kell importalnia
# Ezt megoldhatjuk, ha az almodulban az __all__ valtozot letrehozzuk, es az importalhato modulokat felvesszuk.

print(convert_utils.string_to_number("aaabbbcccddd", "abcd"))
