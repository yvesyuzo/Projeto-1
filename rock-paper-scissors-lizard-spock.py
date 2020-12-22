from random import randint
import time

print ("Let's play rock, paper, scissor, lizard, spock!")
time.sleep (1)
print ("The first of us to win 3 times in a row is the winner!")
time.sleep (1)
reference = 1
#variavel para controlar o primeiro 'while' rock = 10 paper = 20 scissor = 30 lizard = 40 spock = 50

while reference == 1:
    name = str(input("What's your name? "))
    score_player = 0
    score_comp = 0
    valores = {"rock":10, "paper":20, "scissors":30, "lizard":40, "spock":50}
    valores_comp = {1:"rock", 2:"paper", 3:"scissors", 4:"lizard", 5:"spock"}

    palavras = {51:"vaporizes",41:"smashes",    31:"smashes",    21:"covers",   12:"covers",
                52:"disproves",42:"eats",       32:"cuts",       23:"cuts",     13:"smashes",
                53:"smashes",  43:"decapitates",34:"decapitates",24:"eats",     14:"crushes",
                54:"poisons",  45:"poisons",    35:"smashes",    25:"disproves",15:"vaporizes"}
          # dicionario para relacionar as combinações de jogadas com as ações correspondentes
    while score_player <= 2 or score_comp <= 2:
        number = randint(1,5)
        player_move = input(name + " choose your move: ")

        while player_move not in valores.keys():
            player_move = input("I think you have tipped an invalid word, please choose one of the accepted moves (rock, paper, scissors, lizard, spock):  ")
        resultado = valores[player_move] + number
        if resultado in [11, 22, 33, 44, 55]:
                print("It's a draw! Both of us have choosen", player_move)
                score_player = 0
                score_comp = 0
        elif resultado in [13, 14, 21, 25, 32, 34, 42, 45, 51, 53]:
                print(player_move, palavras[resultado], valores_comp[number], "you won this round!")
                score_player += 1
                score_comp = 0
        elif resultado in [12, 15, 23, 24, 31, 35, 41, 43, 52, 54]:
                print(valores_comp[number], palavras[resultado], player_move, "you lost this round!")
                score_comp += 1
                score_player = 0

        if score_player == 3:
                print("Congratulations", name, "you have won!")
        if score_comp == 3:
                print("I'm sorry", name, "you are not smart enough for me")
        if score_player == 3 or score_comp == 3:
                reference = int(input("Press 1 to play again or 2 to stop"))
                score_player = 0
                score_comp = 0
