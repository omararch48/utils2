from copy import deepcopy
from typing import List, Dict, Any


def normalize_list(
        input_dicts_list: List[Dict[str, Any]],
        keys_indicators: Dict[str, str]
    ) -> List[Dict[str, Any]]:




    data = deepcopy(input)


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



    return []