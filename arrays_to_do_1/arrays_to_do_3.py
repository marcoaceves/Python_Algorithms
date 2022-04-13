import math
from traceback import print_tb

# Implement removeNegatives() that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives’ order. As always, do not use built-in array functions.

def removeNegatives(arr):
    for i in arr:
        if i < 0 :
            arr.remove(i)

    return arr

print(removeNegatives([1, -5, 4, 3, -2, 6]))

# Second-to-Last

# Return the second-to-last element of an array. Given [42,true,4,"Kate",7], return "Kate". If array is too short, return null.

def second_to_last(arr):

    if len(arr) <= 1:
        return 'null'
    else:
        return arr[len(arr)-2]

print(second_to_last([42]))
print(second_to_last([42,True,4,"Kate",7]))



# Second-Largest

# Return the second-largest element of an array. Given [42,1,4,Math.PI,7], return 7. If the array is too short, return null.


def second_largest(arr):
    largest=arr[0]
    if len(arr) <= 1:
        return 'null'
    else:
        for i in arr:
            if i > largest:
                largest = i
        for i in arr:
            if i < largest:
                secondLargest= i
                if i> secondLargest:
                    secondLargest = i 
    return(secondLargest)

print(second_to_last([42]))
print(second_largest([42,1,4,math.pi,7]))


# Nth-to-Last

# Return the element that is N-from-array’s-end. Given ([5,2,3,6,4,9,7],3), return 4. If the array is too short, return null.

def n_to_last(arr,n):

    if len(arr)-n < 0:
        return 'null'
    return (arr[len(arr)-n])

print(n_to_last([5,2,3,6,4,9,7],3))



# Nth-Largest

# Liam has "N" number of Green Belt stickers for excellent Python projects. Given arr and N, return the Nth-largest element, where (N-1) elements are larger. Return null if needed.

def Nth_largest(arr,n):
    # i= sorted(arr)
    for k in range(len(arr)-1):
        for j in range(k+1, len(arr)):
            if(arr[k] > arr[j]):
                temp = arr[k];
                arr[k] = arr[j];
                arr[j] = temp;


    return arr[len(arr)-n]




print(Nth_largest([5,2,3,6,4,9,7],3))


# Skyline Heights

# Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().

def skyline(arr):
    new_arr=[]
    temp=arr[0]
    if arr[0]>0:
            new_arr.append(arr[0])
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            new_arr.append(arr[i+1])

    return new_arr


print(skyline([-1,2,1,7,3]))