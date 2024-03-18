#!/bin/python3

import math
import os
import random
import re
import sys

class Movie:
    def __init__(self, name_of_movie, num_of_tickets, total_cost):
        self.name_of_movie = name_of_movie
        self.num_of_tickets = num_of_tickets
        self.total_cost = total_cost
        
    def __str__(self):
        movie_str = f"Movie : {self.name_of_movie}\n"
        movie_str = movie_str + f"Number of Tickets : {self.num_of_tickets}\n"
        movie_str = movie_str + f"Total Cost : {self.total_cost}"
        return movie_str

if __name__ == '__main__':
    name = input()
    n = int(input().strip())
    cost = int(input().strip())
    
    p1 = Movie(name,n,cost)
    print(p1)