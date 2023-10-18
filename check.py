from image_generation import print_image
from config import death

def check_input(enter_choose):
    while not enter_choose.isdigit():
        print("...\nдевочки я в шоке\n\nПопросилже ЦИФРУ")
        enter_choose = input("> Напиши цифру варианта: ")
    return enter_choose
def wrong_death(string, chapter):
    print("— Ха-ха-ха, ты реально играешь не по правилам, таких не любим. Прикончу я тебя \n(я же просил напиши цифру)")
    print("Ты умер!")
    print("1. Переиграть главу\n2. Переиграть игру с нуля\n3. Выход")
    enter_choose = check_input(input("> Напиши цифру варианта: "))
    if enter_choose == "1":
        return chapter
    if enter_choose == "2":
        return 0
    if enter_choose == "3":
        return -1
    
def death_screen(chapter):
    print_image(death)
    print("Ты умер!")
    print("1. Переиграть главу\n2. Переиграть игру с нуля\n3. Выход")
    enter_choose = check_input(input("> Напиши цифру варианта: "))
    if enter_choose == "1":
        return chapter
    if enter_choose == "2":
        return 0
    if enter_choose == "3":
        return -1
    
def win_screen():
    print("Ты выйграл!")
    print("1. Переиграть игру с нуля\n2. Выход")
    enter_choose = check_input(input("> Напиши цифру варианта: "))
    if enter_choose == "1":
        return 0
    if enter_choose == "2":
        return -1
    
def next_page():
    item = input('Нажми Enter для перехода: ')
    while item != "":
        item = input('Да просто нажми ENTER')
    return 