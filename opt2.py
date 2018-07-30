__author__ = 'Chinmay Modi'

'''
Our first tour-improvement heuristic, 2opt takes an existing tour and tries to improve upon it
It does so by inverting sections of the tour that reduce the total cost
Basically, exchange the nodes of two edges
Multiple run throughs of this program will not improve the tour
This implementation has a complexity of O(n^2 log2(n))
'''

import sys
import copy
from reader import readup


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

    opt2(matrix, need)


def opt2(aa, b):
    global tour
    global a
    global mtr
    global mindist
    tour = copy.deepcopy(b)
    mtr = copy.deepcopy(aa)
    a = tour.pop(0)
    mindist = 0
    # if __name__ == "__main__":
    #     random.shuffle(tour)
    for i in range((len(tour)) - 1):
        mindist += aa[tour[i]][tour[i+1]]
    tour.append(a)
    tour.insert(0, a)
    mindist = mindist + aa[a][tour[1]] + aa[a][tour[-2]]

    l = len(tour)

    i = 1
    while i < l - 1:
        k = 1
        while k < l - 1:
            if k is not i:
                if i < k:
                    optswap(i, k)
                else:
                    optswap(k, i)
            k += 1
        i += 1

    if __name__ == "__main__":
        print("Smallest tour is:")
        print(tour)
        print("Tour length is: " + str(mindist))
    else:
        # print(tour)
        return tour, mindist


def optswap(x, y):
    global tour
    global a
    global mtr
    global mindist
    '''
    print("Current tour is: ")
    print(tour)
    print("Current length is: " + str(mindist))
    print("Incoming request to swap at nodes ")
    print(x, y)
    '''
    newdist = mindist - (mtr[tour[x-1]][tour[x]] + mtr[tour[y]][tour[y+1]]) + (mtr[tour[x-1]][tour[y]] + mtr[tour[x]][tour[y+1]])
    '''
    print("We swapped following two edges for the next two edges")
    print("edge one is ")
    print(x-1, x)
    print(mtr[x-1][x])
    print("edge two is ")
    print(y, y+1)
    print(mtr[y][y+1])
    print("Edge three is ")
    print(x-1, y)
    print(mtr[x-1][y])
    print("Edge four is: ")
    print(x, y+1)
    print(mtr[x][y+1])
    print("Old tour had length " + str(mindist) + ", while new tour with 2-opting at positions (" + str(x) + ", " + str(y) + ") has length " + str(newdist))
    '''
    if newdist < mindist:
        tour[x:y+1] = reversed(tour[x:y+1])
        '''
        n1 = tour[:x]
        n2 = tour[x:y+1]
        n3 = tour[y+1:]
        n2.reverse()
        newlist=copy.deepcopy(n1)
        if len(n2) > 0:
            newlist.extend(n2)
        if len(n3) > 0:
            newlist.extend(n3)
        '''
        mindist = newdist
        # tour = copy.deepcopy(newlist)
        # print("optswap found that exchanging " + str(x) + " and " + str(y) + " lead to new tour with length " + str(mindist))
        # print(tour)



if __name__ == "__main__":
    main()
