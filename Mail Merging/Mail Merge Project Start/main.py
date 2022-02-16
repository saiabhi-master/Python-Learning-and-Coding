#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as file:
    # content_list = file.readlines()
    # print(content_list)
    new_list = []
    for i in file:
        new_list.append(i)


fily = open("./Input/Letters/starting_letter.txt")
content = fily.read()

names_list = []
for w in new_list:
    new_name = w.strip()
    names_list.append(new_name)
print(names_list)

for name in names_list:
    fele = open(f"./Output/ReadyToSend/{name}.txt", mode="w")
    x = content.replace("[name]", name)
    fele.write(x)


