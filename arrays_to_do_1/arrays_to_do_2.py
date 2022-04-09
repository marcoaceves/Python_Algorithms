# Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
# array – move values within the array that you are given. As always, do not use built-in array functions such as splice().
arr=[1,2,3,4,5,1,9]

def reverse(arr):
    x=1
    for i in range(len(arr)//2):
        temp =arr[i]
        arr[i] = arr[len(arr) -x]
        arr[len(arr) -x] = temp
        x+=1
    return arr

print(reverse(arr))