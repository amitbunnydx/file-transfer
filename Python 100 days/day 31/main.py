import pandas

with open('french.txt','r') as file:
    data=file.readlines()
print(data)
# li=[d for d in data]
data_f=pandas.DataFrame(data)

data_f=data_f.replace('\n','', regex=True)
data_f=data_f.replace('â€“','', regex=True)
data_f.columns = ['French']
print(data_f['French'])
data_f=data_f['French'].str.split(' ',n=1, expand=True)
data_f=data_f[1].str.split(' ',n=1, expand=True)
data_f.rename({0: 'French', 1: 'English'}, axis=1, inplace=True)
# print(data_f[0])



# print(f'column name is {data_f.columns}')
# print(list(data_f.columns))
print(data_f.head())
print(data_f.to_csv('test.csv'))