import math


def sphereArea(radius):
    area = 4 * math.pi * radius**2
    return area


def sphereVolume(radius):
    volume = (4 / 3.) * math.pi * radius**2
    return volume

print sphereArea(5)
print sphereVolume(5)