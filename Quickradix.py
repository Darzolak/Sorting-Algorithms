import random
from time import time, clock

bucket_list = []
sexy_thang = []
new_array = []
    
def base_conversion(num, r):
    if (num == 0):
        result = "0"
    else:
        quotient = num
        result = ""
        while quotient > 0:
            remainder = quotient % r
            result = str(remainder) + result
            quotient = quotient // r
    return int(result)
                     
def convert_back(listx, r):
    listy = []
    for element in listx:
        counter = 0
        element = str(element)[::-1]
        k = 0
        for j in element:
            k += (int(j) * (r ** counter))
            counter += 1
        listy.append(k)
    return listy
        
def FD(new_array, final, depth, r):
    if depth == -1:
        return new_array
    sexy_thang = [[] for i in range(r)]
    for elements in new_array:
        msd = (elements//int(str(1)+(str(0)*(depth))))%10
        sexy_thang[msd].append(elements)
    if depth >= 0:
        depth = depth - 1
        bucket_list = FD(sexy_thang[0], final, depth,r)
        bucket_list2 = FD(sexy_thang[1], final, depth, r)
        final = bucket_list + bucket_list2
    return final

def main(array):
    final = []
    r = 2
    bucket_list = [[] for i in range(r)]
    for i in array:
        new_array.append(base_conversion(i, r))     
    listx = FD(new_array,final, len(str(max(new_array)))+2, r)
    listy = convert_back(listx, r)
    return listy

    #return MD(new_array, array, bucket_list)
    #return LD()

#print(base_conversion(201, ))
#print([54, 32, 99, 70, 63, 61, 20, 97, 98, 34, 39, 71, 5, 67, 58, 52, 99, 98, 40, 15])
print(main([54, 32, 99, 70, 63, 61, 20, 97, 98, 34, 39, 71, 5, 67, 58, 52, 99,106, 98, 40, 15]))

#n=int(input('input n '))
#random_no=[]
#for i in range(0,10000): 
#random_no = random_no+[int(100*random.random())]
#t=clock();
#LSD(n)
#print(MSD(bucket_list))
#print('time ',clock()-t)
