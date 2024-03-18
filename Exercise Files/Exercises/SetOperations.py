#!/usr/bin/env python3
# Set operations


print()
print("Program to perform set operations.")
print()

def main():
    set_fib = {1,1,2,3,5,8,13,21}
    set_prime = {1, 3, 5, 7, 11, 13, 17, 19, 23}
    # set_prime = {1,3,5,7,11,13,17,19,23}
    print('Print set of Fibonacci series')
    printSet(set_fib)
    print()
    print('Print set of Prime numbers')
    printSet(set_prime)

    # Union operation
    print()
    print('Union operation')
    printSet(set_fib | set_prime)
    print()

    # Intersection operation
    print()
    print('Intersection operation')
    printSet(set_fib & set_prime)
    print()

    # Difference operation
    print()
    print('Difference operation - In set_fib but not in set_prime')
    printSet(set_fib - set_prime)
    print()

    print()
    print('Difference operation - In set_prime but not in set_fib')
    printSet(set_prime - set_fib)
    print()

    # Symmetric Difference operation
    print()
    print('Symmetric Difference operation - opposite of intersection')
    printSet(set_fib ^ set_prime)
    print()

def printSet(o):
    print('{', end=' ')
    for i in o:
        print(i, end=' ')
    print('}', end=' ')
    print()

if __name__ == '__main__': main()