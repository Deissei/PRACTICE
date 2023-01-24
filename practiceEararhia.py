# => Мой код! {

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Student(Human):
    def __init__(self, name, surname, age, facul, group, esti):
        super().__init__(name, surname, age)
        self.facul = facul
        self.group = group
        self.esti = esti

    def info(self):
        return f"{self.name} {self.surname} {self.age} {self.facul} {self.group} {self.esti}"    

class Teacher(Human):
    def __init__(self, name, surname, age, prof, rating):
        super().__init__(name, surname, age)
        self.prof = prof
        self.rating = rating

    def info(self):
        return f"{self.name} {self.surname} {self.age} {self.prof} {self.rating}"


class Graduate(Student):
    def __init__(self, name, surname, age, facul, group, esti, work):
        super().__init__(name, surname, age, facul, group, esti)
        self.work = work

    def info(self):
        return f"{self.name} {self.surname} {self.age} {self.facul} {self.group} {self.esti} {self.work}"


bat = Student('Даши', "Батодалаев", 16, "ГК", "Web_011", 5)
lin = Student('Линар', "Загидуллин", 32, "РПО", "PD_011", 5)
ser = Graduate('Сергей', "Шугани", 15, "РПО", "PD_011", 5, 'Защита персональных данных')
andr = Teacher('Андрей', "Даньшин", 38, "Астрофизика", 110) 
mar = Student('Даниил', "Маркин", 17, "ГК", "Python_011", 5)
alec = Teacher('Алексей', "Башкиров", 45, "Разработка Приложений", 20) 

print()
print(bat.info())
print(lin.info())
print(ser.info())
print(andr.info())
print(mar.info())
print(alec.info())
print()

# }