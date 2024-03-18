#!/bin/python3

import sys
import os
import io
import re

# Complete the function below.
def subst(pattern, replace_str, string):
    #susbstitute pattern and return it
    match_obj = re.search(pattern, string)
    # print(match_obj.group())
    if(match_obj.group()):
        # string = string.replace(match_obj.group(), replace_str)
        string = re.sub(pattern, replace_str, string)
    # print(string)
    return string


def main():
    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            
    #Create pattern Implementation here 
    pattern = r"\bROAD\b"
    
    #Use subst function to replace 'ROAD' to 'RD.',Store as new_address
    new_address = []
    for sline in addr:
        new_address.append(subst(pattern, "RD.", sline))

    return new_address

'''For testing the code, no input is required'''

if __name__ == "__main__":
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    # res = main();
    # f.write(str(res) + "\n")
    # f.close()

    res = main()
    print(str(res))
