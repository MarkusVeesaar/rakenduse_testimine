import unittest


class GradeCalculator:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        if not isinstance(grade, int):
            raise ValueError("Hinne peab olema täisarv")

        if grade < 1 or grade > 5:
            raise ValueError("Hinne peab olema 1 kuni 5")

        self.grades.append(grade)

    def average(self):
        if not self.grades:
            raise ValueError("Hindeid pole")

        return sum(self.grades) / len(self.grades)

    def passed(self):
        return self.average() > 3

    def clear(self):
        self.grades.clear()


def test():
    #postiivsed testid
    calc = GradeCalculator()
    calc.add_grade(5)
    calc.add_grade(4)
    print("Positiivne test:", calc.grades)
    print("Positiivne test:", calc.average())

    #negatiivsed testid
    try:
        calc.add_grade(7)
    except ValueError as e:
        print("Negatiivne test: 7 Viga:", e)

    try:
        calc.add_grade(2.5)
    except ValueError as e:
        print("Negatiivne test: 2.5 Viga:", e)

    #äärejuhtumid
    calc.clear()
    calc.add_grade(1)
    calc.add_grade(1)
    print("Äärejuhtum test:", calc.grades, calc.average())

    calc.clear()
    calc.add_grade(5)
    calc.add_grade(5)
    print("Äärejuhtum test:", calc.grades, calc.average())

    #vigase sisendi test
    calc.clear()
    try:
        calc.average()
    except ValueError as e:
        print("Vigase sisendi test: grades:" + str(calc.grades) + " Viga:", e)

    #koodi olev viga 
    calc.clear()
    calc.add_grade(3)
    print("Koodis olev viga test: Grades:",calc.grades, "passed:", calc.passed())


test()