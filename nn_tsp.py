__author__ = 'Chinmay Modi'

'''
Example for nearest neighbour heuristic
Also known as the most naive form of the greedy algorithm
For an undirected graph that follows triangle inequality
It simply picks the latest member of the tour, and picks the shortest distance node not already in the tour
And adds it to the tour
Surprisingly, it performs well on come maps where there is no trick to adding members
e.g. tours that have nodes very close-by
Complexity is O(n^2)
'''

import sys
from reader import readup


def main():
    # List is the list of locations
    # matrix will store the distance data
    # both of them are read-1 and not read-0, which means [0] and [0][0]
    # will return 0, actual values start from [1]

    if(len(sys.argv)) == 1:
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



    need=[1, 72, 158, 29, 192, 33, 7, 113, 6, 42, 152, 62, 79, 61, 94, 21, 23, 132, 75, 71, 191, 30, 130, 217, 206, 138, 194, 197, 193, 22, 237, 81, 45, 216, 137, 91, 39, 41, 67, 199, 2, 183, 214, 63, 40, 101, 108, 143, 136, 32, 68, 236, 95, 66, 98, 242, 60, 139, 114, 178, 64, 171, 234, 27, 196, 57, 198, 153, 104, 115, 26, 97, 48, 44, 247, 93, 201, 124, 175, 120, 102, 240, 24, 110, 156, 166, 106, 241, 127, 90, 208, 182, 245, 148, 25, 122, 80, 209, 157, 49]
    nn_tsp(matrix, need)

# The call to nn_tsp is made with 2 params
# matrix of node distances, and list of nodes that need to be in the tsp
def nn_tsp(aa, b):
    totaldist = 0
    val = 0
    temp = []
    temp.append(b[0])
    del b[0]
    # print(temp)
    while 1 == 1:
        val = 0
        dist = 0
        if len(b) == 0:
            break
        u = int(temp[len(temp) - 1])
        maxdist = 999999
        lenu = len(aa[u])
        for i in range(0, lenu):
            if i != u and i in b:
                dist = aa[u][i]
                if dist < maxdist:
                    val = i
        # print(val)
        temp.append(val)
        b.remove(val)
        totaldist += dist
    temp.append(temp[0])
    totaldist = totaldist + aa[temp[-1]][temp[-2]]
    # print(temp)
    if __name__ == "__main__":
        print(temp)
        print(totaldist)
    else:
        return temp, totaldist


if __name__ == "__main__":
    main()
