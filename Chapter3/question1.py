import math
print "This program computes the Volume and Surface of a sphere\
        for a user-specified radius."


def main():
    radius = float(raw_input("Please enter a radius: "))
    volume = (4/3.) * (math.pi * radius**3)
    surface = 4 * math.pi * radius**2
    print "The Volume is: ", volume
    print "The Surface is: ", surface

main()