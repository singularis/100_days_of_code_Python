from art import logo
from random import randint


def input_checker(for_check):
    while for_check != "y" and for_check != "n":
        for_check = input("Wrong input 'y' or 'n': ")
    return for_check


def game(hard_level):
    if hard_level == "easy":
        move = 10
    else:
        move = 5
    game_objective = randint(0, 100)
    for i in range(move):
        print(i)
        print(f"You have {move - i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if i == (move - 1) and user_guess != game_objective:
            print(f"You lost, please try again. Answer was {game_objective}")
            break
        elif user_guess == game_objective:
            print(f"You got it! The answer was {game_objective}.")
        elif user_guess > game_objective:
            print("Too high.")
            print("Guess again.")
        elif user_guess < game_objective:
            print("Too low.")
            print("Guess again.")
        i -= 1


if __name__ == '__main__':
    new_game = "y"
    print(logo)
    while new_game == "y":
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        hard_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        game(hard_level)
        new_game = input_checker(input("Do you want to play a game of Day12? Type 'y' or 'n': "))
    print("Bye-Bye")
