
# write a function to relate the father son relationship which is provided in a dictionary, and output this in a list 

def ancestory(d:dict) -> list:
    li = []
    first_key, first_value = next(iter(d.items()))
    li = li + [first_key, first_value]
    for keys, values in d.items():
        if keys == li[-1]:
            li = li + [values]
        if values == li[0]:
            li = [keys] + li
    return li

P = {
    'Jahangir': 'Akbar',
    'Akbar': 'Humayun',
    'Humayun': 'Babur',
    'Babur' : 'Shubham',
    'Shubham' : 'Dilip'
}

print(ancestory(P))
