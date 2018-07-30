__author__ = 'Chinmay Modi'

'''
This is the reader file
Prefer to keep all reader code here to reduce clutter
Simply import it as you need
It needs a command line argument, namely the path of the data file
'''

from math import sqrt

def readup(file = 'qatar'):
    t1 = [0]
    t2 = [0]
    t3 = [0]
    s = 0
    with open(file) as f:
        print(f)
        for line in f:
            l = line.split()
            #print(l)
            a,b,c =  int(l[0]), float(l[1]), float(l[2])
            #print(a, b, c)
            t1.append(a)
            t2.append(b)
            t3.append(c)
        s = len(t1)
        #print(s)
    ta = [[0 for i in range(s)] for i in range(s)]
    '''for i in range(s):
        print(ta[i])'''

    for i in range(1, s):
        for j in range(i+1, s):
            dist = sqrt((t2[i] - t2[j]) ** 2 + (t3[i] - t3[j]) ** 2)
            ta[i][j] = dist
            ta[j][i] = dist


    #print(ta[123][23])
    return t1, ta