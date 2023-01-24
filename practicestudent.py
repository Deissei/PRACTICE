class Student:
    def __init__(self, name, prof):
        self.name = name
        self.prof = prof
        self.books = []
        self.knowledge = 0
        self.is_ready_to_work = False
        self.languages = {}
    
    def add_points(self, points):
        self.knowledge += points
        if self.knowledge > 1000:
            self.is_ready_to_work = True
            return f'Этот студент готов к работе'
        
    def read_book(self, book):
        self.books.append(book)
        self.add_points(50)

    def do_homework(self):
        self.add_points(10)
    
    def do_project(self):
        self.add_points(50)
    
    def learn_new_language(self, lang, points):
        if points < 1 or points > 100:
            raise ValueError("Так делать нельзя")
        else:
            self.languages[lang] = points
            self.add_points(points)
    
    def info(self):
        return f'Меня зовут: {self.name} | Моё призвание: {self.prof}\nЯ читал: {self.books} | За время обучения я накопил: {self.knowledge} баллов\nК работе: {self.is_ready_to_work} | Владею: {self.languages}'

kuma = Student('Kuma', 'Backend')
# print(kuma.info())
kuma.do_homework()
kuma.read_book("Тонкое искуство пофигизма")
kuma.read_book("Чистая архитектура")
kuma.read_book("Грокаем алгоритмы")
kuma.do_project()
kuma.learn_new_language('Python', 80)
kuma.learn_new_language('Html', 10)
kuma.learn_new_language('Css', 10)
kuma.learn_new_language('Flask_Framework', 70)
print(kuma.info())
