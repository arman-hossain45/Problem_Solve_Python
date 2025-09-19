#specific number  how many which number is disible 

#normal way to code 
# def find_divisors(num):
#     result = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             result.append(i)
#     return result

# # Example use
# num = 20
# print(find_divisors(num))#time complexity og this code is 0(n)

#optimal solution 
# def finddivisor(num):
#     res=[]
#     for i in range(1,num//2):#time complexity is 0(n/2)
#         if num%i==0:
#             res.append(i)
#     res.append(num)

#     return res
        
# num=20
# print("divisor of",finddivisor(num))

#more optimal solution 

from math import sqrt

def moreoptimalway(num):
    res = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            res.append(i)
            if num // i != i:   # avoid duplicate when i == sqrt(num)
                res.append(num // i)
    res.sort()
    return res

# Example use
num = 20
print("Divisors of", num, "are:", moreoptimalway(num))


        