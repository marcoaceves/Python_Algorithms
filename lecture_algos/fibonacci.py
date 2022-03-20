

# def fibonacci(num):

#     num1=0
#     num2=1


#     if num <= 0:
#         print('Not going to work')
#     for i in range(2, num):
#         num3 = num1 + num2
#         num1 = num2
#         num2 = num3
#         print(num2)




# fibonacci(3)

def fibonacci(num):
    if num <= 1:
        return(num)
    else:
        return fibonacci(num - 1) + fibonacci(num-2)
print(fibonacci(7))