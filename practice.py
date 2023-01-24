'''
Создать класс “Account”, представляющий собой банковский счет. Класс должен содержать:

- динамические свойства: фамилия владельца, номер счета, процент начисления, сумма в cомах;

- инициализатор: определяет динамические свойства класса и выводит информацию об открытом счете;

- статические свойства: курс сома по отношению к доллару, курс сома по отношению к евро;

- классовые методы: редактировать курс сома по отношению к доллару, редактировать курс сома по отношению к евро;
- статические методы: перевод суммы в доллары и евро;

- методы: смена владельца счета, снятие заданной суммы, начисление заданной суммы, начисление процентов,

- деструктор: выводит сообщение о том, что банковский счет закрыт;

перевод в доллары и евро (в отличие от аналогичных статических методов, данные методы не принимают параметров),
вывод информации о счете;
'''

class Account:
    rate_usd = 0.012
    rate_euro = 0.011
    suffix = 'SOM'
    suffix_usd = 'USD'
    suffix_euro = 'EURO'

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f"Счет #{self.num} принадлежащий {self.surname}")
        print('*'*30)
    
    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate 

    @classmethod
    def set_euro_rate(cls, rate):
        cls.rate_euro = rate

    @staticmethod
    def convert(value, rate):
        return value*rate 
    
    def conver_to_usd(self): # перевод в usd
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
    
    def conver_to_euro(self): # перевод в euro
        euro_val = Account.convert(self.value, Account.rate_euro)
        print(f"Состояние счета: {euro_val} {Account.suffix_euro}")

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def print_info(self): # выводить инфо о счете
        print("Инфо о счете")
        print(f"#{self.num}")
        print(f"Владелец {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
    
    def change_surname(self, new_name):
        self.surname = new_name
        print(f'Имя изменено на {new_name}')
    
    def get_summ(self, get_sum):
        self.value -= get_sum
        print(f'Снятая сумма: {get_sum} {Account.suffix} | На болансе осталось: {self.value} {Account.suffix}')

    def accrual_summ(self, summ):
        self.value += summ
        print(f'Вы начислили: {summ} {Account.suffix} | У вас на балансе: {self.value} {Account.suffix}')

    def accrual_value(self):
        self.value+=self.value*self.percent
        self.print_balance()

# acc = Account('Aibek', 12345, 0.03, 1000)
# acc.print_info()
# acc.conver_to_usd()
# acc.conver_to_euro()
# print()
# Account.set_usd_rate(2)
# Account.set_euro_rate(3)
# acc.conver_to_usd()
# acc.conver_to_euro()
# print()
# acc.change_surname('Adilet')
# acc.print_info()
# print()
# acc.get_summ(500)
# print()
# acc.accrual_summ(10000)
# print()
# acc.accrual_value()
# acc.print_info()
# print()
# acc.conver_to_usd()
# # print()
# acc.conver_to_euro()


class Date:
    def __init_(self, day=0, mouth=0, year=0):
        self.day = day
        self.mouth = mouth
        self.year = year
    
    @classmethod
    def from_string(cls, date):
        day,mouth,year = map(int, date.split('.'))
        date1 = cls(day, mouth, year)
        return date1

    def srting_to_db(self):
        return f'{self.year}-{self.mouth}-{self.day}'
    
d = '21.01.2003'