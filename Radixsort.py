import random
from time import time, clock
#print(clock())

    
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
        
def FD(bucket_list,r, depth, length):

    sexy_thang = []
    for i in range (r):
        sexy_thang.append([])
    for elements in bucket_list:
        lsd = (elements//(r**depth))%r
        sexy_thang[lsd].append(elements)
    new_list = []
    for i in sexy_thang:
        new_list += i
    if depth < length:
        depth += 1
        new_list = FD(new_list,r, depth, length)
    return new_list

def main(array, r):
    new_array = []
    for i in array:
        new_array.append(i)
    length = (len(str(base_conversion(max(array),r))))
    bucket_list = FD(new_array,r, 0, length)
    return bucket_list

#t=clock()
#print(main([0, 22, 46, 27, 87, 19, 17, 87, 2, 40], 100))
#print('time ',clock()-t)
#t=clock()
#print(main([0, 22, 46, 27, 87, 19, 17, 87, 2, 40], 10))
#print('time ',clock()-t)
