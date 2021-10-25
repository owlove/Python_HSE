'''
Описание предметной области: Виды морских судов, их взаимодействия между собой
'''
import pickle
import random
from dataclasses import dataclass

class Sailors:
    """Класс описывающий моряков"""
    def __init__(self, ship, armament, coins):
        self.ship = ship # морское судно
        self.armament = armament # вооружение
        self.coins = coins # монеты

    def __str__(self):
        return f"Судно: {self.ship}\nВооружение: {self.armament}\nКоличество монет: {self.coins}\n"

class Pirates(Sailors):
    """Класс описывающий пиратов"""
    def __init__(self, armament, coins):
        """Инициализация атрибутов класса родителя"""
        self.ship = "Пиратское судно"
        self.armament = armament
        self.coins = coins
        self.kraken_legend = Kraken()

    def attack(self, ship):
        """Нападает на судно"""
        print(f"Атакуем {ship}!!!")

    def escape(self):
        """Побег с поля боя"""
        print("Сматываемся, ребята!")

class Navy(Sailors):
    """Класс описывающий военно-морской флот"""
    def __init__(self, armament, coins):
        """Инициализация атрибутов класса родителя"""
        self.ship = "Военное судно"
        self.armament = armament
        self.coins = coins

    @property
    def basic_description(self):
        """Выводит основную информацию объекта класса"""
        return f"{self.ship} на котором находится {self.armament}"

    def attack(self, ship):
        """Нападает на судно"""
        print(f"Атакуем {ship}!!!")

    def defence(self, ship):
        """Защищает судно"""
        print(f"Атакуем {ship}!!!")

class Sea_traders(Sailors):
    """Класс описывающий морских торговцев"""
    def __init__(self, armament, coins):
        """Инициализация атрибутов класса родителя"""
        self.ship = "Торговое судно"
        self.armament = armament
        self.coins = coins

    def call_for_help(self):
        """Зовет на помощь"""
        print("Помогите!")

    def __add__(self, other):
        """Забрать монеты"""
        if isinstance(other, self.__class__):
            return Sea_traders(self.coins + other.coins)
        elif isinstance(other, (int, float)):
            return Sea_traders(self.coins + other)

    def __sub__(self, other):
        """Отдать монеты"""
        if isinstance(other, self.__class__):
            return Sea_traders(self.coins - other.coins)
        elif isinstance(other, (int, float)):
            return Sea_traders(self.coins - other)

    def __eq__(self, other):
        """Заглянуть в чужой сундук с монетами и сравнить со своим"""
        if isinstance(other, self.__class__):
            return Sea_traders(self.coins == other.coins)
        elif isinstance(other, (int, float)):
            return Sea_traders(self.coins == other)

@dataclass
class Kraken:
    """Класс описывающий легендарного Кракена"""
    weight = 100000
    eye_color = "красный"
    number_of_tentacles = 15

    def description(self):
        """Выводит описание Кракена"""
        return print(f"Кракен весит {self.weight} кг, цвет глаз - {self.eye_color}, а щупальц целых {self.number_of_tentacles} шт.!\n")

class SaveInfo(Exception):
    """Класс, который отлавливает ошибку"""
    def __init__(self, message):
        self.message = message

# Создание экземпляров класса
Davey_Jones = Pirates("16 пушек и 20 пиратов", 1000) # Пираты
Jack_trader = Sea_traders("8 стражников", 3500) # Торговцы
Funny_Djo = Sea_traders("4 стражника", 2000) # Торговцы
English_guys = Navy("10 пушек и 35 солдат", 1500) # Военные
sailors = Sailors("Лодка", "Нет оружия", 30) # Базовый класс мореплаватель

# Вывод полного описания объекта класса
print(Davey_Jones)

# Послушать легенду о Кракене от Дейви Джонса
Davey_Jones.kraken_legend.description()

# Тестирование перегрузки методов
print(Jack_trader.coins + Funny_Djo.coins)
print(Jack_trader.coins - Funny_Djo.coins)
print(Jack_trader.coins == Funny_Djo.coins)

# Тестирование свойств класса
print(English_guys.basic_description)

# Тестирование класса исключений
text = str(sailors)

with open("KRAKEN.txt", mode="w") as file:
    try:
        raise SaveInfo("\nНе удалось сохранить информацию\n") # Вызываем исключение
        file.write(text)
    except SaveInfo as msg:
        print(msg)

# Тестирование функции - генератора
def random_ship(num):
    sailors_ship_list = ["Лодка", "Пиратское судно", "Военное судно", "Торговое судно"]
    sailors_armament_list = ["10 пушек", "25 пушек и 20 пиратов", "12 пушек и 30 солдат", "30 пиратов", "40 солдат",
                             "не повезло сегодня"]
    ships_list = []
    for i in range(num):
        ships_list.append([sailors_ship_list[random.randint(0,3)], sailors_armament_list[random.randint(0,5)], random.randint(0, 3001)])
    return ships_list

# Вывод получившихся данных
ships = random_ship(5)
for i in range(len(ships)):
    print(*ships[i], "(монет)")