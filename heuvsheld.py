__author__ = 'Chinmay Modi'

'''
This program compares timing and length data for held karp solution vs other heuristics
The purpose is to test the accuracy and speed of the heuristics
Suggested size is 15 cities, 100 sample size
Do not run for more then 17 cities, or each sample run will take more then 10 seconds
The results are nicely displayed as
Time Taken || Average path size || Average of % difference per path
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
from heldkarp import heldkarp
from statistics import mean
from finaltourgenerator import gentour

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
    hldt = 0.0

    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a0 = []

    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []
    t0 = []

    for i in range(test):
        # 250 for densecenter
        # 300 for densestar
        # 600 for multicone
        # 200 for singlecone
        need = random.sample(range(2, 190), (city - 1))
        need.insert(0, 1)
        print("Now starting test on following list:")
        print(need)
        temp = copy.deepcopy(need)

        print("Now testing held karp")
        temp = copy.deepcopy(need)
        start = time.clock()
        r1, r2 = heldkarp(matrix, temp)
        end = time.clock()
        t0.append(end-start)
        greedyt += (end - start)
        a0.append(r2)

        print("Now testing nn")
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

        print("Now testing opt2")
        temp = copy.deepcopy(need)
        start = time.clock()
        r1, r2 = opt2(matrix, temp)
        end = time.clock()
        t3.append(end-start)
        opt2t += (end - start)
        a3.append(r2)

        print("Now testing grd2opt")
        temp = copy.deepcopy(need)
        start = time.clock()
        r1, r2 = grd2opt(matrix, temp)
        end = time.clock()
        t4.append(end-start)
        m2ot += (end - start)
        a4.append(r2)

        print("Now testing opt3")
        temp = copy.deepcopy(need)
        start = time.clock()
        r1, r2 = gentour(matrix, temp)
        end = time.clock()
        t5.append(end-start)
        mstt += (end - start)
        a5.append(r2)

        print("Test number " + str(i) + " has finished.")

    print("Average Time|||Average Distance|||% difference")
    print("Held Karp")
    print(str(mean(t0)) + " ||| " + str(mean(a0)) + " ||| 0")
    strata = []
    for i in range(test):
        strata.append(float(float(a2[i] - a0[i])/float(a0[i]))*100.0)
    print("Greedy")
    print(str(mean(t2)) + " ||| " + str(mean(a2)) + " ||| " + str(mean(strata)) + "%")
    strata = []
    for i in range(test):
        strata.append(float(float(a1[i] - a0[i])/float(a0[i]))*100.0)
    print("NN")
    print(str(mean(t1)) + " ||| " + str(mean(a1)) + " ||| " + str(mean(strata)) + "%")
    strata = []
    for i in range(test):
        strata.append(float(float(a3[i] - a0[i])/float(a0[i]))*100.0)
    print("Opt2")
    print(str(mean(t3)) + " ||| " + str(mean(a3)) + " ||| " + str(mean(strata)) + "%")
    strata = []
    for i in range(test):
        strata.append(float(float(a5[i] - a0[i])/float(a0[i]))*100.0)
    print("Gentour")
    print(str(mean(t5)) + " ||| " + str(mean(a5)) + " ||| " + str(mean(strata)) + "%")
    strata = []
    for i in range(test):
        strata.append(float(float(a4[i] - a0[i])/float(a0[i]))*100.0)
    print("Greedyintoopt2")
    print(str(mean(t4)) + " ||| " + str(mean(a4)) + " ||| " + str(mean(strata)) + "%")



if __name__ == "__main__":
    main()