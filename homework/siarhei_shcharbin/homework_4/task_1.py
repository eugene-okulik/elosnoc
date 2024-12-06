my_dict = {
    'tuple': (2, 4, 9, 15, 98),
    'list': [14, 2, 45, 14, 29],
    'dict': {1: 'yes', 2: 'no', 3: 'maybe', 4: 'def_yes', 5: 'def_no'},
    'set': {1, 23, 11, 23, 521.4}
}
print(my_dict['tuple'][-1])
my_dict['list'].append(19)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'it is not a typo'
my_dict['dict'].pop(3)
my_dict['set'].add('some text value')
my_dict['set'].remove(11)
print(my_dict)
