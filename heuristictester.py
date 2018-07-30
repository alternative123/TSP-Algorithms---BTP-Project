__author__ = 'Chinmay Modi'

'''
This program tests the performance of different heuristics compared to each other
Simply point it to a map, enter tour size, enter sampling size, and it will do the rest
'''

import time
import random
import sys
import copy
from reader import readup
from nn_tsp import nn_tsp
from greedy import greedy
from opt2 import opt2
from greedyIntoOpt2 import grd2opt
from msttour import msttour
from finaltourgenerator import gentour
from statistics import mean

def main():

    if (len(sys.argv)) == 1:
        lst, matrix = readup()
    else:
        lst, matrix = readup(sys.argv[1])
        print("Input file is " + str(sys.argv[1]))

    print("Enter how many cities should the test run on:")
    city = int(input())
    print("Enter how many times each dataset should be tested:")
    test = int(input())


    nnt = 0.0
    greedyt = 0.0
    opt2t = 0.0
    m2ot = 0.0
    mstt = 0.0
    gentt = 0.0

    # first item of list is number of times it won in distance
    # second item of list is number of times it won in time
    nnwin = [0,0]
    greedywin = [0,0]
    opt2win = [0,0]
    m2owin = [0,0]
    mstwin = [0,0]
    gentwin = [0, 0]

    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []

    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []
    t6 = []

    for i in range(test):
        # 250 for densecenter
        # 300 for densestar
        # 600 for multicone
        # 200 for singlecone
        # 100 for unknown map, change if needed
        mapsize = 131

        need = random.sample(range(2, mapsize + 1), (city - 1))
        need.insert(0, 1)
        print("Now starting test on following list:")
        print(need)
        temp = copy.deepcopy(need)

        '''        print("Now testing nn")
        start = time.clock()
        r1, r2 = nn_tsp(matrix, temp)
        end = time.clock()
        t1.append(end-start)
        nnt += (end - start)
        a1.append(r2)

        print("Now testing greedy")
        temp = copy.deepcopy(need)
        start = time.clock()
        r1, r2 = greedy(matrix, temp)
        end = time.clock()
        t2.append(end-start)
        greedyt += (end - start)
        a2.append(r2)
        '''

        print("Now testing opt2")
        temp = copy.deepcopy(need)
        start = time.clock()
        r1, r2 = opt2(matrix, temp)
        end = time.clock()
        t3.append(end-start)
        opt2t += (end - start)
        a3.append(r2)

        '''
        print("Now testing grd2opt")
        temp = copy.deepcopy(need)
        start = time.clock()
        r1, r2 = grd2opt(matrix, temp)
        end = time.clock()
        t4.append(end-start)
        m2ot += (end - start)
        a4.append(r2)'''


        '''print("Now testing msttour")
        temp = copy.deepcopy(need)
        start = time.clock()
        r1, r2 = msttour(matrix, temp)
        end = time.clock()
        t5.append(end-start)
        mstt += (end - start)
        a5.append(r2)'''

        print("Now testing Gen Tour")
        temp = copy.deepcopy(need)
        start = time.clock()
        r1, r2 = gentour(matrix, temp, 60)
        end = time.clock()
        t6.append(end-start)
        gentt += (end - start)
        a6.append(r2)

        print("Test number " + str(i) + " has finished.")


    print("test is: " + str(test))

    for i in range(test):
        print("i is: " + str(i))
        d = float("inf")
        ddata = 0
        t = float("inf")
        tdata = 0

        '''if a1[i] < d:
            d = a1[i]
            ddata = 1
        if a2[i] < d:
            d = a2[i]
            ddata = 2'''
        if a3[i] < d:
            d = a3[i]
            ddata = 3
        '''if a4[i] < d:
            d = a4[i]
            ddata = 4
        if a5[i] < d:
            d = a5[i]
            ddata = 5'''
        if a6[i] < d:
            d = a6[i]
            ddata = 6

        '''if t1[i] < t:
            t = t1[i]
            tdata = 1
        if t2[i] < t:
            t = t2[i]
            tdata = 2'''
        if t3[i] < t:
            t = t3[i]
            tdata = 3
        '''if t4[i] < t:
            t = t4[i]
            tdata = 4
        if t5[i] < t:
            t = t5[i]
            tdata = 5'''
        if t6[i] < t:
            t = t6[i]
            tdata = 6

        '''if ddata is 1:
            nnwin[0] += 1

        if ddata is 2:
            greedywin[0] += 1'''

        if ddata is 3:
            opt2win[0] += 1

        '''if ddata is 4:
            m2owin[0] += 1'''

        '''if ddata is 5:
            mstwin[0] += 1'''

        if ddata is 6:
            gentwin[0] += 1

        '''if tdata is 1:
            nnwin[1] += 1

        if tdata is 2:
            greedywin[1] += 1'''

        if tdata is 3:
            opt2win[1] += 1

        '''if tdata is 4:
            m2owin[1] += 1

        if tdata is 5:
            mstwin[1] += 1'''

        if tdata is 6:
            gentwin[1] += 1


    print("Here is data of running " + str(test) + " tests.")

    '''print("Nearest Neighbour heuristic got best distance and best time this many times:")
    print(str(nnwin[0]) + "||" + str(nnwin[1]))

    print("Greedy heuristic got best distance and best time this many times:")
    print(str(greedywin[0]) + "||" + str(greedywin[1]))'''

    print("Opt 2 heuristic got best distance and best time this many times:")
    print(str(opt2win[0]) + "||" + str(opt2win[1]))

    '''print("MST tour heuristic got best distance and best time this many times:")
    print(str(mstwin[0]) + "||" + str(mstwin[1]))'''

    '''print("Greedy into opt 2 heuristic got best distance and best time this many times:")
    print(str(m2owin[0]) + "||" + str(m2owin[1]))'''

    print("Gentour tour heuristic got best distance and best time this many times:")
    print(str(gentwin[0]) + "||" + str(gentwin[1]))
    print("Averagee dist: " + str(mean(a6)) + ", average time = " + str(mean(t6)))

    print(a3, t3)
    print(a6, t6)

if __name__ == "__main__":
    main()