

import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato)
nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}
#print(nato_dict)

word = input("Enter a word: ").upper()
output_list = [nato_dict[item] for item in word] #using list comprehension
# output_list = [] #using conventional loop
# for item in word:
#     output_list.append(nato_dict[item])
print(output_list)
