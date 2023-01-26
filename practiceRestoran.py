class Restoran:
    suffix_som = "som"
    menu = {
        "Шорпо" : 150,
        "Лагман" : 200,
        "Манты": 150,
        "Узгенский Плов": 200,
    }

    order_lst = []
    dishes_lst = []

    def order_dish(self, dishes):
        if dishes in self.menu:
            self.order_lst.append(self.menu[dishes])
            self.dishes_lst.append(dishes)
            return f"Ваш заказ принят. Вы закали '{dishes}'"
        else:
            raise ValueError("Такой еды у нас нету!")
    
    def check(self):
        el = " | ".join(self.dishes_lst)
        return f"\n{'*'*30}\n\nЧек:\nВы заказывали: {el}\nВаша сумма состовляет: {sum(self.order_lst)} {self.suffix_som}"


class Purse:
    full_money = None

    def __init__(self, name, money):
        self.name = name
        self.full_money = money
    
    def add_money(self, money):
        self.full_money += money
        return f"Вы добавили {money} som"
    
    def info_purse(self):
        return f"Вашем кашелке: {self.full_money} som"


class Main(Restoran, Purse):
    def __init__(self, name, money):
        self.name = name
        self.full_money = money
    
    def order_dish(self, dishes):
        return super().order_dish(dishes)
    
    def check(self):
        return super().check()
    
    def add_money(self, money):
        return super().add_money(money)
    
    def top_down(self, money):
        return super().top_down(money)
    
    def payment(self):
        self.full_money -= sum(self.order_lst)
        return f"Вы успешно оплатили\nВаш баланс состовляет: {self.full_money}"
    
    
a = Main("Dastan", 0)
print("*"*30)
print()
print(a.order_dish("Лагман"))
print(a.order_dish("Манты"))
print(a.order_dish("Шорпо"))
print(a.check())
print()
print('*'*30)
print()
print(a.add_money(2000))
print(a.info_purse())
print()
print('#'*30)
print(a.check())
print()
print(a.payment())
print()
print('#'*30)
  