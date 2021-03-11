import csv
import os

with open(os.path.join("csv_fajlok", "kesesek.csv"), encoding="utf8") as fp:
    csv_reader = csv.reader(fp, delimiter=",")
    for row in csv_reader:
        print([r.strip() for r in row])

# Normálisabb CSV olvasó
with open(os.path.join("csv_fajlok", "kesesek.csv"), encoding="utf8") as fp:
    csv_reader = csv.DictReader(fp, delimiter=",")
    for row in csv_reader:
        print(row)

with open('kutyak.csv', mode='w') as kutya_adatok:
    kutya_writer = csv.writer(kutya_adatok, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    kutya_writer.writerow(['Bloki', 'labrador', 'fekete', 'soha'])
    kutya_writer.writerow(['Cukika', 'palotapincsi', 'feher', 'nyaron'])

with open('kutyak_jobb.csv', mode='w') as kutya_adatok:
    fieldnames = ['nev', 'fajta', 'szine', 'szor_hullas']

    kutya_writer = csv.DictWriter(kutya_adatok, fieldnames=fieldnames, lineterminator="\n")

    kutya_writer.writeheader()
    kutya_writer.writerow({'nev': 'Bloki', 'fajta': 'labrador', 'szine': 'fekete', 'szor_hullas': 'soha'})
    kutya_writer.writerow({'nev': 'Cukika', 'fajta': 'palotapincsi', 'szine': 'feher', 'szor_hullas': 'nyaron'})

kutyak = [
    {'nev': 'Bloki', 'fajta': 'labrador', 'szine': 'fekete', 'szor_hullas': 'soha'},
    {'nev': 'Cukika', 'fajta': 'palotapincsi', 'szine': 'feher', 'szor_hullas': 'nyaron'}
]

with open('kutyak_jobb2.csv', mode='w') as kutya_adatok:
    kutya_writer = csv.DictWriter(kutya_adatok, fieldnames=kutyak[0].keys(), lineterminator="\n")

    kutya_writer.writeheader()
    for k in kutyak:
        kutya_writer.writerow(k)
