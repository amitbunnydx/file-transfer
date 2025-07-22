import pandas

nata_data=pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict={data.letter:data.code for index,data in nata_data.iterrows()}

input_name=input("please enter a word ").upper()
input_name=[name for name in input_name]
# print(input_name)
# nata_output=[j for i, j in nato_dict.items() if i in input_name]
# print(nata_output)
new_op=[ nato_dict[i] for i in input_name]
print(new_op)