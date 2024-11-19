immutable_var = ('red', 'green', 1, True, [1, 2, 3, 4])
print( immutable_var)

#immutable_var[0] = 'blue'  элементы в кортеже нельзя изменять напрямую. Это неизменяемый тип данных

mutable_list = ['apple', 11, False]
print(mutable_list)
mutable_list.append(True)
mutable_list[1] = 777
print(mutable_list)