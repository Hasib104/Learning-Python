
import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato)
nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}
#print(nato_dict)

word = input("Enter a word: ").upper()
output_list = [nato_dict[item] for item in word]
print(output_list)