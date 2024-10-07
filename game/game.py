import random

def get_choice(prompt, choices):
    while True:
        user = input(prompt).strip().lower()
        if user in choices:
            return choices[user]
        print("Неправильный ввод.")

def winner(player, computer):
    if player == computer:
        return "Ничья!"
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        return "ПОБЕДА!"
    else:
        return "Поражение!"

def game():
    choices = {"камень": 0, "ножницы": 1, "бумага": 2}
    choice_names = ["Камень", "Ножницы", "Бумага"]

    print("Игра:Камень-ножницы-бумага")
    while True:
        player_choice = get_choice("Сделайте свой ход(камень, ножницы, or бумага): ", choices)
        computer_choice = random.randint(0, 2)

        print("Ваш ход: " + choice_names[player_choice])
        print("Ход компьютера: " + choice_names[computer_choice])
        print(winner(player_choice, computer_choice))

        if input("Ещё? (да/нет): ").strip().lower() != 'да':
            break

game()