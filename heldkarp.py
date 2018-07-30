__author__ = 'Chinmay Modi'

'''
This is the implementation of Held Karp Algorithm, returning optimal tours
This is the most elegant algorithm out of all in this project
First we create two arrays of size 2^n  *  n
One of them is filled with distance data, second is used for last element
The property we follow is:
"Every subpath of a path of minimum distance is itself of minimum distance."
We employ bitmaps to exactly save path of the current array member
A good thing about python is that arrays are dynamic entities that do not use memory till
their members are actually initialized
So we are enabled to create a 1048576*20 array, and python will use no memory for the individual cells
till they are actually used
It has a O(2^n * n^2) time complexity, and a O(2^n * n) space complexity
For more details, refer to http://en.wikipedia.org/wiki/Held-Karp_algorithm
'''

import sys
import copy
from reader import readup
import itertools
import time


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

    '''
    for i in range(1, 6):
        for j in range(1, 6):
            print(matrix[i][j], end=" ")
        print("")
    '''

    '''
    for i in range(6):
        for j in range(6):
            print(matrix[i][j], end = " ")
        print("")
    '''
    tstart = time.clock()
    heldkarp(matrix, need)
    tend = time.clock()
    ttotal = tend - tstart
    if __name__ == "__main__":
        print("Time Taken in seconds: " + str(ttotal))

def heldkarp(aa, b):
    # print("Inside Held-Karp")
    n = len(b)
    bcopy = copy.deepcopy(b)
    g = [[0 for i in range(2**n)] for k in range(n)]
    p = [[0 for i in range(2**n)] for k in range(n)]
    # print(g)
    s = [i for i in range(1,n)]
    '''
    Permutations of size 1, which is the first loop of held karp
    Stores best distances from beginning node
    bitmaps are used to identify and separate different sets
    e.g set with list members 2,3,4 will have a bitmap of 4+8+16=28
    Thus keeping data unique
    '''
    a=itertools.permutations(s, 1)
    for x in a:
        x = list(x)
        bm=bitmap(x)
        # print(x)
        # print(bm)
        g[x[0]][bm] = aa[b[0]][b[x[0]]]
        p[x[0]][bm] = 0
        # print("Storing that cheapest value at [" + str(x[0]) + "," + str(bm) + "] came from edge starting at " + str(b[0]))
    '''
    for i in g:
        print(i)
    print("Above was distance, below is path matrix")
    for i in p:
        print(i)
    '''
    ranvar = 2
    '''
    Second loop-in-loop of held karp
    We imlement the following step:
    {C(S, k) = minm?1,m?k,m?S [C(S ? {k}, m) + dm,k ]}
    By using bitmaps and second matrix to store what path is optimal
    The second array helps us do a traceback at the end
    '''
    while ranvar < n:
        # print("ranvar is " + str(ranvar))
        a = itertools.combinations(s, ranvar)
        for x in a:
            x = list(x)
            bm1 = bitmap(x)
            # print(x)
            # print(bm1)
            mindist = float("inf")
            var = 0
            for i in range(0, len(x)):
                mindist = float("inf")
                k = x[i]
                bm2 = bm1 - (2**k)
                for j in range(0, len(x)):
                    if j is not i:
                        m = x[j]
                        dist = aa[b[m]][b[k]] + g[m][bm2]
                        if dist < mindist:
                            mindist = dist
                            var = m
                # print("Shortest path to " + str(k) + " is from " + str(b[var]))
                # print("Length is " + str(mindist))
                g[k][bm1] = mindist
                p[k][bm1] = var
                # print("Storing that cheapest value at [" + str(k) + "," + str(bm1) + "] came from edge starting at " + str(var))
        '''
        for i in g:
            print(i)
        print("Above was distance, below is path matrix")
        for i in p:
            print(i)
        '''
        ranvar += 1
    '''
    for i in g:
        print(i)
    print("Above was distance, below is path matrix")
    for i in p:
        print(i)
    '''


    '''
    Now we simply find bitmap of the entire set, and use it to find out minimum distance of the entire tour
    '''
    finaldist = float("inf")
    tour = [b[0]]
    finalbm = bitmap(s)
    finalhop = 0
    for i in range(1, n):
        dist = g[i][finalbm] + aa[b[0]][b[i]]
        if dist < finaldist:
            finaldist = dist
            finalhop = i
    # print("Cheapest value came from b member number" + str(finalhop))
    # print("Tour Length is " + str(finaldist))
    bm = finalbm
    # print("Total bitmap is " + str(bm))
    while len(tour) < len(b):
        # print("bitmap is " + str(bm))
        # print("Finalhop is " + str(finalhop))
        # print("Final step is " + str(b[finalhop]))
        tour.append(b[finalhop])
        x = finalhop
        finalhop = p[finalhop][bm]
        bm -= (2**x)
        # print("Step before it was at " + str(b[finalhop]))
    tour.append(b[0])
    # print("Final tour is:")
    # print(tour)
    if __name__ == "__main__":
        print("Tour is: ")
        print(tour)
        print("Length of tour = " + str(finaldist))
        print("Total memory in bytes used:")
        print("Memoization of path distances: " + str(sys.getsizeof(g)))
        print("Memoization of path data: " + str(sys.getsizeof(p)))
    else:
        return tour, finaldist



def bitmap(lst):
    ans = 0
    if type(lst) is not list:
        return 2**lst
    for i in lst:
        ans = ans + 2**i
    return ans



if __name__ == "__main__":
    main()