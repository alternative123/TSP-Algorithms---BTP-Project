__author__ = 'Chinmay Modi'

'''
Note: This is generating tsp tour from minimum spanning tree
We generate mst of the vertices of concern
Instead it straight away begins to find eulerian circuit
Due to this, it can guarantee path being at worse case, 2* optimal tour length
On the other hand, it almost always finds path that is atleast 1.7* optimal tour length
Implemented less for actual use, and more for understanding the concept
O(n^2 log2(n)) complexity
'''

import sys
from reader import readup
import copy
from collections import OrderedDict
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

    msttour(matrix, need)

def msttour(aa, b):
    mst=prim(aa, b)
    # print("MST is:")
    # print(mst)
    tt = []
    tt.append(b[0])
    latest = tt[len(tt) - 1]
    '''
    Here we implement a slight modification of creating a Eulerian Circuit
    We instead do a dfs on the tree with the starting tour as the root
    We add previously un-encountered nodes to our tour, and do not add nodes already in the tour
    '''
    while len(mst) > 0:
        z = 0
        for i in mst:
            if i[1] is latest:
                tt.append(i[2])
                z = 1
            elif i[2] is latest:
                tt.append(i[1])
                z = 1
            if z is 1:
                del mst[mst.index(i)]
                break
        if z is 1:
            latest = tt[len(tt) - 1]
        else:
            latest = tt[tt.index(latest) - 1]
    # print(tt)
    tt.append(b[0])
    dist = 0
    for i in range(len(tt) - 1):
        dist += aa[tt[i]][tt[i+1]]
    if __name__ == "__main__":
        print("Tour is:")
        print(tt)
        print("Length of tour: " + str(dist))
    else:
        return tt, dist

'''
Standard Prim's Algorithm for generating MST
Since prim has a single final tree from the beginning, cycle checking is as simple as
checking if both nodes of new edge are in the MST
'''
def prim(m, l):
    llen=len(l)
    wsort = []
    for i in l:
        for j in l:
            if i is not j:
                wt = m[i][j]
                if i < j:
                    x=[wt,i,j]
                else:
                    x=[wt,j,i]
                if x not in wsort:
                    wsort.append(x)
    wsort.sort(key=lambda x:x[0])
    # print(wsort)
    mstedges = []
    mst=[]
    mst.append(l[0])
    while len(mst) < llen-1:
        for i in wsort:
            if i[1] in mst and i[2] not in mst:
                mstedges.append(i)
                mst.append(i[2])
            elif i[2] in mst and i[1] not in mst:
                mstedges.append(i)
                mst.append(i[1])
    return mstedges


if __name__ == "__main__":
    main()