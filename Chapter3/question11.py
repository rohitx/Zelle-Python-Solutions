print "This program computes the sum of the first n natural numbers"
print ""


def main():
    num = input("Please enter the value n: ")
    total = 0
    for i in range(num+1):
        total += i
    print "The sum of first {n:d} natural numbers is: {total:d}".format(n=num, total=total)

main()