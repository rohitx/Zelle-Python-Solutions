import math


def main():
    num = input("Please enter a number: ")
    total = 0
    for i in range(num):
        factor = (4. * (-1)**i) / (2 * i + 1)
        total += factor
    print "The total is: ", total
    acc = abs(math.pi - total)
    print "The accuracy of the approximation is: {acc:.6f}".format(acc=acc)

main()