'''Write a program to calculate the area of the triangle given
the length of its three sides a, b, and c using these formulas

'''

import math


def main():
    a = input("Enter side a of the triangle: ")
    b = input("Enter side b of the triangle: ")
    c = input("Enter side c of the triangle: ")
    s = (a + b + c) / 2.
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print "The area of the triangle is: ", A






main()