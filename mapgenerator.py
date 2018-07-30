__author__ = 'Chinmay Modi'

'''
File used to generate all maps other than qatar
Modify as per need
'''

import random
import math

filename = 'densecenter'
f = open(filename, 'w')

f.write("1 0 0\n")
i = 2
pointlist=[]
while i < 200:
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    point = [x, y]
    if point not in pointlist:
        d = math.sqrt((x)**2 + (y)**2)
        if d < 50:
            f.write(str(i) + " " + str(x) + " " + str(y) + "\n")
            i += 1
            pointlist.append(point)


while i < 250:
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    point = [x, y]
    if point not in pointlist:
        dist = math.sqrt((x)**2 + (y)**2)
        if dist > 150:
            f.write(str(i) + " " + str(x) + " " + str(y) + "\n")
            i += 1
            pointlist.append(point)



print("Added 200 members to " + str(filename))
f.close()