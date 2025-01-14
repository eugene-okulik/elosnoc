PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_list = PRICE_LIST.split()
print(my_list)
my_items = [x for x in my_list if my_list.index(x) % 2 == 0]
my_prices = [int(x.rstrip('р')) for x in my_list if my_list.index(x) % 2 == 1]
print(my_items)
print(my_prices)
my_dict = dict(zip(my_items, my_prices))
print(my_dict)
