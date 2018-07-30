__author__ = 'Chinmay Modi'

'''
This is an implementation of the brute force algorithm for TSP
Time complexity is O(n!), so it is not very efficient
Takes about 40 seconds for an 11 member tour, so use carefully
'''

import itertools
import sys
from reader import readup
import copy
# import time

def main():
    if (len(sys.argv)) == 1:
        lst, matrix = readup()
    else:
        lst, matrix = readup(sys.argv[1])

    print("Enter numbers of the cities you wish to involve in the TSP:")
    n = int(input())
    print("Enter the city codes 1 per line, starting with your starting city")
    need = []
    for i in range(n):
        x = int(input())
        need.append(x)

    brute(matrix, need)


def brute(aa, b):
    # timer1 = time.clock()
    start = b[0]
    b.pop(0)
    # Here we generate permutations of the tour, which are n! in number
    a = itertools.permutations(b)
    mindist = -1
    tour = []
    # This loop takes the cheapest permutation and saves it as the tour
    for x in a:
        s = list(x)
        s.insert(0, start)
        s.append(start)
        # print(s)
        brake = 0
        dist = 0
        for i in range(len(s) - 1):
            # print("Adding edge between " +str(s[i])+ " and " + str(s[i+1]) + " with weight " + str(aa[s[i]][s[i+1]]))
            dist += aa[s[i]][s[i + 1]]
            if dist >= mindist > 0:
                brake = 1
                break
        # print(dist)
        '''if brake == 0:
            print("Tour is ")
            print(s)
            print("Length is:")
            print(str(dist))'''

        if brake == 0 and mindist == -1 or dist < mindist:
            mindist = dist
            tour = copy.deepcopy(s)

    # print(tour)
    # timer2 = time.clock()
    # timer = timer2 - timer1
    # print("That took " + str(timer) + " time.")
    if __name__ == "__main__":
        print("Smallest Tour is:")
        print(tour)
        print("It's Length is:")
        print(str(mindist))
    else:
        return tour, mindist


if __name__ == "__main__":
    main()
