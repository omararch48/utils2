from copy import deepcopy
from data.columns import columns
from data.data import data_to_excel


data = deepcopy(data_to_excel)
cols = deepcopy(columns)


for element in data:
    print('\n')
    for key, value in element.items():
        print(key, value)

for element in data:
    for key, value in element.items():
        if key in cols.keys():

            print(cols.get(key).get('length'))
            print(value)


            aux = deepcopy(value)

            while len(aux) < cols.get(key).get('length'):
                aux.append('')

            element.update({
                key: aux
            })

for element in data:
    print('\n')
    for key, value in element.items():
        print(key, value)