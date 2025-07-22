#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Letters/starting_letter.txt','r') as file:
    contents=file.read()

with open('Input/Names/invited_names.txt', 'r') as file:
    names = file.readlines()

PLACEHOLDER= '[name]'

for name in range(len(names)):
    name=names[name].strip()
    with open(f'Output/ReadyToSend/invited_{name}.txt', 'w') as file:
        final = contents.replace(PLACEHOLDER, f'{name}')
        file.write(final)


