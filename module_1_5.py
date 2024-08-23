immutable_var = (5, 8, 'd', 'dog')
print(immutable_var)
immutable_var = ([7, 15], 'd', 'dog')
print(immutable_var)
immutable_var = (5, 8, 'd', 'dog') + (57, 'cat')
print(immutable_var)
immutable_var = (5, 8, 'd', 'dog') * 7
print(immutable_var)
immutable_var [1]
print(immutable_var)
immutable_var [2] = 485
print(immutable_var)

mutable_list = [25, 8, 'a', 'morning', 'friday']
print(mutable_list)
print(mutable_list[2])
mutable_list [2] = 'today'
print(mutable_list)
mutable_list.extend(['2025','summer'])
print(mutable_list)
mutable_list.remove(8)
print(mutable_list)
print('dog' in mutable_list)
print(5 not in mutable_list)