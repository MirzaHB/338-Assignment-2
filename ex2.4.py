import json
import matplotlib.pyplot as plt
import sys
import timeit

sys.setrecursionlimit(20000)
def opt_sort(arr, low, high):
    if low < high:
        pi = opt_quicksort(arr, low, high)
        opt_sort(arr, low, pi-1)
        opt_sort(arr, pi + 1, high)
    return

def opt_quicksort(array, start, end):
    p = array[(start + end)//2] 
    low = start + 1 
    high = end      
    while True:
        while low <= high and array[high] >= p:    
            high = high - 1
        while low <= high and array[low] <= p:      
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return ( (high + low ) // 2)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start] 
    low = start + 1 
    high = end      
    while True:
        while low <= high and array[high] >= p:     
            high = high - 1
        while low <= high and array[low] <= p:      
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("file.json", "r") as file:
    arr = json.load(file)


def optimized_func(i):
    optimized = opt_sort(arr[i], 0, len(arr[i])-1)

unoptimized_y = []
optimized_y = []
array_x = []


for i in range(len(arr)):
    optimized_time = timeit.timeit(lambda: optimized_func(i), number=1)
    optimized_y.append(optimized_time)
    array_x.append(len(arr[i]))
plt.plot(array_x, optimized_y, label = "optimized_func")
with open("file.json", "r") as file:
    arr = json.load(file)

def unoptimized_func(i):
    unoptimized = func1(arr[i], 0, len(arr[i])-1)
unoptimized_y = []
array_x = []

for i in range(len(arr)):
    unoptimized_time = timeit.timeit(lambda: unoptimized_func(i), number=1)
    unoptimized_y.append(unoptimized_time)
    array_x.append(len(arr[i]))
plt.plot(array_x, unoptimized_y, label = "unoptimized_func")
plt.xlabel(' elements ')
plt.ylabel(' time (seconds)')
plt.legend()
plt.show()