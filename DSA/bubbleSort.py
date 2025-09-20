#bublle sort algoritm 

# def sort(num):
#     n = len(num)   # get length of the list
#     # loop from n-2 down to 0 with step -2
#     for i in range(n-2, -1, -1):  
#         for j in range(0, i+1):
#             if num[j] > num[j+1]:
#                 # swap
#                 num[j], num[j+1] = num[j+1], num[j]
#     return num   # return sorted list


# Example
# arr = [5, 2, 9, 1, 7, 6]
# print(sort(arr))

#optimal solution to less time complexity
def bubbleSort(num):
    n = len(num)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):   # shrink the range each pass
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                swap = True
        if not swap:
            break
    return num

arr = [5, 2, 9, 1, 7, 6]
print(bubbleSort(arr))
