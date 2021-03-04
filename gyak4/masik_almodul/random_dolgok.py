import random


def random_sor():
    sorok = ["Never gonna give you up",
             "Never gonna let you down",
             "Never gonna run around and desert you",
             "Never gonna make you cry",
             "Never gonna say goodbye",
             "Never gonna tell a lie and hurt you"]

    return random.choice(sorok)


def random_szerencseszam_generator():
    """
    Random szerencseszam
    :return:
    """
    return random.choice([1, 2, 3, 7, 13, 42, 1024])


# print("!!!")
# print("Itt egy kiiratas a globalis scope-ban!")
# print("!!!")

if __name__ == '__main__':
    print("!!!")
    print("Itt egy kiiratas a globalis scope-ban!")
    print("!!!")
