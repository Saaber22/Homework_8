"""
Перегрузить операторы сравнения так, чтобы студенты 
сравнивались по количеству сданных ими дз.
"""
class student:
        def __init__(self, name, homework):
            self.name = name 
            self.homework = homework
        """Перезагружаем операторы сравнения по сданным ДЗ"""
        def __gt__(self, text):
            return int(self.homework) > int(text.homework)
        def __eq__(self, text):
            return int(self.homework) == int(text.homework)
        def __ne__(self, text):
            return int(self.homework) != int(text.homework)

Lapin = student('Ilya', 9)
Glazunova = student('Natalya', 8)
Nazarenko = student('Victorya', 7)

print(f'{Lapin.name} выполнил домашних работ {Lapin.homework}')
print(f'{Glazunova.name} выполнила домашних работ {Glazunova.homework}')
print(f'{Nazarenko.name} выполнила домашних работ {Nazarenko.homework}')

if Lapin.__gt__(Glazunova):
    if Lapin.__gt__(Nazarenko):
        print(f'Больше всех работ сдал {Lapin.name}')
    else:
        print(f'Больше всех работ сдала {Nazarenko.name}')
else:
    if Glazunova.__gt__(Nazarenko):
        if Glazunova.__eq__(Nazarenko):
            print(f'Больше всех работ сдали {Nazarenko.name} и {Glazunova.name}')
        else:
            if Glazunova.__eq__(Nazarenko):
                print(f'Больше всех работ сдали {Glazunova.name} и {Nazarenko.name}')
            else:
                print(f'Больше всех работ сдала {Glazunova.name}')
    else:
        if Lapin.__eq__(Nazarenko):
            print(f'Больше всех работ сдали {Lapin.name} и {Nazarenko.name}')
        else:
            if Glazunova.__eq__(Nazarenko):
                print(f'Больше всех работ сдали {Nazarenko.name} и {Glazunova.name}')
            else:
                print(f'Больше всех работ сдала {Nazarenko.name}')