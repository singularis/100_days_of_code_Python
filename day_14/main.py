# from replit import clear
# from art import logo
# from art import vs
from random import choice
from game_data import data

print(logo)


def random_element():
    return choice(data)


def printer(data):
    return ("{}, a {}, from {}".format(data["name"], data["description"],
                                       data["country"]))


def chouse_print(compare_a, compare_b):
    print("Compare A: {}".format(printer(compare_a)))
    print(vs)
    print("Compare B: {}".format(printer(compare_b)))
    if compare_a["follower_count"] > compare_b["follower_count"]:
        return "a"
    else:
        return "b"


def game(i):
    compare_a = random_element()
    compare_b = random_element()
    while compare_a == compare_b:
        compare_b = random_element()
    answer = chouse_print(compare_a, compare_b)
    user_guess_latter = input(
        "Who has more followers? Type 'A' or 'B': ").lower()
    while user_guess_latter == answer:
        clear()
        i += 1
        answer = chouse_print(compare_a, compare_b)
        user_guess_latter = input(
            "Who has more followers? Type 'A' or 'B': ").lower()
        if answer == "a":
            compare_a = compare_a
        else:
            compare_a = compare_b
        compare_b = random_element()
        while compare_a == compare_b:
            compare_b = random_element()
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {i}")


i = 0
game(i)
