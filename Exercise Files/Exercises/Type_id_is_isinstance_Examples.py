#!/usr/bin/env python3
# Operations using functions - type(), id(), isinstance()
# Operations using is operator

print('Print list')

list_x = (1, 2, 3, 4, 5)
print(str(list_x))
print(f'Type of list_x is {type(list_x)}')

print()
list_mix = [1, 'two', True, None, 23.45]
print(str(list_mix))
print('Print the types of individual elements')
print()
for i in list_mix:
    print(f'Type of element is {type(i)}')
    
# print()
# print('Printing elements of the tuple')
# for i in list_mix:
    # print(list_mix[i])
# TypeError: tuple indices must be integers or slices, not str

print()
print('Printing the id() of tuples')
list_mix_2 = (1, 'two', True, None, 23.45)
print(f'id of list_mix   {id(list_mix)}')
print(f'id of list_mix_2 {id(list_mix_2)}')

# Using the is operator in Python
print()
print('Comparison using the is operator in Python')
if list_mix is list_mix_2:
    print('list_mix and list_mix_2 are same')
else:
    print('list_mix and list_mix_2 are different')
    
# Using isinstance function in Python
print()
print('Using isinstance function in Python')
if isinstance(list_mix, tuple):
    print('list_mix is tuple')
elif isinstance(list_mix, list):
    print('list_mix is list')
elif isinstance(list_mix_2, tuple):
    print('list_mix_2 is tuple')
else:
    print('None')