class Student:
    def __init__(self, name="Nincs nevem", age=12):
        self.name = name  # aktualis objektum vs. parameter neve
        self.age = age
        self._grades = list()  # ures lista (tomb)

    def add_grade(self, grade):
        self._grades.append(int(grade))

    def avg(self):
        sum_grades = 0
        for grade in self._grades:
            sum_grades += grade
        return sum_grades / len(self._grades)
        # return sum(self.grades) / len(self.grades)

    def max_grade(self):
        return max(self._grades)

    def min_grade(self):
        return min(self._grades)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class ClassRoom:
    def __init__(self):
        self._students = list()

    def new_student(self, student):
        if isinstance(student, Student):
            self._students.append(student)
        else:
            raise Exception("Only Student can be inserted!")
            # print("You can't do that")

    def avg(self):
        avgs = [student.avg() for student in self._students]
        return sum(avgs) / len(avgs)

    def __str__(self):
        return ("[Just a class, which consist of "
                "%d student(s).]" % len(self._students))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __add__(self, other):
        if isinstance(other, ClassRoom):
            returned = ClassRoom()
            returned._students = self._students + other._students
            return returned

