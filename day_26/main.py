import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

dict_alphabet = {}
dict_list = []

for (index, row) in df.iterrows():
    dict_alphabet[row.letter] = row.code


def translator(user_input):
    for letter_iter in user_input:
        dict_list.append([phoneme for (latter, phoneme) in dict_alphabet.items() if latter == letter_iter])
    print(f"Phonetic output is: {dict_list}")


is_valid = False
while not is_valid:
    user_input = list(input("Type word: ").upper())
    try:
        if user_input not in dict_alphabet.values():
            raise ValueError("Wrong input")
        else:
            is_valid = True
            translator(user_input)
    except ValueError:
        print("Only latters")
