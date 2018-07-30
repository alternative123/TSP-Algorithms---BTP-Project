__author__ = 'Chinmay Modi'

'''
This is a simple implementation of Greedy into 2-opt meta-heuristic
We pass our list of nodes to greedy heuristic
Then, we take the tour it produces and pass it to 2-opt
Output of 2-opt is our final result
'''

import sys
from reader import readup
from opt2 import opt2
from greedy import greedy


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

    grd2opt(matrix, need)

def grd2opt(matrix, need):
    a1, b = greedy(matrix, need)
    # We pop last element of list because it is the start node added at end for tour completion
    # 2opt will re-add it so no worries
    a1.pop()
    matrix[0][0] = 0
    tour, dist = opt2(matrix, a1)
    # We make another pass with 2opt
    # It costs us double time, yes
    # But that increase is miniscule compared to run time of actual sorting algorithm, greedy in this case
    # And the tour does improve in the second pass
    # However, more then 2 passes in total will have no effect, so do not waste time
    print("First Pass tour length is: " + str(dist))
    tour.pop()
    tour, dist = opt2(matrix, tour)
    print("Second Pass tour length is: " + str(dist))
    tour.pop()
    tour, dist = opt2(matrix, tour)

    if __name__ == "__main__":
        print("Smallest tour is:")
        print(tour)
        print("Tour length is: " + str(dist))
    else:
        # print(tour)
        return tour, dist

if __name__ == "__main__":
    main()