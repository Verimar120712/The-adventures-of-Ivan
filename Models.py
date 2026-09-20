def check_positive(value, name):
    if value < 0:
        raise ValueError(f'{name} не может быть отрицательным, повторите еще раз')
    else:
        return value

class Character:
    """Основной класс, инициализирует персонажей
    Имеет а атрибуты name, max_hp, hp+, damage"""

    def __init__(self, name, max_hp, hp, damage):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.damage = damage
        

    def __str__(self):
        return f'Персонаж {self.name} имеет: \nМаксимальное здоровье: {self.max_hp} \nТекущее здоровье: {self.hp} \nУрон: {self.damage}.'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, max_hp={self.max_hp!r}, hp={self.hp!r}, damage={self.damage!r})'
            
    @property
    def max_hp(self):
        return self._max_hp
    @max_hp.setter
    def max_hp(self, new_max_hp):
        self._max_hp = check_positive(new_max_hp, 'Максимальное здоровье')
        if hasattr(self, '_hp') and self._hp > self._max_hp:
            self._hp = self._max_hp

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, new_hp):
        if new_hp > self._max_hp:
            self._hp = self._max_hp
        elif new_hp < 0:
            self._hp = 0
        else:
            self._hp = new_hp

    @property 
    def damage(self):
        return self._damage
    @damage.setter
    def damage(self, new_damage):
        self._damage = check_positive(new_damage, 'Урон')
        
    def attack(self, target):
        if self.hp > 0:
            target.hp -= self.damage
            return f'{target.name} получил {self.damage} урона и его здоровье составило {target.hp}'



class Player(Character):
    """ Класс игрока 
    Наследуется от Character
    Имеет метод eat увеличивающий здоровье при поедании еды"""

    def __init__(self, name, max_hp, hp, damage, food):
        super().__init__(name, max_hp, hp, damage)
        self.food = food

    def __str__(self):
        return f'{super().__str__()} \nЕду: {self._food}.'

    def __repr__(self):
        return f'Player(name={self.name!r}, max_hp={self.max_hp!r}, hp={self.hp!r}, damage={self.damage!r}, food={self._food!r})'

    @property
    def food(self):
        return self._food
    @food.setter
    def food(self, new_food):
        self._food = check_positive(new_food, 'Еда')

    def eat(self, food_item: 'FoodItem'):
        if self._hp < self._max_hp:
            if self.food > 0:
                self.hp += food_item.heal
                self.food -= 1
                return f'{self.name} съел {food_item.name} и увеличил свое здоровье на {food_item.heal} до {self.hp}.'
            else:
                return f'У {self.name} недостаточно {food_item.name}'
        else:
            return f'У {self.name} максимальное здоровье, еда не требуется!'    

class Enemy(Character):
    """Класс Врагов
    Наследуюется от Character
    Пока не имеет уникальных особнностей"""
    def __init__(self, name, max_hp, hp, damage):
        super().__init__(name, max_hp, hp, damage)



class FoodItem:
    """Класс еды
    Принимает название объекта еды (name) и количество восстанавливаемого здоровья (heal)"""
    def __init__(self, name, heal):
        self.name = name
        self.heal = heal

    def __str__(self):
        return f'Еда: {self.name} \nВосстанавливает здоровья: {self.heal}.'
    
    def __repr__(self):
        return f'FoodItem(name={self.name}, heal={self.heal})'
    

# character = Character('Кто-то', 100, 90, 30)
# print(character)

# ivan = Player('Ваня', 100, 70, 20, 0)   
# print(ivan)

# enemy = Enemy('Кабан', 80, 80, 25)
# print(enemy)

# while ivan.hp > 0 and enemy.hp > 0:
#     print(ivan.attack(enemy))
#     print(enemy.attack(ivan))