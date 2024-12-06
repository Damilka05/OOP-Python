# TODO: Подробно описать три произвольных класса
import doctest

# TODO: описать класс


class Person:
    def __init__(self, first_name: str, second_name: str, patronymic='', age=18):
        """
        Создание и подготовка к работе объекта "Персона"

        :param first_name: Фамилия
        :param second_name: Имя
        :param patronymic: Отчество
        :param age: Возраст

        Примеры:
        >>> pers_1 = Person("Пушкин", "Александр", "Сергеевич", 20)  # инициализация экземпляра класса
        """
        if not isinstance(first_name, str):
            raise TypeError("Фамилия должна быть типа str")
        self.first_name = first_name
        if not isinstance(second_name, str):
            raise TypeError("Имя должно быть типа str")
        self.second_name = second_name
        if not isinstance(patronymic, str):
            raise TypeError("Отчество должно быть типа str")
        self.patronymic = patronymic
        self.age = age

    def get_patronymic(self, patronymic: str) -> None:
        """
        Функция, которая устанавливает/меняет отчество или убирает его

        Примеры:
        >>> pers_1 = Person("Пушкин", "Александр", "Сергеевич", 20)
        >>> pers_1.get_patronymic('')
        """
        if not isinstance(patronymic, str):
            raise TypeError("Отчество должно быть типа str")
        self.patronymic = patronymic

    def get_age(self, age: int) -> None:
        """
        Функция, которая устанавливает возраст

        Примеры:
        >>> pers_1 = Person("Пушкин", "Александр", "Сергеевич", 20)
        >>> pers_1.get_age(25)
        """
        if self.age < 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age


# TODO: описать ещё класс

class Wallet:
    def __init__(self, salary: int, total=2000):
        """
        Создание и подготовка к работе объекта "Кошелек"

        :param salary: З/п
        :param total: Баланс

        Примеры:
        >>> wal = Wallet(50000, 20000)  # инициализация экземпляра класса
        """
        if not isinstance(salary, (int, float)):
            raise TypeError("З/п должна быть типа int или float")
        if salary <= 0:
            raise ValueError("З/п должна быть положительным числом")
        self.salary = salary
        if not isinstance(total, (int, float)):
            raise TypeError("Баланс должн быть типа int или float")
        self.total = total

    def get_salary(self, salary: (int, float)) -> None:
        """
        Уствновка заработной платы

        Примеры:
        >>> wal = Wallet(50000, 20000)  # инициализация экземпляра класса
        >>> wal.get_salary(60000)
        """
        if not isinstance(salary, (int, float)):
            raise TypeError("З/п должна быть типа int или float")
        if salary <= 0:
            raise ValueError("З/п должна быть положительным числом")
        self.salary = salary

    def get_total(self, total: (int, float)) -> None:
        """
        Уствновка баланса кошелька

        Примеры:
        >>> wal = Wallet(50000, 20000)  # инициализация экземпляра класса
        >>> wal.get_total(5000)
        """
        if not isinstance(total, (int, float)):
            raise TypeError("Баланс должн быть типа int или float")
        self.total = total

    def view_total(self) -> int:
        """
        Запрос баланса кошелька

        :return: Баланс кошелька

        Примеры:
        >>> wal = Wallet(50000, 20000)  # инициализация экземпляра класса
        >>> wal.view_total()
        20000
        """
        return self.total

# TODO: и ещё один


class Company:
    def __init__(self, name_company: str, employee: int):
        """
        Создание и подготовка к работе объекта "Компания"

        :param name_company: Название компании
        :param employee: Количество работников

        Примеры:
        >>> comp = Company('Баскунчакская соль', 2500)  # инициализация экземпляра класса
        """
        if not isinstance(name_company, str):
            raise TypeError("Название компании должно быть типа str")
        self.name_company = name_company
        if not isinstance(employee, int):
            raise TypeError("Количество работников должно быть типа int")
        if employee <= 0:
            raise ValueError(
                "Количество работников должно быть положительным числом")
        self.employee = employee

    def show_name(self) -> None:
        """
        Показывает название компании

        Примеры:
        >>> comp = Company('Баскунчакская соль', 2500)  # инициализация экземпляра класса
        >>> comp.show_name()
        Баскунчакская соль
        """
        print(self.name_company)

    def show_employee(self) -> None:
        """
        Показывает количество работников

        Примеры:
        >>> comp = Company('Баскунчакская соль', 2500)  # инициализация экземпляра класса
        >>> comp.show_employee()
        2500
        """
        print(self.employee)


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
