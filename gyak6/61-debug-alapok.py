from utils.students import Student, ClassRoom

MAGIC_NUMBER = 95


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    name = "Kiscica"
    if name == "Kiscica":
        print("A név kiscica volt")
        # Hozzunk letre egy hallgatot
        cn = Student("Chuck Norris", 65)
        cn.add_grade(5)
        # cn.add_grade("sajt")
        cn.add_grade(2)
        print('Avg', cn.avg())
        print('Max. grade', cn.max_grade())
        print('Min. grade', cn.min_grade())

        js = Student('Jon Snow', 30)
        js.add_grade(1)
        js.add_grade(5)

        heroes = ClassRoom()
        heroes.new_student(cn)
        heroes.new_student(js)
        # heroes.new_student("John Rambo")

        cnt = 1
        while cnt != 100:
            print(cnt // (cnt % MAGIC_NUMBER))
            cnt += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
