import csv
import os

data = dict()
with open("netflix_titles.csv", encoding="utf8") as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        if row['release_year'] not in data:
            data[row['release_year']] = list()
        data[row['release_year']].append(row)

os.mkdir("netflix_yearly_data")
for year, netflix_data in data.items():
    with open(os.path.join("netflix_yearly_data", f"data-{year}.csv"), "w", encoding="utf8") as fp:
        writer = csv.DictWriter(fp, fieldnames=netflix_data[0].keys(), lineterminator="\n")

        writer.writeheader()
        for k in netflix_data:
            writer.writerow(k)
