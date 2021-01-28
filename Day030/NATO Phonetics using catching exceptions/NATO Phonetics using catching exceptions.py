
import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato)
nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}
#print(nato_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    print(word)
    try:
        ###Use try: in that line of code where the error will occur.
        output_list = [nato_dict[item] for item in word]
    except KeyError:
        print("\nSorry, Use letters please.")
        generate_phonetic()

    else:
        print(output_list)

generate_phonetic()