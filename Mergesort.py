import random, comparisons
from time import time, clock

COUNTER = comparisons.Counter()

def out(n, a):
    data = []
    for i in range(1, n+1): 
        data.append(a[i])
    return data
    
def mergesort(p, q,a,b):
    if p < q :
        m = (p+q) // 2;
        mergesort(p, m,a,b);
        mergesort(m+1, q,a,b);
        merge(p, m+1, q+1,a,b)
# merge(p,m,q) merges array a from position p to m and position m+1 to q
def merge(p, r, q,a,b):
    i=p; j=r; k=p;
    while i < r and j < q :
        COUNTER.increment()
        if a[i] <= a[j]:
            b[k] = a[i]; i=i+1
        else : b[k] = a[j]; j=j+1
        k=k+1
    while i < r :
        b[k]= a[i]; i=i+1; k=k+1
    while j < q :
        b[k] = a[j];
        j=j+1; k=k+1;
    for k in range(p,q): a[k] = b[k]

def main(a, n):
    b = [0 for i in range(n+1)]
    mergesort(1, n, a,b)
    return out(n, a), COUNTER

print(main([0,1,2,3,4,6,5,7,8,9,10],10))
print(main([0,10,9,8,7,6,5,4,3,2,1],10))
#print(main([0, 43, 7, 67, 52, 78, 2, 53, 3, 96, 12, 22, 36], 12))
#print(main([0, 36, 71, 14, 65, 49, 25, 92, 51, 9, 54, 17, 4, 83, 30, 78, 18], 16))
# main program
#n=int(input('input n '))
#a=[]
#for i in range(0,20000): a=a+[int(100*random.random())]
#b=[]
#for i in range(0,20000): b=b+[0]
#t=clock()
#mergesort(1, n); out(n)
#print('time ',clock()-t, 'c=', c)
##n=raw_input('finished ')