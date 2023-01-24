
class Liquid:
    def __init__(self, name, density):
        self._name = name
        self._density = density # плотность

    def edit_density(self, val): # изменение плотности
        self._density = val 
    
    def calc_v(self, m): # вычисление объема жидкости, соответствующего заданной массе
        res = m / self._density
        print(f"Объем {m} kg {self._name} равен {res} m^3")
        return res 
    
    def calc_m(self, v): # вычисление массы жидкости соответствующего заданному объему
        res = v * self._density
        print(f"Вес {v} m^3 {self._name} составляет {res} kg")

    def print_info(self):
        print(f"Жидкость {self._name} плотность = {self._density} kg/m^3 ecn", end=" ")
    

class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength # крепость
    
    def edit_strength(self, val): # изменение крепости
        self.strength = val 
    
    def calc_v(self, m):
        super().calc_v(m)
        res = m*self.strength
        print(f"Объем алкоголя {m} kg {self._name} равен {res} m^3")
    
    def calc_m(self, v):
        super().calc_m(v)
        res = v*self.strength
        print(f"Вес алкоголя {v} m^3 {self._name} составляет {res} kg")
    
    def print_info(self):
        res = super().print_info()
        print(f'{res} крепость = {self._density:.1%}')
    
    @property
    def name(self):
        return self._name
        



a = Alcohol('Wine', 993, 14)
a.print_info()
print()
a.edit_density(1000)
a.print_info()
print()
a.calc_v(300)
a.calc_m(0.5)
print()
print(a.strength)
a.edit_strength(20)
print(a.strength)

# public открытый переменный
# protected - защищенными _name 
# private - приватный getter setter __