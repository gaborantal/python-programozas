import itertools

for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")
print("\n---")

print("Jó sokszor megismételjük a legszebb számot")
print(list(itertools.repeat(2, 4)))
print("\n---")

szinek = ["sárga", "kék", "zöld", "barna", "piros"]
targyak = ["autó", "motor", "ház", "gomba"]

print(list(zip(szinek, targyak)))
print(list(itertools.zip_longest(szinek, targyak)))
print(list(itertools.zip_longest(szinek, targyak, fillvalue="valami")))

hallgatok = ["Harry Potter", "Ron Weasly", "Hermione Granger", "Ginny Weasley", ]
# "Tom Denem", "Sirius Black", "Dudley Dursley", "Albus Dumbledore",
# "Luna Lovegood", "Draco Malfoy", "Rubeus Hagrid", "Parvati Patil",
# "Neville Longbottom", "Romilda Vane"]

print("-- kombinációk")
print(list(itertools.combinations(hallgatok, 3)))
print(list(itertools.combinations_with_replacement(hallgatok, 3)))

print("-- permutációk")
print(list(itertools.permutations(hallgatok)))

print("-- ciklizálás")
count = 0
for i in itertools.cycle(hallgatok):
    print(i)
    count += 1
    if count == 100:
        break

lapok = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
szinek = ['H', 'D', 'C', 'S']  # hearts, diamonds, clubs, and spades


def pakli():
    for lap in lapok:
        for szin in szinek:
            yield lap, szin


pakli_0 = pakli()
pakli_1 = ((lap, szin) for szin in szinek for lap in lapok)
pakli_2 = itertools.product(lapok, szinek)

print(list(pakli_0))
print(list(pakli_1))
print(list(pakli_2))

hallgatok_1 = ["Harry Potter", "Ron Weasly", "Hermione Granger", "Ginny Weasley"]
hallgatok_2 = ["Tom Denem", "Sirius Black", "Dudley Dursley", "Albus Dumbledore"]

print(itertools.chain(hallgatok_1, hallgatok_2))
print(list(itertools.chain(hallgatok_1, hallgatok_2)))
