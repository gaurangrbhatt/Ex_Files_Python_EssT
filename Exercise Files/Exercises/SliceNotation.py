def main():

    py='''
                    +---+---+---+---+---+---+
                    | P | y | t | h | o | n |
                    +---+---+---+---+---+---+
    Slice position: 0   1   2   3   4   5   6
                    +---+---+---+---+---+---+
            ->     -6  -5  -4  -3  -2  -1       Step +1
                    +---+---+---+---+---+---+
            <-         -6  -5  -4  -3  -2  -1   Step -1
                    +---+---+---+---+---+---+
    Index position:   0   1   2   3   4   5
                    +---+---+---+---+---+---+
    '''
    print(py, end="\n")
    print("a[start:stop:step] # start through not past stop, by step") # start through not past stop, by step
    print(py, end="\n")

    p=['p','y','t','h','o','n']
    print("p ", p)

    # a[start:stop]  # items start through stop-1
    print("p[0:2] ", p[0:2])
    
    # a[start:]      # items start through the rest of the array
    print("p[0:] ", p[0:])
    
    # a[:stop]       # items from the beginning through stop-1
    print("p[:2] ", p[:2])

    # a[:]           # a copy of the whole array
    print("p[:] ", p[:])

    '''
    The key point to remember is that the :stop value represents the first value that is not in the selected slice. 
    So, the difference between stop and start is the number of elements selected (if step is 1, the default).
    The other feature is that start or stop may be a negative number, which means it counts from the end of the array instead of the beginning. 
    So:

    '''

    # a[-1]    # last item in the array
    print("p[-1] ", p[-1])

    # a[-2:]   # last two items in the array
    print("p[-2:] ", p[-2:])

    # a[:-2]   # everything except the last two items
    print("p[:-2] ",p[:-2])
    print("p[-1:-2] ",p[-1:-2])
    print("p[-2:-1] ",p[-2:-1])

    # Answer should be letter o
    print("p[-1:-2:-1] ",p[-1:-2:-1])
    
    print("p[-2:-1:-1] ",p[-2:-1:-1])
    print("p[0:-1:-1] ",p[0:-1:-1])
    print("p[0:-1] ",p[0:-1])

    '''
    Similarly, step may be a negative number:
    '''

    # a[::-1]    # all items in the array, reversed
    print("p[::-1] ",p[::-1])
    
    # a[1::-1]   # the first two items, reversed
    print("p[1::-1] ",p[1::-1])
    
    # a[:-3:-1]  # the last two items, reversed
    print("p[:-3:-1] ",p[:-3:-1])

    # a[-3::-1]  # everything except the last two items, reversed
    print("p[-3::-1] ",p[-3::-1])
    
    '''

    Relation to slice() object

    The slicing operator [] is actually being used in the above code with a slice() object using the : notation (which is only valid within []), i.e.:

    a[start:stop:step] >> is equivalent to >> a[slice(start, stop, step)]

    Slice objects also behave slightly differently depending on the number of arguments, similarly to range(), i.e. both slice(stop) and slice(start, stop[, step]) are supported. To skip specifying a given argument, one might use None, so that e.g. a[start:] is equivalent to a[slice(start, None)] or a[::-1] is equivalent to a[slice(None, None, -1)].

    While the :-based notation is very helpful for simple slicing, the explicit use of slice() objects simplifies the programmatic generation of slicing.

    '''

    return None


if __name__ == "__main__":
    main()