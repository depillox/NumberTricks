#numberTricks.py
# Adapted from https://www.thoughtco.com/math-tricks-that-will-blow-your-mind-4154742
from lib2to3.fixer_util import Number

def test():
    print("Hello from test")
    
import random
def trick02():
    '''
    Think of a number.
    Multiply it by 3.
    Add 6.
    Divide this number by 3.
    Subtract the number from Step 1 from the answer in Step 4.
    The answer is 2.
    '''
    number = random.randint(12345,54321)
    step1 = number
    number = number * 3
    number = number + 6
    number = number / 3
    number = number - step1
    print("Started with", step1, "ended with", number)
    
def trick03():
    '''
    Think of any three-digit number in which each of the digits is the same. Examples include 333, 666, 777, and 999.
    Add up the digits.
    Divide the three-digit number by the answer in Step 2.
    The answer is 37.
    '''
    number = 777 
    step1 = number
    digit1 = str(number)[0] #gives me the first digit
    digit2 = str(number)[1] #second digit
    digit3 = str(number)[2] #third digit
    temp = int(digit1) + int(digit2) + int(digit3)
    number = step1 / temp
    print("Started with", step1, "ended with", number)
