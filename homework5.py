immutable_var = (1, 2.5, [3, 4, 5], 'кортеж', True)
print(immutable_var)

# Кортеж неизменяемая упорядоченная коллекция, которая может содержать в себе разные типы данных.
# Если изменить хоть один элемент, то столкнемся с ОШИБКОЙ.
# Однако если в кортеже присутствует тип "СПИСОК", то его можно изменить.
immutable_var[2][0] = 5
print(immutable_var)

mutable_list = [1, 2, 'кортеж', True]
print(mutable_list)
mutable_list[0] = 99
mutable_list[3] = False
print(mutable_list)
