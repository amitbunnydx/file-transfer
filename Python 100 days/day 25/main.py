# with open ('weather_data.csv','r') as file:
#     file=file.readlines()
#     print(file)
#
# import csv
# with open('weather_data.csv','r') as file:
#     data=csv.reader(file)
#     temperature=[]
#     for data in data:
#         temp=data[1]
#         if temp!='temp':
#             temperature.append(int(data[1]))
# print(temperature)
from weakref import finalize

import pandas
import math
# data=pandas.read_csv('weather_data.csv')
# print(data['temp'])
# dataa=data['temp'].to_list()
# print(sum(dataa)/len(dataa))
# print(data['temp'].max())
# print(data[data.temp==data.temp.max()])

# print(data[data.temp.max()])
# data=data.temp[data.day=='Monday'].to_list()
# print((data[0]*(9/5))+32)
# data_dict={
#     'student':['any','kjames','angela'],
#     'score':[76,45,89]
# }
# data=pandas.DataFrame(data_dict)
# print(data)
# data.to_csv('new_csv')

#--------------------find number to squirrel based on color
data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
cinnamon_squirrels_count=len(data['Primary Fur Color'][data['Primary Fur Color']=='Cinnamon'])
gray_squirrels_count=len(data['Primary Fur Color'][data['Primary Fur Color']=='Gray'])
black_squirrels_count=len(data['Primary Fur Color'][data['Primary Fur Color']=='Black'])

print(data['Primary Fur Color'])
print(gray_squirrels_count)

data=data['Primary Fur Color'].dropna()

# data=data.unique()
new_data=data.to_list()
new_data=set(new_data)
new_data=list(new_data)
print(new_data)

data_dict={
    'Fur Color':new_data,
    'count':[cinnamon_squirrels_count,gray_squirrels_count,black_squirrels_count]
}
print(data_dict)

final=pandas.DataFrame(data_dict)
final.to_csv('final_data.csv')


# cinnamon=0
# # for i in data.unique():
# #     print(i)
# gray=0
# black=0
#
# for value in new_data:
#     if value=='Gray':
#         gray+=1
#     elif value=='Cinnamon':
#         cinnamon+=1
#     elif value=='Black':
#         black+=1
# print(f'cinnamon ={cinnamon} gray ={gray} black ={black}')
#
# dict=dict(zip(data.unique(),[cinnamon,gray,black]))
# fur_color=[]
# count=[]
# for i,j  in dict.items():
#     fur_color.append(i)
#     count.append(j)
#
# dict={fur_color,count}
#
# print(dict)
# fin=pandas.DataFrame(dict)
#
# fin.to_csv('final dict.csv')

