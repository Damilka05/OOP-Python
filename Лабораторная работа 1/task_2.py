# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from task_1 import Person, Wallet, Company

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    pers_1 = Person("Пушкин", "Александр", "Сергеевич", 20)
    wal = Wallet(50000, 20000)
    comp = Company('Баскунчакская соль', 2500)
    try:
        pers_1 = Person(252, "Александр", "Сергеевич", 20)
        pers_1 = Person("Пушкин", 552, "Сергеевич", 20)
        pers_1 = Person("Пушкин", "Александр", 000, 20)
        pers_1 = Person("Пушкин", "Александр", "Сергеевич", '20')
        pers_1.get_patronymic(2582)
        pers_1.get_age("25")
     # TODO: вызвать метод с некорректными аргументами(b)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        wal = Wallet("50000", 20000)
        wal = Wallet(50000, "20000")
        wal.get_salary("60000")
        wal.get_total("5000")
     # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        comp = Company(1525, 2500)
        comp = Company('Баскунчакская соль', "2500")
     # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')
