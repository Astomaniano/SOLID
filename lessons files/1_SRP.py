# SOLID — это акроним, представляющий пять основных принципов объектно-ориентированного программирования и дизайна,
# направленных на улучшение разработки системы, сделав её более понятной, гибкой и поддерживаемой. Эти принципы были
# введены Робертом Мартином, также известным как Uncle Bob, в начале 2000-х.
#
# Принципы SOLID:
#
# принцип единственной ответственности (Single Responsibility Principle);
# принцип открытости/закрытости (Open closed Principle);
# принцип подстановки Барбары Лисков (Liskov substitution Principle);
# принцип разделения интерфейсов (Interface Segregation Principle);
# принцип инверсии зависимости (Dependency Inversion Principle)
# Рассмотрим каждый из этих принципов подробнее и научимся их применять.
#
# Принцип единственной ответственности (SRP, Single Responsibility Principle)
# Принцип единственной ответственности гласит, что каждый класс должен иметь только одну причину для изменения. Это
# означает, что класс должен выполнять только одну задачу или иметь только одну область ответственности.
# Это упрощает тестирование и поддержку кода.
#
# Проще говоря, не стоит загружать класс множеством разнообразных функций. Если у нас есть класс, который занимается и
# отправкой писем, и хранением данных пользователя, и генерацией отчётов, то, например, при изменении способа отправки
# писем не должно затрагиваться хранение данных, способы их извлечения, генерирование отчётов. Другими словами, всё должно
# быть разделено, чтобы у каждого была своя ответственность.

# class UserManager():
#     def __init__(self, user):
#         self.user = user
#     def change_user_name(self, user_name):
#         self.user = user_name
#
#     def save_user(self):
#         with open('user.txt', 'a') as file:
#             file.write(self.user)

class User():
    def __init__(self, user):
        self.user = user

class UserNameChanger():
    def __init__(self, user):
        self.user = user
    def change_name(self, new_name):
        self.user = new_name

class SaveUser():
    def __init__(self, user):
        self.user = user
    def save_user(self):
        with open('user.txt', 'a') as file:
            file.write(self.user)