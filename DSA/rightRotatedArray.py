def rightRotated(num):
    n = len(num)
    
    rotated = [num[-1]] + num[0:n-1]
    return rotated

num = [1, 4, 3, 2, 4, 5, 6]
a = rightRotated(num)
print(a)


#optimal way without slicing right rotated 

def withoutSlicing(num):
    n = len(num)
    temp = num[n-1]  

    for i in range(n-2, -1, -1):
        num[i+1] = num[i]

    num[0] = temp
    return num


num = [1, 4, 3, 2, 4, 5, 6]
a = withoutSlicing(num)
print(a)


