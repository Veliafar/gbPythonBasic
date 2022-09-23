# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
#  Играют два игрока делая ход друг после друга. Первы
# й ход определяется жеребьёвкой. За один ход можно забрать не
#  более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать
#  все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

CANDIES_TOTAL = 2021


def set_players_names():
    player1, player2 = None, None

    while not player1:
        player1 = input("Имя игрока 1: ")
    while not player2:
        player2 = input("Имя игрока 2: ")
    return [player1, player2]


def grab_candies(player, candies_total):
    candies = -1
    while candies > 28 or candies < 1 or candies > candies_total:
        candies = input(f"{player} - сколько конфет вы берете (не более 28)?: ")        
        if not candies.isdigit() or candies.count("-") > 0:            
            candies = -1
            continue

        candies = int(candies)

    return candies


def grab_candies_game(candies_total):

    players = set_players_names()

    random.shuffle(players)

    current_player = None
    while candies_total > 0:
        current_player = players.pop(0)
        print("\n")
        print(f"Игрок {current_player} ходит")
        print(f"На столе {candies_total} конфет")
        grabed_candies = grab_candies(current_player, candies_total)
        candies_total -= grabed_candies
        print("\n")
        players.append(current_player)

    print(f"Победа за игроком: {current_player}")


grab_candies_game(CANDIES_TOTAL)
