from math import *
# class Phone:
#     def __init__(self, title, color, display, model, year_made):
#         self.name = title #Атрибуты объекта класса Phone
#         self.color = color
#         self.display = display
#         self.model = model
#         self.year_made = year_made

#     def call(self, number):
#         print(f'Calling {number}...')

#     def sms(self, number, text):
#         print(f'Sending sms to {number}: {text}')

#     def play_game(self, game_name):
#         print(f'Playing {self.name}, {game_name}...')


# phone = Phone('iPhone', 'silver', '6.1', 'X', 2020)
# phone.play_game('Doom Eternal')

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print(f'{self.name} is barking')

# bobik = Dog('Bobik', 3)
# bobik.bark()
# print(bobik.name)
# print(bobik.age)

# sharik = Dog('Sharik', 4)
# sharik.bark()

#Task 1
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def  width_of_circle(self):
        return 2 * pi * self.radius

    def area_of_circle(self):
        return pi * self.radius ** 2
    
circle = Circle(12.6)
print(f'Длина окружности: {round(circle.width_of_circle(), 2)}')
print(f'Площадь окружности: {round(circle.area_of_circle(), 2)}')

print('---------------')

#Task 2
class Calculator():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
calc = Calculator(34.2, 12.2)
print(f'Результат сложения: {calc.add()}')
print(f'Результат вычитания: {calc.sub()}')
print(f'Результат умножения: {calc.mul()}')
print(f'Результат деления: {calc.div()}')

print('---------------')

#Task 3
class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Имя: {str(self.name)}, Возраст: {int(self.age)} лет')


student = Student('Ануар Досмухамедов', 36)
student.info()

print('---------------')

#Task 4
class Rectangle():

     def __init__(self, width: float, height: float):
        if isinstance(width, (float, int)) or isinstance(height, (float, int)):

            self.width = width 
            self.height = height
        else:
            raise ValueError('Вы ввели неправильное значение')

     def area_of_rect(self):
         return self.width * self.height
     
rectangle = Rectangle(12, 56)

print(f'Площадь прямоугольника: {rectangle.area_of_rect()}')

print('---------------')

#Task 5
class Counter:
    def __init__(self, cur_value: int, max_value: int):
        self.cur_value = cur_value
        self.max_value = max_value

    def inc_value(self):
        if self.cur_value < self.max_value:
            self.cur_value += 1
            print('Мы увеличили счетчик на 1:', self.cur_value)

        else:
            print('Вы достигли максимального значения')

    def dec_value(self):
            self.cur_value -= 1
            print('Мы уменьшили счетчик на 1:', self.cur_value)

    def reset_value(self):
        self.cur_value = 0
        print('Счетчик сброшен')

counter = Counter(0, 10)

while True:
    i = input('Выберите действие \n1. увеличить \n2. уменьшить \n3. посмотреть текущее значение\n4. Сброс счетчика\n>>> ')
    if i == '1':
        counter.inc_value()
    elif i == '2':
        counter.dec_value()
    elif i == '3':
        print(counter.cur_value)
    elif i == '4':
        counter.reset_value()
        print(counter.cur_value)
        break
        
    print()
    print()

    

#Task 6
class Auto:

    def __init__(self, manufacturer, model, color):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
    
    def info(self):
        print(f'Марка: {self.manufacturer}, Модель: {self.model}, Цвет: {self.color}')


auto = Auto('Honda', 'CR-V', 'серебристный металлик')

auto.info()



    








