import timeit
from matplotlib import pyplot as plt
#Origional:
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
#Optimized:
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_num = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = fib_num
    return fib_num

first_dic= {}
optimized_list=[]
origional_list=[]
for i in  range(0,36):
    
    optimized_time = timeit.timeit(lambda: fibonacci(i), number=1)
    origional_time = timeit.timeit(lambda:func(i),number=1)
    optimized_list.append(optimized_time)
    origional_list.append(origional_time)

plt.plot (optimized_list)
plt.xlabel ("number")
plt.ylabel("time")
plt.title("optimized")
plt.plot(origional_list)
plt.xlabel ("number")
plt.ylabel("time")
plt.title("Original(Orange) VS Optimized(Blue)")
plt.show()