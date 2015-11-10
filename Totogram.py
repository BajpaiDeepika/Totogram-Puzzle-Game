'''
# Approach:
# The approach used is basically a combination of branch and bound and local search.
# All the values of nodes from 1 to N are arranged in a sorted list called InitialFringe.Next we find the median value from the sorted list and make it the root of TotogramTree and remove from the InitialFringe . 
# Now the root always have three children.Hence will divide(branch) the remaining nodes into three sublists and will compare all the elements of each sublists with its parent node(local search).
# We will select the node from each sublist which will have the minimum absolute difference from its parent node
# Similarly for level3 we will have 6 modes and hence 6 sublists,12 for level 4,24 for level 5 ,48 for level6 and 96 for level 7 .
# We will keep on storing all the absolute minimum differences in a separate sublist call absmindiff
# Once we have the list having the arrangement of vertices as per BFS, we will print the maximum of absolute minimum difference as the max of absmindiff list
#(1) the best solution your code was able to find for-
K=3:
    Score:3
    Tile arrangement-6 3 5 8 1 2 4 7 9 10
    Time:0.000999927520752 seconds
K=4:
    Score:5
    Tile arrangement-12 7 11 16 3 6 10 13 17 20 1 2 4 5 8 9 14 15 18 19 21 22
    Time:0.000999927520752 seconds i.e less than 10ms
K=5:
    Score:9
    Tile arrangement-24 15 23 32 7 14 22 25 33 40 3 6 10 13 18 21 26 29 34 37 41 44 1 2 4 5 8 9 11 12 16 17 19 20 27 28 30 31 35 36 38 39 42 43 45 46
    Time:0.001 seconds i.e less than 10ms
K=6:
    Score:17
    Tile arrangement-48 31 47 64 15 30 46 49 65 80 7 14 22 29 38 45 50 57 66 73 81 88 3 6 10 13 18 21 25 28 34 37 41 44 51 54 58 61 67 70 74 77 82 85 89 92 1 2 4 5 8 9 11 12 16 17 19 20 23 24 26 27 32 33 35 36 39 40 42 43 52 53 55 56 59 60 62 63 68 69 71 72 75 76 78 79 83 84 86 87 90 91 93 94
    Time:0.0001 seconds i.e less than 10ms
K=7:
    Score:33
    Tile arrangement-96 63 95 128 31 62 94 97 129 160 15 30 46 61 78 93 98 113 130 145 161 176 7 14 22 29 38 45 53 60 70 77 85 92 99 106 114 121 131 138 146 153 162 169 177 184 3 6 10 13 18 21 25 28 34 37 41 44 49 52 56 59 66 69 73 76 81 84 88 91 100 103 107 110 115 118 122 125 132 135 139 142 147 150 154 157 163 166 170 173 178 181 185 188 1 2 4 5 8 9 11 12 16 17 19 20 23 24 26 27 32 33 35 36 39 40 42 43 47 48 50 51 54 55 57 58 64 65 67 68 71 72 74 75 79 80 82 83 86 87 89 90 101 102 104 105 108 109 111 112 116 117 119 120 123 124 126 127 133 134 136 137 140 141 143 144 148 149 151 152 155 156 158 159 164 165 167 168 171 172 174 175 179 180 182 183 186 187 189 190
    Time:0.00999999046326 seconds
#
 
'''
import math
import sys
from sys import argv
import time
start_time = time.time()
K = int(sys.argv[1])
#K=5
N=0                       # N is the total number of nodes in the tree
InitialFringe=[]          #InitialFringe is the initial sorted list of all numbers from 1 to N
TotogramTree=[]
absmindiff=[]

def TotoGram(K):       #K is the no of levels of tree
    N =1+(3*(2**(K-1)-1))
        #print("Number of nodes are ", N)
        #print ("Depth is ", K)
    for i in range(1,N+1):
        InitialFringe.append(i)
        i=i+1
        #print InitialFringe
    l1=len(InitialFringe)
    mid=l1/2
    root=InitialFringe[mid]
    TotogramTree.append(root)
    InitialFringe.remove(root)
        #level2 has three children always so divide the fringe in group of three
    if (InitialFringe!=[]):
        level2 =len(InitialFringe)/3
        data=list(sublists(InitialFringe,level2))
        last=len(TotogramTree)-1
        i=0
        while i<3:
            absdiff(data,i,InitialFringe,last,TotogramTree)
            i=i+1
        #level3 has six nodes always so divide the fringe in six groups
    if (InitialFringe!=[]):
        level3=len(InitialFringe)/6
        last1=len(TotogramTree)-3
        data1=list(sublists(InitialFringe,level3))
        increment=0
        i=0
        while i<6:
            if i in [2,4]:
                increment=increment+1
            absdiff(data1,i,InitialFringe,last1+increment,TotogramTree)
            i=i+1
    if (InitialFringe!=[]):
        #level4 has twelve nodes always so divide the fringe in twelve groups
        level4=len(InitialFringe)/12
        last2=len(TotogramTree)-6
        data2=list(sublists(InitialFringe,level4))
        increment=0
        i=0
        while i<12:
            if i in [2,4,6,8,10]:
                increment=increment+1
            absdiff(data2,i,InitialFringe,last2+increment,TotogramTree)
            i=i+1
    if (InitialFringe!=[]):
       #level5 has 24 nodes always so divide the fringe in 24 groups
        level5=len(InitialFringe)/24
        last3=len(TotogramTree)-12
        data3=list(sublists(InitialFringe,level5))
        i=0
        increment=0
        while i<24:
            if i in [2,4,6,8,10,12,14,16,18,20,22]:
                increment=increment+1
            absdiff(data3,i,InitialFringe,last3+increment,TotogramTree)
            i=i+1
    if (InitialFringe!=[]):
       #level6 has 48 nodes always so divide the fringe in 48 groups
        level6=len(InitialFringe)/48
        last4=len(TotogramTree)-24
        data4=list(sublists(InitialFringe,level6))
        i=0
        increment=0
        while i<48:
            if i in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46]:
                increment=increment+1
            absdiff(data4,i,InitialFringe,last4+increment,TotogramTree)
            i=i+1
        if (InitialFringe!=[]):
       #level7 has 96 nodes always so divide the fringe in 96 groups
            level7=len(InitialFringe)/96
            last5=len(TotogramTree)-48
            data5=list(sublists(InitialFringe,level7))
            i=0
            increment=0
            while i<96:
                if i in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96]:
                    increment=increment+1
                absdiff(data5,i,InitialFringe,last5+increment,TotogramTree)
                i=i+1
    #print("--- %s seconds ---" % (time.time() - start_time)) #This is to calculate time by stopping the timer.
    print max(absmindiff)
        
    sys.stdout.write(' '.join(map(str, TotogramTree)) )  #this is to print totogramtree without comma and bracket just space delimited arrangement
    
def absdiff(data,m,InitialFringe,last,TotogramTree):  
    diff=[]
    root=[]

    for i in range(0,len(data[m])):
        diff.append(abs(data[m][i]-TotogramTree[last]))
    root=data[m][diff.index(min(diff))]
    TotogramTree.append(root)
    InitialFringe.remove(root)
    absmindiff.append(min(diff))
    
def sublists(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

TotoGram(K)

