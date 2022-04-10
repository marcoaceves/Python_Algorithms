# Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
# array – move values within the array that you are given. As always, do not use built-in array functions such as splice().
arr=[1,2,3,4,5,6]

def reverse(arr):
    x=1
    for i in range(len(arr)//2):
        temp =arr[i]
        arr[i] = arr[len(arr) -x]
        arr[len(arr) -x] = temp
        x+=1
    return arr

print(reverse(arr))


# Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), 
# change the array to [3,1,2]. Don't use built-in functions.
# Second: allow negative shiftBy (shift L, not R).
# Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
# Fourth: minimize the touches of each element.

def rotate_arr(arr, shiftby):

    for i in range(shiftby):

        last=arr[len(arr)-1]

        for j in range(len(arr)-1,-1,-1):
            arr[j] = arr[j-1]

        arr[0]=last
    print(arr)
rotate_arr(arr,1)

def rotate_arr_left(arr, shiftby):

    for i in range(shiftby):

        first=arr[0]

        for j in range(len(arr)-1):
            arr[j] = arr[j+1]

        arr[len(arr)-1]=first
    print(arr)

rotate_arr_left(arr,1)

# Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.

def elim(arr,min,max):


    for x in list(arr):
        if x < min or x > max:
            arr.remove(x)
    print(arr, 'elim')
elim([1, 5, 4, 3, 2, 6],3,5)




# elim min and max
def elim_min_max(arr):
    min=arr[0]
    max= arr[0]

    for i in range(len(arr)-1):
        if arr[i]< arr[i+1]:
            max=arr[i+1]
        if arr[i]> arr[i+1]:
            min=arr[i+1]
    for x in list(arr):
        if x== min:
            arr.remove(x)
    for x in list(arr):
        if x== max:
            arr.remove(x)

    print(arr, 'elimmaxmin')
elim_min_max(arr)