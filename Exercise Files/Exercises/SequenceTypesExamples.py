#!/usr/bin/env python3
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print('Print list')

list_x = [1, 2, 3, 4, 5]

for i in list_x:
    print(i)
    
print()
print('Print tuple')
tuple_x = (1, 2, 3, 4, 5)

for  i in tuple_x:
    print(i)

print()    
print('Print range')

for i in range(7):
    print
    
print()
print('Print dictionary')

dict_x = {'one':1, 'two':2, 'three':3}
print(dict_x)
print()
print('Print dict by looping over it')

for i in dict_x:
    print(f'The value of i is dict_x[{i}]')
print()
for k, v in dict_x.items():
    print(f'The key is {k} and value is {v}')
print()
dict_x['two'] = 2222222

value_of_element = dict_x.get('two')
print(f'value of dict_x["two"] is {value_of_element}')

for k, v in dict_x.items():
    print(f'The value of dict_x[{k}] is {v}')
    
print()
print('Print keys of dict_x')
print(dict_x.keys())

print()
print('Print values of dict_x')
print(dict_x.values())

print()
print('Print key-value pairs of dict_x')
print(dict_x.items())

print()
print('Print using str() method ' + str(dict_x))
print('Print using normal method {}'.format(dict_x))
print(f'Print using f String {dict_x}')

print()
print(f'Print single element using f String {dict_x["two"]}')
print('Print single element using format method {}'.format(dict_x['two']))

