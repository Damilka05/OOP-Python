class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом!")
        if value <= 0:
            raise ValueError("Количество страниц должно быть неотрицательно!")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, {self.pages} страниц"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом!")
        if value <= 0:
            raise ValueError("Продолжительность должна быть неотрицательно!")
        self._duration = float(value)

    def __str__(self):
        return f"{super().__str__()}, продолжительность {self.duration: .2f} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration: .2f})"
