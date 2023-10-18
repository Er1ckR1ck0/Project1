from image_generation import print_image
from print_text import print_text
from config import start_image, forest_image, forest_image_thief, forest_run, win
from check import wrong_death, death_screen, win_screen, next_page
import time

#Start
def chapter_kingdom():
    print_image(start_image)    
    start_text = """
    > Ты как истинный давакине, ворвался в королевство, чтобы с помощью ведра украсть 
    у охраны деньги. Спасибо, что ты драконорождённый, а не Тодд Говард

    (шёпотом) Купи Skyrim!
    """
    for i in start_text:
        print(i, end="")
        time.sleep(0.01)
    next_page()
    return 1

def chapter_forest():
    print_image(forest_image)    
    strat_text_forest = """
    > Вдруг тебе в голову пришла идея срезать через лес. Ну вдруг на вора нарвёшься
    может быть тебе это нравится. 

    люблю молоко и огурцы — ремарка автора
    """
    for i in strat_text_forest:
        print(i, end="")
        time.sleep(0.01)
    next_page()
    return 2

def chapter_thief():
    print("\n"*60) #space generation
    strat_text_forest_thief = """
    > Как же неожиданно перед нами заспавнился вор! 
    -- как будто мы его и не ждали -- 

    я как сценарист, реально не ждал
    """
    for i in strat_text_forest_thief:
        print(i, end="")
        time.sleep(0.01)
    next_page()
    print("\n"*20) #space generation
    print_image(forest_image_thief)
    speech_thief = """
    — Кошлёк или жизнь?

    > Спросил тебя вор... Каковы же будут твои действия?
    """
    for i in speech_thief:
        print(i, end="")
        time.sleep(0.01)
        
    choose = """
    Варианты действий

    1. Сбежать
    2. Договорится
    """
    print(choose)
    enter_choose = input("> Напиши цифру варианта: ")
    if enter_choose.isdigit():
        if enter_choose == "1":
            return 2.1
        if enter_choose == "2":
            return 2.2
    else: chapter = wrong_death(enter_choose, 2)
    return chapter
def chapter_thief_run():
    print_image(forest_run)
    speech_thief = """
    — Стой! Стой! Стой!

    > Кричит тебе вор, что ты сделаешь
    """
    for i in speech_thief:
        print(i, end="")
        time.sleep(0.01)
        
    choose = """
    Варианты действий

    1. Бежать дальше
    2. Остановится
    """
    print(choose)
    enter_choose = input("> Напиши цифру варианта: ")
    if enter_choose.isdigit():
        if enter_choose == "1":
            return 'win_run'
        if enter_choose == "2":
            return death_screen(2.1)
    else: chapter = wrong_death(enter_choose, 2)
    return chapter

def speech_with_thief():
    print("\n"*35)
    speech_thief = """
    — Я не буду с тобой ни о чём договариваться! ДАВАЙ ДЕНЬГИ

    > Слушай, он настроен решительно, тут нужно что-то да предпринять
    """
    for i in speech_thief:
        print(i, end="")
        time.sleep(0.01)
    choose = """
    Варианты действий

    1. Убежать
    2. Начать драку
    3. Достать своего питона
    """
    print(choose)
    enter_choose = input("> Напиши цифру варианта: ")
    if enter_choose.isdigit():
        if enter_choose == "1":
            print("\n"*35)
            speech_thief = """
            > Вор понимал, что ты сбежишь и успел достать лук и ранить тебя в колено.
            > Про то, что тебя убили, говорить не буду...
            
            > Хотя...
            """
            for i in speech_thief:
                print(i, end="")
                time.sleep(0.01)
            return death_screen(2.2)
        if enter_choose == "2":
            print("\n"*35)
            speech_thief = """
            > У тебя в руке лишь ведро... Ты же с помощью него стражей обманывал
            
            > Забыл?
            
            > А под рукой меча не оказалось, как ты давакином стал не понятно...
            
            > КОРОЧЕ!
            """
            for i in speech_thief:
                print(i, end="")
                time.sleep(0.01)
            return death_screen(2.2)
        if enter_choose == "3":
            return 'win'
    else: chapter = wrong_death(enter_choose, 2)
    return chapter

def wining():
    print("\n"*35)
    speech_author = f"""
    > Ты вспонимаешь два важных факта
    
    > 1. Ты до сих пор держишь ведро в руках
    """
    
    for i in speech_author:
        print(i, end="")
        time.sleep(0.01)
    next_page()
    speech_author = """
    > 2. Ты обучаешься...
    """
    for i in speech_author:
        print(i, end="")
        time.sleep(0.2)
    print_image(win)
    speech_author = """
    > НА ЯНДЕКС ПРАКТИКУМЕ ПО НАПРАВЛЕНИЮ PYTHON РАЗРАБОТЧИК! 
    
    > ЧТО ТЕБЕ МЕШАЕТ НАПИСАТЬ БОТА, КОТОРЫЙ УБЬЕТ ТВОЕГО ПРОТИВНИКА ИЗ БЛАСТЕРА
    
    > ... ИЛИ УНИЗИТЬ ЕГО ТЕМ, ЧТО ОН ЛИШЬ ВОР, А ТЫ КВАЛИФИЦИРОВАННЫЙ СПЕЦИАЛИСТ
    
    >Но ты благородный давакин, поэтому просто даёшь ему ссылку на программу и вы
    вместе учитесь и получаете знания
    
    (СПУСТЯ 1 ГОД)
    
    — Давакин! Спасибо, что посоветовал курсы от Яндекс по Python. Я вот в Яндекс устроился, круто быть программистом
    — Ого, я тоже там работаю!
    — С меня кофе тогда)
    
    (наши два героя идут в офис Яндекс фиксить баги)
    """
    for i in speech_author:
        print(i, end="")
        time.sleep(0.01)
    next_page()
    win_screen()
def main():
    chapter = 0
    while True:
        match chapter:
            case 0: 
                print("\n"*100) #space generation
                print("> Это была обычная история о давакине (сорри не знаю, как правильно, я ленивый)")
                next_page()
                print("> Но тут случилось, что-то странное")
                print("\n"*4) #space generation
                chapter = chapter_kingdom()
            case 1: chapter = chapter_forest()
            case 2: chapter = chapter_thief()
            case 2.1: chapter = chapter_thief_run()
            case 'win_run': chapter = win_screen()
            case 2.2: chapter = speech_with_thief()
            case 'win': chapter = wining()
            case _: break 
    print("ПОКИ СПОКИ")
if __name__ == "__main__":
    main()