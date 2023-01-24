# Создайте базовый  класс “Валюта” для работы с денежными суммами.
# Определите методы перевода значения в сомы и вывода на экран.

# Реализуйте производные классы “Доллар” и “Евро” с собственными методами перевода в сомы и вывода на экран.

# * решите самостоятельно, какими свойствами будет обладать каждый из классов, и какие методы необходимо сделать 

# ***********************************
# 5 USD = 370.80 SOM

# 10 USD = 741.60 SOM

# 50 USD = 3708.00 SOM

# 100 USD = 7416.00 SOM
# ******************************
# 5 EURO = 450.70 SOM.

# 10 EURO = 901.40 SOM

# 50 EURO = 4507.00 SOM

# 100 EURO = 9014.00 SOM

class Valute:
    _USD = 86.14
    _EURO = 93.56

    _suffix_som = 'SOM'
    _suffix_usd = 'USD'
    _suffix_euro = 'EURO'

    @classmethod
    def _convert_dollar(cls, value):
        res = value * cls._USD
        return res
    
    @classmethod
    def _convert_euro(cls, value):
        res = value * cls._EURO
        return res


class Dollar(Valute):
    def convert(self, som):
        dollar = Valute._convert_dollar(som)
        return f'{som} {self._suffix_usd} = {dollar} {self._suffix_som}'
    


class Euro(Valute):   
    def convert(self, som):
        euro = Valute._convert_euro(som)
        return f'{som} {self._suffix_euro} = {euro} {self._suffix_som}'


dol = Dollar()
eur = Euro()

print()
print('*'*50)
print(dol.convert(5))        
print(dol.convert(10))        
print(dol.convert(50))        
print(dol.convert(100)) 
print('*'*40)
print(eur.convert(5))       
print(eur.convert(10))       
print(eur.convert(50))       
print(eur.convert(100))       
print()


class Currency:
    def __init__(self, value):
        self.value = value 
    
    def convert_to_som(self):
        pass 

    def print_value(self):
        print(self.value, end=" ")
    
class Dollar(Currency):
    rate_to_som = 86.14
    suffix = 'USD'
    
    def convert_to_som(self):
        som = self.value * Dollar.rate_to_som
        return som 
    
    def print_value(self):
        super().print_value()
        print(Dollar.suffix, end=" ")

class Euro(Currency):
    rate_to_som = 93.56
    suffix = 'Euro'

    def convert_to_som(self):
        som = self.value * Euro.rate_to_som
        return som 
    
    def print_value(self):
        super().print_value()
        print(Euro.suffix, end=" ")
    
d = [
    Dollar(5),Dollar(10),Dollar(50),Dollar(100),
]
e = [
    Euro(5),Euro(10),Euro(50),Euro(100),
]
for i in d:
    i.print_value()
    print(f" = {i.convert_to_som():.2f} SOM")

for i in e:
    i.print_value()
    print(f" = {i.convert_to_som():.2f} SOM")