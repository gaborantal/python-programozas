from .random_dolgok import *

random_szerencseszam = random_dolgok.random_szerencseszam_generator

# import * miatt megtehetjük ezt is
random_szerszam = random_szerencseszam_generator

# Így csak a random_dolgok modulból lesz importálva minden.
# Azonban, ha valaki a masik_modul modult importálja csillaggal, az nem nem fogja látni a convert_utils metódusokat.
# A csillaggal való importáláskor, ha létezik az __all__ változó, akkor az itt definiált modulok importálását jelenti majd a * import
# Link: https://docs.python.org/3/tutorial/modules.html#importing-from-a-package

# __all__ = ["random_dolgok", "convert_utils"]
