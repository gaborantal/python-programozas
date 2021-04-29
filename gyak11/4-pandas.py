import os
import pandas as pd
import numpy as np

array = [1, 3, 5]
series = pd.Series(array)

print(series)

series = pd.Series(array, index=["elso", "masodik", "harmadik"])

print(series)

dictionary = {"elso": 1, "masodik": 3, "harmadik": 5}
series = pd.Series(dictionary)
print(series)

data = {
    "nem": ["ferfi", "no", "no", "ferfi"],
    "kor": [23, 32, 42, 19]
}

df = pd.DataFrame(data)
print(df)
print(df.to_string())
print(df.to_csv())

print("loc0", df.loc[0])


print(df.loc[[0, 2]])  # nem  kor
# 0  ferfi   23
# 2     no   42

df1 = pd.read_csv(os.path.join("data", "data1.csv"))
# df3 = pd.read_excel(os.path.join("data", "data.xls"), "Sheet1")
df3 = pd.read_excel(os.path.join("data", "titanic3.xls"))
df2 = pd.read_json(os.path.join("data", "pulse.json"))

with open(os.path.join("data", "shows.json")) as project_file:
    import json
    data = json.load(project_file)
df4 = pd.DataFrame(data.get('_embedded').get('episodes'))
df5 = pd.json_normalize(data.get('_embedded').get('episodes'))
print("ST", df4.head())
print("ST", df5.head())

print(df.head(2))  # Az első 2 sor megjelenítése
print(df2.tail(2))  # Az utolsó 2 sor megjelenítése

print(df.info())
# Alap információk a DataFrame-ről
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3			<-- sorok száma
# Data columns (total 2 columns):		<-- oszlopok száma
# #   Column  Non-Null Count  dtype 	<-- az oszlopok neve és adattípusa
# ---  ------  --------------  -----
# 0   nem     4 non-null      object
# 1   kor     4 non-null      int64
# dtypes: int64(1), object(1)
# memory usage: 192.0+ bytes
# None
print("-------------")
print("- mean", df.mean())  # A sorok átlaga oszloponként
print("- count", df.count())  # A nem üres sorok száma oszloponként
print("- max", df.max())  # A legnagyobb érték oszloponként (szövegnél ábécé sorrendben utolsó)
print("- min", df.max())  # A legkisebb érték oszloponként (szövegnél ábécé sorrendben első)
print("- median", df.median())  # A sorok mediánja oszloponként
print("-------------")

data1 = {
    "nem": ["ferfi", "no", "no", "ferfi"],
    "kor": [23, 32, 42, 19]
}
data2 = {
    "nem": ["ferfi", "ferfi"],
    "kor": [30, 65]
}
data3 = {
    "hazas": [True, False]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

df1.append(df2)  # További sorok beszúrása

df3 = pd.concat([df1, df3], axis=1)  # df1 oszlopai mellé kerülnek df2 oszlopai
#      nem  kor  hazas
# 0  ferfi   23   True
# 1     no   32  False
# 2     no   42    NaN
# 3  ferfi   19    NaN

print(pd.isnull(df3))  # egy True/False táblázatot ad vissza, ahol a True értékek jelölik a hiányzó cellákat
#      nem    kor  hazas
# 0  False  False  False
# 1  False  False  False
# 2  False  False   True
# 3  False  False   True

pd.notnull(df3)  # ugyan ez csak fordítva

print(df3.dropna())  # törli azokat a sorokat, amiknél van NaN érték valamelyik oszlopban
# alapértelmezetten nem változtatja meg a változó tartalmát,
# de ha az inplace paraméterét igazra állítjuk, akkor már igen

#      nem  kor  hazas
# 0  ferfi   23   True
# 1     no   32  False

print("-dropna\n", df3.dropna(axis=1))  # törli azokat az oszlopokat, amiknél van NaN érték valamelyik sorban
# inplace paraméter itt is ugyan úgy működik

#      nem  kor
# 0  ferfi   23
# 1     no   32
# 2     no   42
# 3  ferfi   19

df3.drop_duplicates(inplace=True)  # Törli a duplikátumokat

df3["hazas"].fillna(True, inplace=True)  # A NaN értékek feltöltése a "hazas" oszlopban úgy,
# hogy a változtatások mentődnek a df3 változóba

df3_kutyak = df3.copy()
df3_kutyak["kutyak_szama"] = np.random.randint(0, 6, df3_kutyak.shape[0])
print(df3_kutyak)


print(df3)  # nem  kor  hazas
# 0  ferfi   23   True
# 1     no   32  False
# 2     no   42   True
# 3  ferfi   19   True

df3["hazas"].replace(True, "hazas")  # A "hazas" oszlopban a True értékek módosítása a "hazas" szóra
df3["hazas"].replace(False, "nem hazas")
# vagy egyszerre, úgy hogy változzon df3 értéke
df3["hazas"].replace([True, False], ["hazas", "nem hazas"], inplace=True)
print(df3)  # nem  kor      hazas
# 0  ferfi   23      hazas
# 1     no   32  nem hazas
# 2     no   42      hazas
# 3  ferfi   19      hazas

df3.rename(columns={"hazas": "hazas-e"}, inplace=True)  # Oszlop átnevezése
print(df3)

print(df3[df3["kor"] > 30])  # boolean szűrés, akár több kifejezést is összekapcsolhatunk & és | jelekkel
print(df3.sort_values("kor"))  # értékek rendezése a megadott oszlop szerint, alapértelemzetten növekvő sorrendben
#      nem  kor      hazas
# 3  ferfi   19      hazas
# 0  ferfi   23      hazas
# 1     no   32  nem hazas
# 2     no   42      hazas

df3.sort_values(["kor", "hazas-e"], ascending=[False, True])  # rendezés több oszlop alapján csökkenő és növekvő sorrendben
group = df3.groupby("hazas-e")  # groupby egy oszlop szerint
print(group.describe())  # kor
#           count  mean        std   min   25%   50%   75%   max
# hazas-e
# hazas       3.0  28.0  12.288206  19.0  21.0  23.0  32.5  42.0
# nem hazas   1.0  32.0        NaN  32.0  32.0  32.0  32.0  32.0

df3.to_csv("valami.csv")
df3.to_json("valami.json")

df3.to_excel("valami.xlsx") # Szükséges hozzá az openpyxl
