def main():
    temperature = 25
    for i in range(5):
        celsius = temperature + i
        fahrenheit = (9/5.) * celsius + 32
        print "The temperature is", fahrenheit, "degrees Fahrenheit."

main()