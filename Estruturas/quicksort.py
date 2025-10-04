# Implementação de Quick Sort usando Recursividade.
def quicksort_v1(arr, left, right):
    if left < right:
        print(arr[left:right+1])
        pi = partition_v1(arr, left, right) # Pivota o array
        quicksort_v1(arr, left, pi-1)
        quicksort_v1(arr, pi+1, right)
    quicksort_v1(0, len(arr)-1)
    return arr

def partition_v1(arr, left, right):
    pivot = arr[right]

    i = left-1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1


# Implementação de Quick Sort usando list comprehension
def quicksort_v2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        bigger_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort_v2(less_than_pivot) + [pivot] + quicksort_v2(bigger_than_pivot)



arr = [0,3,6,7,8,4,2,1,5]

print(f"V1 \n {quicksort_v1(arr, 0, len(arr)-1)}")
print(f"V2 \n {quicksort_v2(arr)}")