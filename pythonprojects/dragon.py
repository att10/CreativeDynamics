import matplotlib.pyplot as plt
import numpy as np

str = "U"
str2 = "U"
str3 = "U"
currentX = 0
currentY = 0
nextX = 0
nextY = 0
colors = ["black", "red"]

def rotate(str):
    result = ""
    for letter in str:
        if letter == "R":
            result = "U" + result
        elif letter == "U":
            result = "L" + result
        elif letter == "L":
            result = "D" + result
        else:
            result = "R" + result
    return result

def half(str):
    length_string = len(str)
    mid = round(length_string / 2)
    second_half = str[mid:].upper()
    return second_half

plt.show()

for i in range(20):
    for letter in str3:
        if letter == "R":
            nextX += 1
        elif letter == "U":
            nextY += 1
        elif letter == "L":
            nextX -= 1
        else:
            nextY -= 1
        plt.plot([currentX,nextX],[currentY,nextY], c=colors[i%2])
        plt.axis("equal")
        plt.pause(.01)
        currentX = nextX
        currentY = nextY
    str = rotate(str2)
    str2 += str
    str3 = half(str2)
