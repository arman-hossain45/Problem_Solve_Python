# merge two sorted lists and return a new sorted list
def merge(left, right):
    result = []
    i = 0
    j = 0
    n = len(left)
    m = len(right)

    
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    
    if i < n:
        result.extend(left[i:])
    if j < m:
        result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


arr = [38, 27, 43, 3]
print("Before:", arr)
print("After: ", merge_sort(arr))
