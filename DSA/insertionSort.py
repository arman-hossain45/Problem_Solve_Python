def insertionSort(num):
    n = len(num)
    for i in range(1, n):
        key = num[i]
        j = i - 1
        while j >= 0 and num[j] > key:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key

arr = [678, 34, 22, 5788, 90]
insertionSort(arr)
print("Sorted array:", arr)
