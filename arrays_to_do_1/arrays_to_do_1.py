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
    newnew=[]

    for i in range(len(arr)):
        newnew.append(arr[i])
    for i in range(len(arr2)):
        newnew.append(arr2[i])



    for i in range(0, len(newnew)):
        for j in range(i+1, len(newnew)):
            if(newnew[i] > newnew[j]):
                temp = newnew[i];
                newnew[i] = newnew[j];
                newnew[j] = temp;

    return newnew

print(zipit([4,15,100],[10,20,30,40]))

