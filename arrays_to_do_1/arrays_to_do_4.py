import random



# Shuffle

# In JavaScript, the Array object has numerous useful methods. It does not, however, contain a method that will randomize the order of an array’s elements. Let’s create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally. Do you need to return anything from your function?

def shuffle(arr):
    random.shuffle(arr)
    return arr

print(shuffle([1,2,3,4,5]))



# Remove Range

# Given array, and indices start and end, remove vals in that index range, working in-place (hence shortening the array). Given ([20,30,40,50,60,70],2,4), change to [20,30,70] and return it.


def remove_range(arr,start,end):
    print(arr)
    temp = []
    for x in range(start,end+1):
        temp.append(arr[x])
    print(temp)
    for x in temp:
        for i in arr:
            if i==x:
                arr.remove(i)
    return arr


print(remove_range([20,30,40,50,60,70],2,4))




# Intermediate Sums

# You will be given an array of numbers. After every tenth element, add an additional element containing the sum of those ten values. If the array does not end aligned evenly with ten elements, add one last sum that includes those last elements not yet been included in one of the earlier sums. Given the array [1,2,1,2,1,2,1,2,1,2,1,2,1,2], change it to [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6]

def sums(arr):
    loops, remainder = divmod(len(arr), 10)
    intermediate_sum = 0
    j = 0

    while j < loops:
        for i in range(10+j):
            intermediate_sum += arr[i]
        arr.insert(10, intermediate_sum)
        j += 1


    remainder_sum = sum(arr[(loops*10+loops):])
    arr.insert((loops*10+loops+remainder), remainder_sum)

    return arr

print(sums([1,2,1,2,1,2,1,2,1,2,1,2,1,2]))







# Double Trouble

# Create a function that changes a given array to list each original element twice, retaining original order. Convert [4,"Ulysses",42,false] to [4,4,"Ulysses","Ulysses",42,42,false,false].

def double_trouble(arr):
    double=arr
    new_arr=[]
    for i in range(len(arr)):
        new_arr.append(arr[i])
        new_arr.append(double[i])
    return new_arr




print(double_trouble([4,"Ulysses",42,False]))

# Zip It

# Create a standalone function that accepts two arrays and combines their values sequentially into a new array, at alternating indices starting with first array. Extra values from either array should be included afterward. Given [1,2] and [10,20,30,40], return new array containing [1,10,2,20,30,40].


def double_trouble(arr,arr2):
    new_arr=[]
    while arr:
        new_arr.append(arr[i])
    for i in range(len(arr2)):
        new_arr.append(arr2[i])
    return new_arr




x=zip([1,2],[10,20,30,40])
print(tuple(x))

# Second: combine the two arrays’ values into the first array, instead of into a new array. Much more fun!