__author__ = 'Chinmay Modi'

'''
Example of Greedy algorithm
Choose cheapest edges that don't form a cycle OR increase degree of a node above 2
Find n such edges where n == |nodes| - 1
That is our greedy tour
Time complexity is about O(n^2 log2(n))
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

    greedy(matrix, need)


# The call to nn_tsp is made with 3 params
# matrix of node distances, and list of nodes that need to be in the tsp
def greedy(aa, b):
    # print("In greedy, need list is:")
    # print(b)
    nodes = [{i: 0} for i in b]
    # print(nodes)
    edges = []

    bcopy = copy.deepcopy(b)
    # print("bcopy is:")
    # print(bcopy)
    lenbcopy = len(bcopy)

    for i in bcopy:
        for j in bcopy:
            if j != i:
                s = bcopy.index(i)
                r = bcopy.index(j)
                nodes[s].update({j: aa[i][j]})
                temp = [i, j, aa[i][j]]
                temp2 = [j, i, aa[i][j]]
                if temp2 not in edges:
                    edges.append(temp)
                # edges.append(temp2)
                nodes[r].update({i: aa[j][i]})
    # print(nodes)
    # print(edges)

    edges.sort(key=lambda x: x[2])
    # print(edges)

    '''
    for i in range(len(nodes)):
        nodes[i] = OrderedDict(sorted(nodes[i].items(), key=lambda x: x[1]))
    '''
    # print(nodes)

    tempnode = []
    tempdegree = [0 for x in range(len(aa))]
    # print(tempdegree)
    numedge = 0
    tempdist = 0
    # edgescopy = copy.deepcopy(edges)
    selectededge = []

    '''
    We create our list of edges here, adhering to the two conditions
    For that, we keep track of degree of every node, and check for cycle creation
    '''
    while numedge < lenbcopy - 1:
        if len(edges) == 0:
            break
        n1, n2, wt = edges.pop(0)
        # print(n1, n2, wt)
        if n1 != b[0] and n2 != b[0] and tempdegree[n1] < 2 and tempdegree[n2] < 2:
            # print(str(n1) + " + " + str(n2) + " with weight " + str(wt) + " could be added to final list.")
            t = [n1, n2]
            # print("Now going to check the edge:")
            # print(t)
            rtemp = checkcycle(n1, n2, tempnode, selectededge)
            if rtemp == 0:
                # print("OOps, this edge causes a cycle:")
                # print(t)
                continue
            # print(t)
            # print("ok, passed cycle check, now adding this edge.")
            selectededge.append(t)
            numedge += 1
            tempdist += wt
            tempdegree[n1] += 1
            # print("tempdegree of " + str(n1) + " is " + str(tempdegree[n1]))
            tempdegree[n2] += 1
            # print("tempdegree of " + str(n2) + " is " + str(tempdegree[n2]))
            if n1 not in tempnode:
                if tempdegree[n1] < 2:
                    tempnode.append(n1)
            if n2 not in tempnode:
                if tempdegree[n2] < 2:
                    tempnode.append(n2)
    # print("ended loop, selected edges are:")
    # print(selectededge)

    # time.sleep(10)
    mindist = -1
    selnode = 0
    r = bcopy[0]
    for i in tempnode:
        if tempdegree[i] == 1:
            if mindist == -1:
                mindist = aa[r][i]
                selnode = i
            elif mindist > aa[r][i]:
                mindist = aa[r][i]
                selnode = i
    # print("Selected node is " + str(i) + ", with distance " + str(mindist))

    # tempnode.append(r)
    # tempnode.insert(0, r)
    '''
    print("List of nodes in temp tour is:")
    print(tempnode)
    print("Length of temp tour is:")
    print(tempdist)
    print(selectededge)
    '''
    finaldist = tempdist
    tour = [r, selnode]
    # print(tour)
    '''
    We iterate through our list of edges, and add whatever node comes next
    '''
    while len(tour) < lenbcopy:
        # print("len tour is " + str(len(tour)) + ". len bcopy is: " + str(len(bcopy)))
        # print("aaa")
        # time.sleep(1)
        s = tour[len(tour) - 1]
        # print("Last element of tour is: " + str(s))
        for j in selectededge:
            # print("Trying to determine if following edge can be added")
            # print(j)
            if j[0] == s:
                tour.append(j[1])
                selectededge.remove(j)
                break
            elif j[1] == s:
                tour.append(j[0])
                selectededge.remove(j)
                break
    tour.append(r)
    finaldist += aa[tour[0]][tour[1]] + aa[tour[-1]][tour[-2]]
    # print(tour)
    if __name__ == "__main__":
        print("Final tour is: ")
        print(tour)
        print("Total distance is: {0:.2f}".format(finaldist))
    else:
        return tour, finaldist

'''
Function to check for cycles for any edge(a, b)
It iterates over list of edges inside the list so far, and makes a list of all reachable nodes
It starts list with 'a', and at the end, if the list contains 'b', then there is a cycle formed
Otherwise, we are good to go
'''
def checkcycle(n1, n2, nlist, elist):
    stemp = []
    e = copy.deepcopy(elist)
    # n = copy.deepcopy(nlist)

    '''
    print("n1 and n2 are")
    print(n1, n2)
    print("n and e are:")
    print(n)
    print(e)
    '''

    stemp.append(n1)
    # print("stemp before iterations is:")
    # print(stemp)
    star = 0
    while 1 == 1:
        # print("Inside 1==1")
        i = 0
        lene = len(e)
        while lene > 0:
            # time.sleep(1)
            if i == 0:
                star = lene
            # print("star is " + str(star))
            # print("i and len e are: " + str(i) + " " + str(len(e)))
            j = e[i]
            prus = 0
            # print("Edge we are checking is:")
            # print(j)
            # print("i = " + str(i))
            if j[0] in stemp and j[1] not in stemp:
                stemp.append(j[1])
                prus = 1
            elif j[1] in stemp and j[0] not in stemp:
                stemp.append(j[0])
                prus = 1
            if prus == 1:
                e.remove(j)
                lene -= 1
            # print("i and len e are: " + str(i) + " " + str(len(e)))
            i += 1
            if i >= lene:
                if star == lene:
                    break
                i = 0
            if n2 in stemp:
                break
        if n2 in stemp or star == lene or lene is 0:
            break
    # print("stemp after iterations is:")
    # print(stemp)
    if n2 in stemp:
        return 0
    else:
        return 1


if __name__ == "__main__":
    main()
