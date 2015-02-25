'''Write a program to print the lyrics of the song Old MacDonald.
Your program should print the lyrics for five different animals,
similar to the example verse below.'''

def song(animal, a_sound):
    print "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"
    print "And on that farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!"
    print "With a " + a_sound + ", " + a_sound + " here and a " + a_sound + ", " + a_sound + " there."
    print "Here a " + a_sound + ", " + "there a "+ a_sound + ", everywhere a " + a_sound + ", " + a_sound + "."
    print "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"
    return ""

animals = ["cow", "pig", "horse", "chicken", "duck"]
sounds = ["moo", "snort", "neigh", "cluck", "quack"]

for i in range(len(animals)):
    print song(animals[i], sounds[i])
