#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 10:47:57 2018

@author: GhostGirl
"""

# Arithmetic
print(5/2)
print(5//2)

# Functions

def apply_to_one(f):
    return f(29)

def funcion(p):
    return p * 2

print(apply_to_one(funcion))
print(funcion(2))

def apply_to_one(f, p):
    return f(p)

print(apply_to_one(funcion, 15))

# Uso de parámatros por defecto
def apply_to(funcion, p = 2):
    return funcion(p)

print(apply_to(funcion))
print(apply_to(funcion, 5))

# Exceptions
try:
    print(0/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
    
# List, tuples, dictionaries and set

integer_list = [1,2,3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

x = list(range(10) )  # is the list [0,1, ..., 9]
# En Python 2.7 lo anterior era sin el uso de list
print(x)
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]

x[0] = -1

first_three = x[:3] # [-1,1.2]
print(first_three)
three_to_end = x[3:] # [3,4,5,6,7,8,9]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]
print(1 in [1,2,3])
print(0 in [1,2,3])

x = [1,2,3]
x.extend([4,5,6])

x = [1,2,3]
y = x + [4,5,6]    

x = [1,2,3]
x.append(0) # x is now [1,2,3,0]

y = x[-1]   # equals 0
z = len(x)  # equals 4

x, y = [1,2]    # now x is 1, y is 2
_, y = [1,2]    # now y is 2, didn't care about the first element

# Tuples : list immutable

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print("Cannot modify a tuple")

# Tuples in functions

def sum_and_product(x, y):
    return (x+y),(x*y)

sp = sum_and_product(2,3)
s, p = sum_and_product(5,10)

# Swap with Tuples
a, b = 1, 2
a, b = b, a

# Dictionaries
 
empty_dict = {}         # Pythonic
empty_dict2 = dict()    # less Pythonic

grades = {"Joel" : 80, "Tim" : 95}
joel_grade = grades["Joel"]

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("No grade for Kate!")
    
joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

# Method that return a default value
x_joel_has_grade = grades.get("Joel", 0)
x_kate_has_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No one")

grades["Tim"] = 90  # Replaces the old value
grades["Kate"] = 100    # Adds a third entry
num_students = len(grades)

tweet = {
        "user" : "joelgrus",
        "test" : "Data Science is awesome",
        "retweet_count": 100,
        "hashtag" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
        }
    
tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

print("user" in tweet_keys)     # True, but uses slow list in
print("user" in tweet)          # more Pythonic, uses faster dict in
print("joelgrus" in tweet_values)   # True

# defaultdict

document = ["silbato", "Peter", "Rabbit", "Game", "Of", "Thrones", "Star", "Wars", "Of"]
# First approach
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        
# Second approach
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1        
        
# Thrid approach
word_counts = {}
for word in document:
    previous_count = word_counts.get(word,0)
    word_counts[word] = previous_count + 1
    
# Now, use defaultdict
from collections import defaultdict
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1