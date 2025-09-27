def duplicate(num):
    freq_map = {}
    # store elements in dictionary (unique keys)
    for x in num:
        freq_map[x] = 1  

    j = 0
    # put unique keys back into num
    for k in freq_map:
        num[j] = k
        j += 1

    return j   # number of unique elements


num = [1,2,3,1,22,2,3,3,2,1,45,45,67]
a = duplicate(num)
print(a)          # count of unique numbers
print(num[:a])    # actual unique elements


#optimal way to remove duplicate in a array 

def optimal(num):
    n=len(num)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if num[j]!=num[i]:
         i=i+1
        num[i],num[j]=num[j],num[i]
        j=j+1

    return i+1

num=[1,34,56,67,87,34]
a=optimal(num)
print(a)