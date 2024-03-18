# Prime number generator
def prime_generator(end, val):
    if val == 0:
        flag = True
    for n in range(2, end):     # n starts from 2 to end
        for x in range(2, n):   # check if x can be divided by n
            if n % x == 0:      # if true then n is not prime
                break
        else:                   # if x is found after exhausting all values of x
            if flag:
                flag = False
            else:
                flag = True
                yield n             # generate the prime


g = prime_generator(21, 0)       # give firt 1000 prime numbers
print(list(g)) 