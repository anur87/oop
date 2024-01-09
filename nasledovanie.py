class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def eat(self):
        print(f"{self.name} кушает еду")
    
    def sleep(self):
        print(f"{self.name} спит")
    
    def work(self):
        print(f"{self.name} работает")
    
    def relax(self):
        print(f"{self.name} отдыхает")
   

class Doctor(Person):
    def __init__(self, name, surname, age,  knife):
        Person.__init__(self, name, surname, age)
        self.knife = knife

    def heal(self):
        print(f"{self.name} лечит")

    def __str__(self):
        return f"Это доктор {self.name} {self.surname}"

class Miner(Person):
    def __init__(self, name, surname, age,  kirka):
        super().__init__(name, surname, age)
        self.kirka = kirka

    def eat(self):
        super().eat()
        print(f"и еще {self.name} кушает камень")

    def mine(self):
        print(f"{self.name} майним")

    def __str__(self):
        return f"Это майнер {self.name} {self.surname}"

class Child(Doctor, Miner):
    def __init__(self, name, surname, age, knife, kirka):
        Doctor.__init__(self, name, surname, age, knife)
        Miner.__init__(self, name, surname, age, kirka)

    def __str__(self):
        return f"Это детский доктор {self.name} {self.surname}\n {self.kirka=} {self.knife=}"


d = Doctor('Настя', 'Иванова', 30, 'Короткий нож')
m = Miner('Вася', 'Пушкин', 30, 'Кирка 3го уровня')


c = Child('Аня', 'Пушкинa', 5, 'Короткий нож', 'Кирка 3го уровня')
print(c)
    
