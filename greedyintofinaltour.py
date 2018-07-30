__author__ = 'Chinmay Modi'

'''
This is a simple implementation of Greedy into final tour meta-heuristic
We pass our list of nodes to greedy heuristic
Then, we take the tour it produces and pass it to final tour generator
That output is our final result
'''

import sys
from reader import readup
from finaltourgenerator import gentour
from greedy import greedy
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

    start = time.clock()

    grd2opt(matrix, need)
    print("Total time = " + str(time.clock() - start))

def grd2opt(matrix, need):
    a1, b = greedy(matrix, need)
    # We pop last element of list because it is the start node added at end for tour completion
    # finaltour generator will re-add it so no worries
    a1.pop()
    matrix[0][0] = 0
    tour, dist = gentour(matrix, a1)

    if __name__ == "__main__":
        print("Smallest tour is:")
        print(tour)
        print("Tour length is: " + str(dist))
    else:
        # print(tour)
        return tour, dist

if __name__ == "__main__":
    main()