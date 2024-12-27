# TODO: описать базовый класс
class Person:
    """
    Базовый класс для представления человека.

    Атрибуты:
        name (str): Имя человека.
        age (int): Возраст человека.
    """

    def __init__(self, name: str, age: int):
        """
        Инициализация объекта класса Person.

        :param name: Имя человека.
        :param age: Возраст человека.
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным числом")
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """
        Строковое представление объекта.

        :return: Строка с именем и возрастом.
        """
        return f"Имя: {self.name}, Возраст: {self.age}"

    def __repr__(self) -> str:
        """
        Представление объекта для разработчика.

        :return: Строка, показывающая инициализацию объекта.
        """
        return f"Person(name='{self.name}', age={self.age})"

    def birthday(self) -> None:
        """
        Увеличивает возраст человека на 1 год.
        """
        self.age += 1


class Wallet(Person):
    """
    Класс, представляющий человека с кошельком.
    Является дочерним классом Person.

    Атрибуты:
        balance (float): Баланс кошелька.
    """

    def __init__(self, name: str, age: int, balance: float = 0.0):
        """
        Инициализация объекта класса Wallet.

        :param name: Имя человека.
        :param age: Возраст человека.
        :param balance: Баланс кошелька (по умолчанию 0.0).
        """
        super().__init__(name, age)
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Баланс должен быть неотрицательным числом")
        self.__balance = balance  # Закрытый атрибут для защиты от прямого доступа

    def __str__(self) -> str:
        """
        Перегрузка строкового представления для Wallet.

        Причина: отображение баланса кошелька.
        """
        return f"{super().__str__()}, Баланс: {self.__balance: .2f}"

    def deposit(self, amount: float) -> None:
        """
        Пополнение баланса.

        :param amount: Сумма для пополнения.
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств.

        :param amount: Сумма для снятия.
        """
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount

    def get_balance(self) -> float:
        """
        Получение текущего баланса.

        :return: Баланс кошелька.
        """
        return self.__balance


class Company(Person):
    """
    Класс, представляющий человека как владельца компании.
    Является дочерним классом Person.

    Атрибуты:
        company_name (str): Название компании.
        employee_count (int): Количество сотрудников.
    """

    def __init__(self, name: str, age: int, company_name: str, employee_count: int):
        """
        Инициализация объекта класса Company.

        :param name: Имя владельца компании.
        :param age: Возраст владельца компании.
        :param company_name: Название компании.
        :param employee_count: Количество сотрудников компании.
        """
        super().__init__(name, age)
        if not isinstance(company_name, str):
            raise TypeError("Название компании должно быть строкой")
        if not isinstance(employee_count, int) or employee_count < 0:
            raise ValueError(
                "Количество сотрудников должно быть неотрицательным числом")
        self.company_name = company_name
        # Закрытый атрибут для защиты данных компании
        self.__employee_count = employee_count

    def __str__(self) -> str:
        """
        Перегрузка строкового представления для Company.

        Причина: добавление информации о компании.
        """
        return f"{super().__str__()}, Компания: {self.company_name}, Сотрудники: {self.__employee_count}"

    def hire_employees(self, count: int) -> None:
        """
        Увеличивает количество сотрудников.

        :param count: Количество новых сотрудников.
        """
        if count <= 0:
            raise ValueError(
                "Количество сотрудников для найма должно быть положительным")
        self.__employee_count += count

    def fire_employees(self, count: int) -> None:
        """
        Уменьшает количество сотрудников.

        :param count: Количество сотрудников для увольнения.
        """
        if count > self.__employee_count:
            raise ValueError("Невозможно уволить больше сотрудников, чем есть")
        self.__employee_count -= count

    def get_employee_count(self) -> int:
        """
        Получение текущего количества сотрудников.

        :return: Количество сотрудников.
        """
        return self.__employee_count


# Пример использования
if __name__ == "__main__":
    person = Person("Алексей", 30)
    wallet = Wallet("Мария", 25, 1500.0)
    company = Company("Дмитрий", 40, "TechCorp", 50)

    print(person)  # Имя: Алексей, Возраст: 30
    print(wallet)  # Имя: Мария, Возраст: 25, Баланс: 1500.00
    print(company)  # Имя: Дмитрий, Возраст: 40, Компания: TechCorp, Сотрудники: 50
