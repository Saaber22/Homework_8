"""
Написать класс “animals” (животные), который включает общие признаки
 и поведения животных. От “animals” наследовать класс “mammals” 
 (млекопитающие), который включает общие признаки и поведения 
 млекопитающих. От “mammals” наследовать “human” (человек), 
 “cat”(кот), “dog”(собака), у каждого свои признаки и поведения.
 """

class animals:
    def __init__(self, gender, name, age, height, weight):
        """
        Входные данные:
        gender - пол
        name - имя
        age - возраст
        height - рост
        weigth - вес
        """
        self.gender = gender
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class mammals(animals):
    def __init__(self, gender, name, age, height, weight, family, type, country):
        """
        Входные данные:
        Насследованы из класса animals +
        family - семейство
        type - вид
        country - страна происхождения
        """
        super().__init__(gender, name, age, height, weight)
        self.family = family
        self.type = type
        self.country = country

class human(mammals):
    def __init__(self, gender, name, age, height, weight, family, type, country, company, position, income):
        """
        Входные данные:
        Насследованы из класса mmamals +
        company - организация
        position - должность
        income - оклад
        """
        super().__init__(gender, name, age, height, weight, family, type, country)
        self.company = company
        self.position = position
        self.income = income

class cat(mammals):
    def __init__(self, gender, name, age, height, weight, family, type, country, color, ears, eyes, wool):
        """
        Входные данные:
        Насследованы из класса mmamals +
        color - цвет кота
        ears - тип ушей
        eyes - цвет глаз
        wool - тип шерсти
        """
        super().__init__(gender, name, age, height, weight, family, type, country)
        self.color = color
        self.ears = ears
        self.eyes = eyes
        self.wool = wool

class dog(mammals):
    def __init__(self, gender, name, age, height, weight, family, type, country, wool, dog_tail, destination):
        """
        Входные данные:
        Насследованы из класса mmamals +
        destination - предназначение
        dog_tail - тип собачего хвоста
        wool - тип шерсти
        """
        super().__init__(gender, name, age, height, weight, family, type, country)
        self.dog_tail = dog_tail
        self.destination = destination
        self.wool = wool
        
    def say(self):
        if self.age > 0:
            print(f'Hello my name is {self.name}! I am {self.age} years.')

Lucifer = dog('male', 'Lucifer', 1, 30, 4, 'Canidae', 'Dog', 'Deutschland', 'Langhaarig', 'No', 'Home')
