
# # property method: getter and setter

class Student:
    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total/5

    def getter(self):
        return self._total

    def setter(self, value):
        if isinstance(value, (int, float)) and value >= 0 and value <= 500:
            self._total = value
        else:
            print("Enter valid total")

    total = property(getter, setter)


s1 = Student(443)

print("Total   : ", s1.total)
print("Average : ", s1.average())
s1.total = 350
print("Total   : ", s1.total)
print("Average : ", s1.average())
