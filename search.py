import time
import math
# linear search
def linear_search(data,key):
    start=time.time()
    for index, item in enumerate(data):
        if item >= key:
            return index,item
    return len(data)-1,None
# binary search
def binary_search(data,item):
    L = 0
    R = len(data) - 1
    while(L<R):
        index=math.floor((L+R)/2)
        if data[index] < item:
            L = index + 1
        elif data[index] > item:
            R = index
        else:
            return index,data[index]
    return L,data[L]
# insertion sort
def insertion_sort(data):
    for i in range(1,len(data)):
        for j in range(i,0,-1):
            if data[j-1] > data[j]:
                temp = data[j-1]
                data[j-1] = data[j]
                data[j] = temp
    return data     
def insertion_sort_optimized(data):
    for i in range(1,len(data),1):
        idx,item = linear_search(data[:i],data[i])
        if data[idx] > data[i]:
            data[idx:i+1]=data[i],*data[idx:i]
    return data
def insertion_sort_final(data):
    for i in range(1,len(data),1):
        idx,item = binary_search(data[:i],data[i])
        if data[idx] >= data[i]:
            data[idx:i+1] = data[i],*data[idx:i]
    return data
# merge sort
def merge_sort(data:list, verbose=False, level=0):
    indent = "  " * level
    if len(data) <= 1:
        if verbose: print(f"{indent}Returning: {data}")
        return data
    mid = len(data)//2
    if verbose: print(f"{indent}Divide: {data[:mid]} and {data[mid:]}")
    Left = merge_sort(data[:mid], verbose, level + 1)
    Right = merge_sort(data[mid:], verbose, level + 1)
    merged = merge(Left, Right, verbose, level)
    if verbose: print(f"{indent}Merge: {merged}")
    return merged

def merge(left:list, right:list, verbose=False, level=0):
    indent = "  " * level
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    else:
        result.extend(right[j:])
    return result
# heap sort
def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
def heapify(lst, n, i, verbose=False):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lst[largest] < lst[left]:
        largest = left
    if right < n and lst[largest] < lst[right]:
        largest = right
    if largest != i:
        if verbose: print(f"Swap {lst[i]} and {lst[largest]}")
        swap(lst, i, largest)
        heapify(lst, n, largest, verbose) # maintain max heap
def heapSort(lst, verbose=False):
    n = len(lst)
    if verbose: print("Building max heap:")
    for i in range(n // 2 - 1, -1, -1): # i means parent
        heapify(lst, n, i, verbose)
        if verbose: print(lst)
    if verbose: print("\nStarting heap sort:")
    for i in range(n-1, 0, -1):
        if verbose: print(f"Swap {lst[0]} and {lst[i]}")
        swap(lst, 0, i)
        if verbose: print(lst[:i], "|", lst[i:])
        heapify(lst, i, 0, verbose)
# quick sort
def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)
            _quick_sort(items, low, pivot_index - 1)
            _quick_sort(items, pivot_index + 1, high)
    def partition(items, low, high):
        midpoint = (low + high) // 2
        pivot = items[midpoint]
        items[midpoint], items[high] = items[high], items[midpoint]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1
    _quick_sort(arr, 0, len(arr) - 1)
