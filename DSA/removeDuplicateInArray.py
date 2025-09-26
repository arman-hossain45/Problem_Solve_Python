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
