print "This program takes Celsius temperature as user \
        input and outputs temperature in Fahrenheit"
def main():
    celsius = input("What is the Celsius temperature?")
    fahrenheit = (9/5.) * celsius + 32
    print "The temperature is", fahrenheit, "degrees Fahrenheit."

main()