# Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)
#
# ✅Объекты в программе должны быть заменяемыми на экземпляры подтипов без влияния на правильность программы. Это значит,
# что объекты производного класса должны иметь возможность заменить объекты базового класса без изменения работы программы.
#
# Этот принцип означает, что когда у нас есть родительский и дочерний классы, мы можем использовать родительский класс в
# любых местах, где мы ожидаем использование родительского класса. Другими словами, и тот, и другой класс мы можем
# использовать, и при этом программа будет оставаться рабочей.
# И у класса родительского, и у дочернего класса при этом есть объекты, которые мы используем с какими-то функциями.
# Например, если мы написали "класс родителя.fly", мы можем заменить его на "класс потомка.fly", и ошибки это вызывать
# не должно. Это и есть принцип подстановки.


# class Bird():
#     def __init__(self, name):
#         self.name = name
#     def fly(self):
#         print(f'{self.name} летает')
#
# class Ping(Bird):
#     pass
#
# p = Ping("Сара")
#
# p.fly()

class Bird():
    def fly(self):
        print('Летает')

class Duck(Bird):
    def fly(self):
        print('Летает быстро')

def fly_in_the_sky(animal):
    animal.fly()

b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)