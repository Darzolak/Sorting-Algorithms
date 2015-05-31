import random, comparisons
from time import time, clock

a = []
COUNTER = comparisons.Counter()

def out(n,a):
    listx = []
    for i in range(1, n+1): listx.append(a[i])
    return listx

def sort(left,right,a):
    if left<right:
        m=partition(left,right,a)
        sort(left,m-1,a)
        sort(m+1,right,a)
        
def partition(left,right,a):
    x=a[left]
    i=left
    j=right+1
    while i<j:
        j=j-1
        if i==j: break
        while a[j]>=x:
            COUNTER.increment()
            j=j-1; 
            if i==j : 
                break
        if i==j: break
        COUNTER.increment()
        a[i]=a[j]
        i=i+1
        if i==j: break
        while a[i]<=x:
            COUNTER.increment()
            i=i+1; 
            if i==j:
                break
        if i==j: break
        COUNTER.increment()
        a[j]=a[i]
    
    a[i]=x
    return i

def main(a, n):
    sort(1, n,a); 
    return out(n,a), COUNTER

print(main([0, 36, 71, 14, 65, 49, 25, 92, 51, 9, 54, 17, 4, 83, 30, 78, 18], 16))
# {main program}
# n=int(input('input n '))
# a=[]
# for i in range(0,10000): a=a+[int(100*random.random())]
#
# t=clock();
# sort(1,n, a);
# print(out(n, a));
# print('time ',clock()-t)
#n=raw_input('finished ')
# main(a, n)