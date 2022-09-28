# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
rep = True
def repeat():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("sorry, only letters in the alphabet please!")
    else:
        print(output_list)
    finally:
        go_again = input("do you want to again (y or n)?")
        if go_again == "n":
            global rep
            rep = False
            print(rep)
        else:
            rep = True

while rep == True:
    repeat()


