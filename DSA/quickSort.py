def partition(num, low, high):
    pivot = num[low]
    i = low
    j = high

    while i < j:
        while num[i] <= pivot and i <= high - 1:
            i += 1
        while num[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            num[i], num[j] = num[j], num[i]

    num[low], num[j] = num[j], num[low]
    return j


def quick_sort(num, low, high):
    if low < high:
        pIdx = partition(num, low, high)
        quick_sort(num, low, pIdx - 1)
        quick_sort(num, pIdx + 1, high)


# Example usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
