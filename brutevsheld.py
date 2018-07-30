__author__ = 'Chinmay Modi'

'''
This file is used to test performance of brute force algorithm vs held karp algorithm
It asks for number of cities, and number of iterations
Then, it generates that number of random iterations containing given number of cities
It runs each algorithm on all tours, and compares their times
Finally, brute force gives reasonable time till 11 city tours, and held karp works for upto 19 city tours
You are looking at 400 seconds for 12 city brute force run, and 80 seconds for 20 city held karp run
So be careful
'''

import time
import random
import sys
import copy
from reader import readup
from heldkarp import heldkarp
from bruteforce import brute
import statistics





def main():

    if (len(sys.argv)) == 1:
        lst, matrix = readup()
    else:
        lst, matrix = readup(sys.argv[1])

    print("Enter how many cities should the test run on:")
    city = int(input())
    print("Enter how many times each dataset should be tested:")
    test = int(input())

    brutet = 0.0
    heldt = 0.0
    a1 = []
    a2 = []
    t1=[]
    t2=[]


    print("Now testing all codes:")
    brttest = 0
    if city >= 10:
        print("This will cause large delay for brute force test, do you want to skip testing it? Enter 1 for yes, 2 for no:")
        brttest = int(input())

    for i in range(test):
        need = random.sample(range(1, 190), city)
        temp = copy.deepcopy(need)

        # print("Now starting test on following list:")
        # print(need)

        if brttest is 0 or brttest is 2:
            # print("Starting brute")
            start = time.clock()
            r1, r2 = brute(matrix, temp)
            end = time.clock()
            t1.append((end-start))
            brutet += (end - start)
            a1.append(r2)


        temp = copy.deepcopy(need)
        # print("Starting greedy")
        start = time.clock()
        r1, r2 = heldkarp(matrix, temp)
        end = time.clock()
        t2.append((end - start))
        heldt += (end - start)
        a2.append(r2)

        print("Test run number " + str(i) + " finished.")

    '''
    if brttest is 0 or brttest is 2:
        print(str(brutet), a1)
    print(str(greedyt), a2)
    print(str(nnt), a3)
    print(str(opt2t), a4)
    '''

    # In order, they are mean, standard deviation, min and max of each algo
    # t1 throuth t4 are the run times of each case.
    m1,m2 = 0,0
    max1,max2 = -1,-1
    min1,min2 = 999999,999999
    tm1,tm2 = 0,0
    maxtm1,maxtm2=-1,-1
    mintm1,mintm2 = 99,99

    for i in a2:
        if max2 < i:
            max2 = i
        if min2 > i:
            min2 = i
    for i in t2:
        if maxtm2 < i:
            maxtm2 = i
        if mintm2 > i:
            mintm2 = i
    m2 = statistics.mean(a2)
    tm2 = statistics.mean(t2)
    if brttest is 0 or brttest is 2:
        for i in a1:
            if max1 < i:
                max1 = i
            if min1 > i:
                min1 = i
        for i in t1:
            if maxtm1 < i:
                maxtm1 = i
            if mintm1 > i:
                mintm1 = i
        m1 = statistics.mean(a1)
        tm1 = statistics.mean(t1)


    print("Following are the statistics for each used function:")
    if brttest is 0 or brttest is 2:
        print("For brute force algorithm:")
        print("Average run time = " + str(tm1) + " sec. Max took " + str(maxtm1) + " and Min took " + str(mintm1) + " sec.")
        print("Average Path length = " + str(m1) + ". Max took " + str(max1) + " and Min took " + str(min1) + ".")

    print("For Held Karp algorithm:")
    print("Average run time = " + str(tm2) + " sec. Max took " + str(maxtm2) + " and Min took " + str(mintm2) + " sec.")
    print("Average Path length = " + str(m2) + ". Max took " + str(max2) + " and Min took " + str(min2) + ".")

if __name__ == "__main__":
    main()