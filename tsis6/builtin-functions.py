#1
from functools import reduce

def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)

#2
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

#3
def is_palindrome(string):
    return string == string[::-1]

#4
import time
import math

def sqrt_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

#5
def all_true(t):
    return all(t)