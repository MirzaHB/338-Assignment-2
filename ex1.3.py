def func_1(n, cache={}):
    if n == 0 or n == 1:
        return n
    if n in cache:
        return cache[n]
    else:
        result = func_1(n-1) + func_1(n-2)
    cache[n] = result
    return result





import json
import sys
sys.setrecursionlimit(20000)
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
with open  ('file.json','r',encoding= "latin-1") as file:
    array_1= json.load(file)

low=0

for i in range(len(array_1)):
    func1(array_1[i],low,len(array_1[i]))