# 1)Создайте класс Phone, который содержит переменные number, name.
# 2)Выведите на консоль значения их переменных. 
# 3)Добавить в класс Phone методы: receiveCall, имеет один параметр – имя звонящего. Выводит на консоль сообщение “Звонит {name}”. Метод getNumber – возвращает номер телефона. Вызвать эти методы для каждого из объектов.
# 4)Создать метод sendMessage с аргументами переменной длины. Данный метод принимает на вход номера телефонов, которым будет отправлено сообщение на другой номер. Метод выводит на консоль номера этих телефонов и сообщение.

class Phone:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        print(f'Имя: {self.name} | Номер: {self.number}')
    
    def receiveCall(self, name, number, to_whom):
        if to_whom == self.number:
            return f"Вам звонит: {name} | {number}"
        else:
            return "Такого номера нет"
    
    def getNumber(self):
        return f'Ваше имя: {self.name} | Ваш номер: {self.number}'
    
    def sendMessage(self, name, number, to_whom, message):
        if to_whom == self.number:
            return f"Вам отправили сообщение!\n\n - {message} - \n\nИмя отправителя: {name}\nНомер отправителя: {number}"
        else:
            return "Такого номера нету!"
    
a = Phone('Deissei', 1111)
b = Phone('Husan', 2222)
c = Phone('Talgat', 3333)

print('*'*30)
print(b.receiveCall('Deissei', 1111, 2222))
print(b.getNumber())
print('*'*30)
print(c.sendMessage('Husan', 2222, 3333, "Привет! Как дела?"))
print()
print(c.getNumber())
print('*'*30)