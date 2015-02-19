import math
print "This program computes the square root of a number using the Newton method."


def main():
    value = input("Enter a value: ")
    number = input("Enter the number of times you wish to improve it: ")
    guess = value / 2.
    for i in range(number):
        guess = (guess + (value/guess))/2.
    print "The sqrt of {val:.2f} is: {guess:.5f}".format(val=value, guess=guess)
    compare = abs(math.sqrt(value) - guess)
    print "Here's how close they are: {comp:.6f}".format(comp=compare)
main()