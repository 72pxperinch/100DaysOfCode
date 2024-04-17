import os
PLACEHOLDER = "[name]"

script_dir = os.path.dirname(__file__)
invitedNames = os.path.join(script_dir, 'Input/Names/invited_names.txt')
startingLetter = os.path.join(script_dir, 'Input/Letters/starting_letter.txt')
output_directory = os.path.join(script_dir, 'Output/ReadyToSend/')  # New output directory

with open(invitedNames) as names_file:
    names = names_file.readlines()

with open(startingLetter) as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(os.path.join(output_directory, f"letter_for_{stripped_name}.txt"), mode="w") as completed_letter:
            completed_letter.write(new_letter)


