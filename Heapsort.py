import random, comparisons
from time import time, clock

COUNTER = comparisons.Counter()

def out(a, n):
    data = []
    for i in range(1, n+1): 
        data.insert(0,a[i])
    return data

def swap(i,j, a): # This swaps a[i] and a[j]
    w=a[i]; a[i]=a[j]; a[j]=w
    
def siftup(p, q, a, n):
    y=a[p]; j=p; k=2*p
    while k <= q:
        z=a[k]
        if k < q :
            COUNTER.increment()
            if z > a[k+1]:
                k=k+1
                z=a[k]
        COUNTER.increment()
        if y <= z : 
            break
        a[j]=z
        j=k
        k=2*j
        a[j]=y
        
def build_heap(n, a):
    for i in reversed(range(1,n//2+1)): siftup(i, n, a, n)
    
def sort(n, a):
    build_heap(n, a)
    for i in reversed(range(2,n+1)) :
        swap(1, i, a) # swap a[1] and a[i]
        siftup(1,i-1, a, n)
        # {main program}
    return i
    
def main(a, n):
    sort(n, a)
    return out(a, n), COUNTER
    
    
#print(main([0, 10, 77, 51, 56], 4))
#n=int(input('input n '))
#a=[]
#for i in range(0,10000): a=a+[int(100*random.random())]
#out(n); t=clock()
#sort(); out(n)
#print('time ',clock()-t)
#print('finished ')
##print(main(n))