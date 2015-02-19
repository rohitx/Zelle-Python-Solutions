def main():
    print "Celsius          Fahrenheit"
    for celsius in range(0, 101, 10):
        fahrenheit = (9/5.) * celsius + 32
        print "{cel:1.2f} {fah:20.2f}".format(cel=celsius, fah=fahrenheit)
main()