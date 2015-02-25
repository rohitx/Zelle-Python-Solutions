'''
Write definitions for the following two functions:
sumN(n) returns the sum of the first n natural numbers.
sumNCubes(n) returns the sum of the cubes of the first n natural numbers.
Then use these functions in a program that prompts a user for n and prints out the sum of the first n natural
numbers and the sum of the cubes of the first n natural numbers.

'''

def sumN(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

def sumNCubes(n):
    total = 0
    for i in range(n+1):
        total += i**3
    return total

print "This program computes the sum and cubed sum of n numbers."
num = input("Please enter the number: ")

print sumN(num)
print sumNCubes(num)