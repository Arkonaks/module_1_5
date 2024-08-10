immutable_var = (123, True, 'apple')
print(immutable_var)
#immutable_var[0] = 321 #элемент кортеджа, который не является списком не изменяется
mutable_list = [1, 2, 3, 'apple', True]
mutable_list[0] = 2
mutable_list.append('banana')
mutable_list.extend([12, 13])
mutable_list.remove(True)
print(mutable_list)
