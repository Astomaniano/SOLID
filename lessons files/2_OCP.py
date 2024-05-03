# Принцип открытости/закрытости (OCP, Open/Closed Principle)
#
# ✅Программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
# Суть в том, что уже существующий код не должен модифиироваться при добавлении новых функций. Это достигается за счёт
# использования абстракций и интерфейсов.
#
# Другими словами, мы должны иметь возможность добавлять новый функционал в программу, но при этом не изменять уже
# существующий код. Необходимо руководствоваться такой логикой ещё на этапе создания кода с нуля, чтобы потом не
# приходилось переделывать. Это достигается как раз с помощью абстракций и интерфейсов.
#
#
#
# Абстракции и интерфейсы Это очень похожие термины, но в нашей работе больше будут использоваться абстракции, так как
# интерфейсы в Python применяются не так часто.
#
# ✅Абстракция (абстрактный класс) — это своеобразный чертёж, шаблон для других классов, по которому можно создавать
# другие классы. В абстрактном классе могут быть как абстрактные, так и обычные методы.


# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f'сформирован отчет{self.title} {self.content}')

from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HTMLFormatted(Formatted):
    def format(self, report):
        print(f'<H1>{report.title}</H1>')
        print(f'<p>{report.content}</p>')

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)

report = Report('Заголовок отчета', 'Это текст отчета и его тут много', TextFormatted())

report.docPrinter()