import math


def main():
    print "This program computes the cost per square inch of a circular\
           pizza, given its diameter and price."
    price = float(raw_input("Please enter the price: "))
    diameter = float(raw_input("Please enter the diameter: "))
    area = math.pi * (diameter/2.)**2
    cost = price / area
    print "The price per square-inch is: ${cost:.2f}".format(cost=cost)

main()