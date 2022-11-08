from art import logo
from random import randint

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
users_cards = []
dealer_cards = []
winner = False


def random_card_init():
    for _ in range(2):
        users_cards.append(cards[randint(0, len(cards) - 1)])
        dealer_cards.append(cards[randint(0, len(cards) - 1)])


def input_checker(for_check):
    while for_check != "y" and for_check != "n":
        for_check = input("Wrong input 'y' or 'n': ")
    return for_check


def winner_printer():
    print(f"Your final hand:: {users_cards}, final score: {sum(users_cards)}")
    print(f"Dealer final hand:: {dealer_cards}, final score: {sum(dealer_cards)}")


def appender(cards_list):
    rand_card = cards[randint(0, len(cards) - 1)]
    if sum(cards_list) == 20 and rand_card == 11:
        return 1
    else:
        return rand_card


def dealer_move():
    if sum(dealer_cards) < 17:
        dealer_cards.append(appender(dealer_cards))


def game_progress():
    print(f"Your cards: {users_cards}, current score: {sum(users_cards)}")
    print(f"Computer's first card: {users_cards[0]}")
    if sum(users_cards) > 21:
        winner_printer()
        print(f"You went over. You lose 😭")
    elif sum(dealer_cards) > 21:
        winner_printer()
        print(f"Opponent went over. You win 😁")
    elif sum(users_cards) == 21:
        winner_printer()
        print(f"21. You win 😁")
    elif sum(dealer_cards) == 21:
        winner_printer()
        print(f"21. Dealer win 😁")
    elif sum(users_cards) == 21 and sum(dealer_cards) == 21:
        print(f"Wow. Lets get new card 😁")
        users_cards.append(appender(users_cards))
        dealer_move()
        game_progress()
    else:
        next_card = input_checker(input("Type 'y' to get another card, type 'n' to pass: "))
        if next_card == "y":
            users_cards.append(appender(users_cards))
            dealer_move()
            game_progress()
        else:
            dealer_move()
            game_progress()


if __name__ == '__main__':
    new_game = "y"
    print(logo)
    while new_game == "y":
        # game init
        new_game = input_checker(input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
        users_cards = []
        dealer_cards = []
        random_card_init()
        game_progress()
    print("Bye-Bye")
