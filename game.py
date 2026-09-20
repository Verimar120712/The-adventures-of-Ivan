import models
from dialogs import dialogs_start_location, dialogs_text
import random
import os
import time

def is_valid(choice: str, destinations: list) -> bool:
    for text in destinations:
        if choice.lower().strip() == text.lower().strip() :
            return True
    return False

def pause(second):
    time.sleep(second)
    os.system("cls" if os.name == "nt" else "clear")

def start_game():
    '''Стартовая функция, запуск игры при положительном ответе'''

    while True:   
        choice = input(f'{dialogs_text['choice_text'][0]}?\n').lower().strip() 
        if is_valid(choice, dialogs_text['dialog_choice'][:-2]): # в списке dialog_choice элементы "да" и "нет" находятся в конце списка
            return True
        else:
            print(dialogs_text['invalid'])

def choice_level(level: list) -> int:
    '''Выбор сложности
    В функцию передается список сложностей, например: ['Легкий', 'Средний', 'Сложный']
    Результатом выполнения функции будет индекс выбранного пользователем элемента этого списка'''

    while True:
        level_choice = input(f'Ввведите уровень сложности {tuple(level)}\n').lower().strip()
        if is_valid(level_choice, level):
            return [text.lower() for text in level].index(level_choice) # приводим элементы переданного списка к одному регистру и находим индекс
        else:
            print(dialogs_text['invalid'])

def choce_player(quantity_destinations: int) -> str:
    '''Функция возвращает выбранное пользователем направление из доступных
    На текущий момент эта функция спаггети код и требует оптимизации'''

    destinations_text = dialogs_text['dialog_choise'][:quantity_destinations] # выбираем нужные варианты ответа из списка dialog_choise
    for text in dialogs_text['choice_text'][1:-1]: #зачем внутри функции запускать диалог??? Требует оптимизации
        print(text)
        time.sleep(1)
    while True:    
        print('Доступные направления:')
        for destinations in destinations_text:
            if destinations != dialogs_text['dialog_choise'][quantity_destinations - 1]:
                print(destinations, end='/')
            else:
                print(destinations)
        choice = input(f'{dialogs_text['choice_text'][2]}\n').lower()
        if is_valid(choice, destinations_text):
            return choice
        else:
            print(dialogs_text['invalid'])
            continue
        
def play_start_location():
    for text in dialogs_start_location['start_text']:
        print(text)               
        pause(1)

destinations = 3
# if not start_game():
#     print('Очень жаль! До встречи!')
# else:
#     play_start_location()
# print(choce_player(destinations))
level = choice_level()
print(level)
vanya = models.Player('Ваня', 100, 100, 20, 0)



# print(id(vanya))
# print(id(igor._damage))