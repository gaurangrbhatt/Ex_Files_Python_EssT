#!/usr/bin/env python3
# Use list comprehension to print Math tables


print()
print("List comprehension to print Math tables")
print()

def main():
    table = 4
    printMathTable(table, 11)
    
def printMathTable(n, r):
    print(f'Table of {n}')
    print('****************')
    seq = range(1, r)
    # print(f'Printing the seq :: {[x for x in seq]}')
    # seq2 = [x * n for x in seq]
    # print(f'Printing the seq2 :: {[x for x in seq2]}')
    for x in seq:
        print(f'{n} x {x} = {n*x}')
    print('****************')


if __name__ == '__main__': main()