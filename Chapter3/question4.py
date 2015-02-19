def main():
    print "This program computes the distance to the lightning strike\
           based on the time elapsed."
    time = input("Enter the time since flash and sound of thunder: ")
    distance = 1100 * time
    distance_in_mile = distance / 5280.
    print "The lightning strike occured at {dis:.2f}".format(dis=distance_in_mile), "miles."
main()