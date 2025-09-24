class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Животное издаёт звук"

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Звук: {self.make_sound()}")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Мяу!"

    def info(self):
        print(f"[Кошка] Информация о {self.name}:")
        super().info()


if __name__ == "__main__":
    generic_animal = Animal("Существо")
    my_dog = Dog("Барбос")
    my_cat = Cat("Мурка")

    print("=== Базовый класс ===")
    generic_animal.info()

    print("\n=== Производный класс Dog ===")
    my_dog.info()

    print("\n=== Производный класс Cat (с расширенным info) ===")
    my_cat.info()

    input("\nДемонстрация завершена. Нажмите Enter для выхода...")