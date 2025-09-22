def selectionSort(num):
    n=len(num)
    for i in range(0,n):
        mini_idx=i
        for j in range(i+1,n):
            if num[j]<num[mini_idx]:
                mini_idx=j
        num[i],num[mini_idx]=num[mini_idx],num[i]


arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print("Sorted array:", arr)
