#!/bin/python3

import math
import os
import random
import re
import sys

class comp:
    
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def add(self, cox):
        # print("----add----")
        # print(f"     {self.real}      {cox.real}")
        # print(f"     {self.imaginary}      {cox.imaginary}")
        c1 = complex(self.real, self.imaginary)
        c2 = complex(cox.real, cox.imaginary)
        c3 = complex(c1 + c2)
        # print(c3)
        add_str = f"{c3}"
        if(c3.real == 0):
            add_str = "0+" + add_str
        add_str = add_str.replace('(','')
        add_str = add_str.replace(')','')
        add_str = add_str.replace('j','i')
        print(f"Sum of the two Complex numbers :{add_str}")
        
    def sub(self, cox):
        c1 = complex(self.real, self.imaginary)
        c2 = complex(cox.real, cox.imaginary)
        c3 = complex(c1 - c2)
        # print(c3)
        sub_str = f"{c3}"
        if(c3.real == 0):
            sub_str = "0+" + sub_str
        sub_str = sub_str.replace('(','')
        sub_str = sub_str.replace(')','')
        sub_str = sub_str.replace('j','i')
        print(f"Subtraction of the two Complex numbers :{sub_str}")
#
#Write your code here

if __name__ == '__main__':
    
    real1 = int(input().strip())
    img1 = int(input().strip())
    
    real2 = int(input().strip())
    img2 = int(input().strip())
    
    p1 = comp(real1,img1)
    p2 = comp(real2,img2)

    p1.add(p2)
    p1.sub(p2)
