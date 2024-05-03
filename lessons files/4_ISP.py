# Принцип разделения интерфейсов (ISP, Interface Segregation Principle)
#
# ✅Клиенты не должны быть вынуждены зависеть от интерфейсов, которые они не используют. Суть в создании
# специализированных интерфейсов вместо одного, делающего всё подряд. Это упрощает внедрение зависимостей и повышает
# гибкость системы.Объекты в программе должны быть заменяемыми на экземпляры подтипов без влияния на правильность
# программы. Это значит, что объекты производного класса должны иметь возможность заменить объекты базового класса
# без изменения работы программы.
#
# Представим, что у нас дома много разных устройств: микроволновка, телевизор, система освещения и так далее. Если мы
# хотим включить музыку, мне не нужны кнопки для управления другими устройствами. Было бы неудобно иметь огромный пульт,
# на котором множество кнопок для всех устройств в доме. Вместо этого удобнее иметь отдельный пульт только для музыки.
# Это и есть принцип разделения интерфейсов: создание пульта для каждого устройства делает управление проще и понятнее.

# class SmartHouse():
#     def turn_on_light(self):
#         pass
#     def heat_food(self):
#         pass
#     def turn_on_music(self):
#         pass

class Light():
    def turn_on_light(self):
        print('свет включен')

class HeatFood():
    def heat_food(self):
        print('еда разогревается')

class Music():
    def turn_on_music(self):
        print('музыка включена')