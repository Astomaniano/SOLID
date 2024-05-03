# Принцип инверсии зависимости (DIP, Dependency Inversion Principle)
#
# ✅Модули высокого уровня не должны зависеть от модулей низкого уровня. Оба типа модулей должны зависеть от абстракций.
#
# Абстракции не должны зависеть от деталей; детали должны зависеть от абстракций. Это позволяет разрабатывать систему
# более гибкой и способствует её лёгкому тестированию.
#
# Представим, что у нас есть конструктор для строительства домов и машин. Для дома мы используем крупные детали
# конструктора (модули высокого уровня), а для машин — более мелкие детали (модули низкого уровня). Если большие модули
# будут использовать маленькие модули, то мы сможем создать постройку только в одном стиле. Но если мы не позволим
# высокоуровневым модулям зависеть от низкоуровневых, то сможем строить любые конструкции. Мы должны сделать так, чтобы
# наши модули зависели от абстракций. Что такое абстракции, мы уже знаем.

# class Book():
#     def read(self):
#         print('читаем книгу')
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()

from abc import ABC, abstractmethod
class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print('читаем книгу')

class Audiobook(StorySource):
    def get_story(self):
        print('слушаем аудиокнигу')

class StoryReader:
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

book = Book()
audiobook = Audiobook()

readerBook = StoryReader(book)
readerAudioBook = StoryReader(audiobook)

readerBook.tell_story()
readerAudioBook.tell_story()