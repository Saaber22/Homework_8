"""
Написать класс “Student”, который наследует класс human, 
у которого среди прочих признаков есть “Количество сданных дз”.
"""
from home8_1 import human

human_1 = human

class student(human_1):
    def __init__(self, gender, name, age, height, weight, family, type, country, company, position, income, homework):
        super().__init__(gender, name, age, height, weight, family, type, country, company, position, income)
        self.homework = homework
    
    def homew(self):
        if self.homework > 0:
            print(f'Hello my name is {self.name}! I have completed {self.homework} homework. ')

Lapin = student('male', 'Ilya', 27, 181, 85, 'Гоминиды', 'People', 'Russia', 'Tenzor', 'System_administator', 50000, 7)
Glazunova = student('female', 'Natalya', 25, 156, 49, 'Гоминиды', 'People', 'Russia', 'Tenzor', 'System_administator', 50000, 6)
Nazarenko = student('female', 'Viktorya', 27, 164, 55, 'Гоминиды', 'People', 'Russia', 'Tenzor', 'System_administator', 50000, 9)

for student in (Lapin,Glazunova,Nazarenko):
    student.homew()

    