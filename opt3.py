__author__ = 'Chinmay Modi'

'''
Our second tour-improvement heuristic, 3opt takes an existing tour and tries to improve upon it
It does so by inverting sections of the tour that reduce the total cost
It does so by swapping the nodes of upto 3 edges
'''

import sys
import copy
from reader import readup
import time
from opt2 import opt2

global compare6
compare6 = [0 for q in range(6)]

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
    temp1, temp2 = opt2(matrix, need)
    print("opt 2 result is: " + str(temp2))
    temp1.pop()
    opt3(matrix, temp1)


def opt3(aa, b):
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
    while i < l - 6:
        # print("Outmost loop " + str(i))
        j = i + 2
        while j < l - 4:
            k = j + 2
            while k < l - 2:
                if k is not i and i is not j and j is not k:
                    optswap(i, j, k)
                k += 1
            j += 1
        i += 1

    if __name__ == "__main__":
        print("Smallest tour is:")
        print(tour)
        print("Tour length is: " + str(mindist))
    else:
        # print(tour)
        return tour, mindist


def optswap(i, j, k):
    global tour
    global a
    global mtr
    global mindist
    global compare6

    '''
    print("Current tour is: ")
    print(tour)
    print("Current length is: " + str(mindist))
    print("Incoming request to swap at nodes ")
    print(i, j, k)
    print("Tour size is " + str(len(tour)))
    '''



    # dist[] is set of distances calculated by the 6 possibilities of 3 swap happening
    # We then choose the minimum and apply it
    dist = [0 for q in range(6)]
    dist[0] = mindist - (mtr[tour[i]][tour[i+1]] + mtr[tour[j]][tour[j+1]] + mtr[tour[k]][tour[k+1]]) + (mtr[tour[i]][tour[j+1]] + mtr[tour[k]][tour[j]] + mtr[tour[i+1]][tour[k+1]])
    dist[1] = mindist - (mtr[tour[i]][tour[i+1]] + mtr[tour[j]][tour[j+1]] + mtr[tour[k]][tour[k+1]]) + (mtr[tour[i]][tour[j]] + mtr[tour[i+1]][tour[k]] + mtr[tour[j+1]][tour[k+1]])
    dist[2] = mindist - (mtr[tour[i]][tour[i+1]] + mtr[tour[j]][tour[j+1]] + mtr[tour[k]][tour[k+1]]) + (mtr[tour[i]][tour[k]] + mtr[tour[j+1]][tour[i+1]] + mtr[tour[j]][tour[k+1]])
    dist[3] = mindist - (mtr[tour[i]][tour[i+1]] + mtr[tour[k]][tour[k+1]]) + (mtr[tour[i]][tour[k]] + mtr[tour[i+1]][tour[k+1]])
    dist[4] = mindist - (mtr[tour[i]][tour[i+1]] + mtr[tour[j]][tour[j+1]]) + (mtr[tour[i]][tour[j]] + mtr[tour[i+1]][tour[j+1]])
    dist[5] = mindist - (mtr[tour[j]][tour[j+1]] + mtr[tour[k]][tour[k+1]]) + (mtr[tour[j]][tour[k]] + mtr[tour[j+1]][tour[k+1]])
    newdist = mindist
    newindex = -1
    for q in range(6):
        if dist[q] < newdist:
            newdist = dist[q]
            newindex = q

    mindistindex = -1
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
        newtour = []
        '''
        print("I, J and K are: ")
        print(i, j, k)
        '''
        a = tour[:i]
        b = tour[i+2:j]
        bd = tour[i+2:j]
        bd.reverse()
        c = tour[j+2:k]
        cd = tour[j+2:k]
        cd.reverse()
        d = tour[k+2:]
        wtf3 = tour[i+2:k]
        wtf3.reverse()
        compare6[newindex] = compare6[newindex] + 1
        if newindex is 0:
            newtour = a+tour[i:i+1]+tour[j+1:j+2]+c+tour[k:k+1]+tour[j:j+1]+bd+tour[i+1:i+2]+tour[k+1:k+2]+d
            '''
            print("Step 0:")
            print(a)
            print(tour[i:i+1])
            print(tour[j+1:j+2])
            print(c)
            print(tour[k:k+1])
            print(tour[j:j+1])
            print(bd)
            print(tour[i+1:i+2])
            print(tour[k+1:k+2])
            print(d)
            '''
        elif newindex is 1:
            newtour = a+tour[i:i+1]+tour[j:j+1]+bd+tour[i+1:i+2]+tour[k:k+1]+cd+tour[j+1:j+2]+tour[k+1:k+2]+d
            '''
            print("Step 1 is:")
            print(a)
            print(tour[i:i+1])
            print(tour[j:j+1])
            print(bd)
            print(tour[i+1:i+2])
            print(tour[k:k+1])
            print(cd)
            print(tour[j+1:j+2])
            print(tour[k+1:k+2])
            print(d)
            '''
        elif newindex is 2:
            newtour = a+tour[i:i+1]+tour[k:k+1]+cd+tour[j+1:j+2]+tour[i+1:i+2]+b+tour[j:j+1]+tour[k+1:k+2]+d
        elif newindex is 3:
            newtour = a+tour[i:i+1]+tour[k:k+1]+wtf3+tour[i+1:i+2]+tour[k+1:k+2]+d
        elif newindex is 4:
            newtour = a+tour[i:i+1]+tour[j:j+1]+bd+tour[i+1:i+2]+tour[j+1:j+2]+tour[j+2:]
            '''
            print("Step 4:")
            print(a)
            print(tour[i:i+1])
            print(tour[j:j+1])
            print(bd)
            print(tour[i+1:i+2])
            print(tour[j+1:j+2])
            print(tour[j+2:])
            '''
        elif newindex is 5:
            newtour = a+tour[i:j]+tour[j:j+1]+tour[k:k+1]+cd+tour[j+1:j+2]+tour[k+1:k+2]+d

        '''
        print("Size of newtour is: " + str(len(newtour)) + ", and its length is " + str(newdist))
        print("Size of oldtour is: " + str(len(tour)) + ", and its length is " + str(mindist))
        print("Step number " + str(newindex) + " made the change.")
        print("New tour is:")
        print(newtour)
        print("Old tour is:")
        print(tour)
        print("Replacing old tour with new tour")
        '''
        tour=copy.deepcopy(newtour)
        mindist = newdist
        # time.sleep(1)
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
        # print(compare6)
        # time.sleep(1)
        # tour = copy.deepcopy(newlist)
        # print("optswap found that exchanging " + str(x) + " and " + str(y) + " lead to new tour with length " + str(mindist))
        # print(tour)



if __name__ == "__main__":
    main()
