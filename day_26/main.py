import pandas as pd

user_input = list(input("Type word: ").upper())
df = pd.read_csv('nato_phonetic_alphabet.csv')

dict_alphabet = {}
dict_list = []

for (index, row) in df.iterrows():
    dict_alphabet[row.letter] = row.code


for letter_iter in user_input:
    dict_list.append([phoneme for (latter, phoneme) in dict_alphabet.items() if latter == letter_iter])
print(f"Phonetic output is: {dict_list}")
