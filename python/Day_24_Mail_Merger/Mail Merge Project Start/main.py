#TODO: Create a letter using starting_letter.txt
import os
script_dir = os.path.dirname(__file__)
file_path_letter = os.path.join(script_dir, "./Input/Letters/starting_letter.txt")
with open(file_path_letter, "r") as file:
    letter_template = file.read()
file_path_names = os.path.join(script_dir, "./Input/Names/invited_names.txt")
with open(file_path_names, "r") as file:
    names = file.read()
for name in names.split("\n"):
    file_path_write = os.path.join(script_dir, f"./Output/ReadyToSend/letter_to_{name}.txt")
    content = letter_template.replace("[name]", name.strip())
    with open(file_path_write, "w") as file:
        file.write(content)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
