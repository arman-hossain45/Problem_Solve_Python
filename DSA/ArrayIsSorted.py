def sorted(num):
    n=len(num)
    for i in range(0,n-1):
        if num[i]>num[i+1]:
            return False
        
    return True


n=[1,45,67,89,90]
a=sorted(n)
print(a)