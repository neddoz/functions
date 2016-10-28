def fib(n):

#Declare the variables to be used
    l = []
    a, b = 0, 1

#Calculate the nth fibonacci number
    for i in range(n):
        l.append(a)
        a, b = b, a+b

    return l