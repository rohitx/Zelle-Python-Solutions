'''Write a program that accepts two points and determines
the distance between them'''

import math


def main():
    x1 = input("Please enter value for point x1:")
    x2 = input("Please enter value for point x2:")
    y1 = input("Please enter value for point y1:")
    y2 = input("Please enter value for point y2:")
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print "The distance between two points is", distance

main()