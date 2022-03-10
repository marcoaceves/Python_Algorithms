# shuffle

from random import random
import random

def shuffle(arr):
    for i in range(len(arr)):
        j =  random.randint(0,len(arr)-1)
        temp= arr[i]
        arr[i] = arr[j]
        arr[j]= temp
    print(arr)
    return arr

shuffle([1,2,3,4,5])


# skyline heights

def skyline(arr):
    can_see = []
    x=0
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] > x:
            can_see.append(arr[i])
            x = arr[i]
    return can_see
print(skyline([-1,1,1,7,3,9]))


# zip it
def zipit(arr,arr2):
    new_arr = []
    temp =arr[0]
    high = 0

    temp1=0
    for i in range(len(arr)):
        if arr[i] > high:
            high = arr[i]
    for i in range(len(arr2)):
        if arr2[i] > high:
            high = arr2[i]

    low=high

    for i in range(len(arr)):
        if arr[i] < low:
            low = arr[i]
    for i in range(len(arr2)):
        if arr2[i] < low:
            low = arr2[i]
    new_arr.append(low)

    for i in range(len(arr)):
        if arr[i] > low < high :
            temp = arr[i]
            new_arr.append(temp)

    print("high:",high)
    print("low:",low)
    print(new_arr)

zipit([10,2,3,5],[6,7,4])