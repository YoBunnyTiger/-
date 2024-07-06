my_dict = {'Kortney': 1986, 'Johnny': 1978, 'Megan': 1996}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Megan'))
print('Not existing value:', my_dict.get('Sasha'))
my_dict.update({'Peta': 1990,
                'Maximo': 1992})
a = my_dict.pop('Johnny')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print()

my_set = {1990, 1992, 'Kortney', 1990, 1992, 1992, True}
print('Set:', my_set)
my_set.update({(1, 2, 3), 'Megan'})
my_set.discard(1992)
print('Modified set:', my_set)
