import random
from functools import reduce

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        if pi > 0:
            quicksort_in_place(arr, low, pi - 1)
        if pi < (high - 1):
            quicksort_in_place(arr, pi + 1, high)

def select_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
arr = [64, 25, 12, 22, 11]
print("Before sorting:", arr)
sorted_arr = quicksort_in_place(arr, 0, len(arr) - 1)
print("After sorting using quicksort:", sorted_arr)

n = int(input("Enter the size of the array: "))
arr = [int(input(f"Enter element {i+1}:")) for i in range(n)]
print("Unsorted array:")
print(arr)

# Select sort
arr = arr.copy()
select_sort(arr)
print("\nUsing selection sort:", arr)

# Bubble sort
arr = arr.copy()
bubble_sort(arr)
print("\nUsing bubble sort:", arr)

random.shuffle(arr)
quicksort_in_place(arr, 0, len(arr) - 1)
sorted_arr = quicksort_in_place(arr, 0, len(arr) - 1)
print("After sorting using quicksort:", sorted_arr)
