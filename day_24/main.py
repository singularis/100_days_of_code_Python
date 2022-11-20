PLACE_HOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    with open("./Input/Letters/starting_letter.txt") as starting_letter:
        text = starting_letter.read()
    for name in names:
        name = name.strip()
        replaced_text = text.replace("PLACE_HOLDER", name)
        file_name = "./Output/ReadyToSend/letter_for_" + name
        with open(file_name, mode="w") as ready_to_send:
            ready_to_send.write(replaced_text)

