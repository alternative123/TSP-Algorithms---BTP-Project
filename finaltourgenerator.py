__author__ = 'Chinmay Modi'

from opt2 import opt2
from opt3 import opt3
import time
import sys
from reader import readup
import copy

def main(lim = 0):
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
    print("Starting gentour")
    gentour(matrix, need, lim)


def gentour(matrix, need, timelimit = 0):



    start = time.clock()

    temp1, temp2 = opt2(matrix, need)
    mintour = copy.deepcopy(temp1)
    mindist = temp2
    now = time.clock()
    count = 0
    bin = 0
    if timelimit is 0:
        timelimit = 30000
    while((now - start) < timelimit):
        print("Still below timelimit")
        temp1.pop()
        if bin is 0:
            bin = 1
            temp1, temp2 = opt2(matrix, temp1)
            if temp2 < mindist:
                mindist = temp2
                mintour = copy.deepcopy(temp1)
                count = 0
            else:
                count = count + 1
        else:
            bin = 0
            temp1, temp2 = opt3(matrix, temp1)
            if temp2 < mindist:
                mindist = temp2
                mintour = copy.deepcopy(temp1)
                count = 0
            else:
                count = count + 1
        now = time.clock()
        if count > 1:
            break

    if __name__ == "__main__":
        print("Smallest tour is:")
        print(mintour)
        print("Tour length is: " + str(mindist))
        print("Total time is : " + str(now - start))
    else:
        # print(tour)
        return mintour, mindist


if __name__ == "__main__":
    main()