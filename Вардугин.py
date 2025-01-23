import random


def rock_paper_scissors():
    win = 0
    replay = 0
    player_thing = str(input("Выберите предмет ").lower())
    print(player_thing)
    while win != 1:
        if player_thing == "камень":
            bot_thing = random.randint(1, 3)
            if bot_thing == 1:
                print("Переиграть")
                rock_paper_scissors()
            if bot_thing == 2:
                print("Проигрыш, переиграть")
                rock_paper_scissors()
            if bot_thing == 3:
                print("Вы переиграли пилу! Но что же это? Почему он идет к вам с дубинк...")
                win = 1
        elif player_thing == "бумага":
            bot_thing = random.randint(1, 3)
            if bot_thing == 2:
                print("Переиграть")
                rock_paper_scissors()
            if bot_thing == 3:
                print("Проигрыш, переиграть")
                rock_paper_scissors()
            if bot_thing == 1:
                print("Вы переиграли пилу! Но что же это? Почему он идет к вам с дубинк...")
                win = 1
        elif player_thing == "ножницы":
            bot_thing = random.randint(1, 3)
            if bot_thing == 3:
                print("Переиграть")
                rock_paper_scissors()
            if bot_thing == 1:
                print("Проигрыш, переиграть")
                rock_paper_scissors()

            if bot_thing == 2:
                print("Вы переиграли пилу! Но что же это? Почему он идет к вам с дубинк...")
                win = 1


print("Здравствуйте! Вы попали к пиле на смертельные игры!")
print("Wanna play the game?")
input("да/нет ")
print("Вас никто не спрашивал...")
rock_paper_scissors()



