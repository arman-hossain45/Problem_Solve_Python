# def greet():
#     print("arman")
#     greet()

# greet()#it show stack overflow error this fun is called again again 
#we want to reduce the space for this reason we want to give a stop condition 

# def fun(count=0):
#     if count == 4:
#         return
#     count += 1
#     fun(count)
#     print("Arman")

# fun()

#recursion using parameters 

# def fun(x,n):
#     if n==0:
#         return
#     print(x)
#     fun(x,n-1)

# fun(15,4)

# #print 1 to 5 using recursion 

# def auto(i,n):
#     if i>n:
#         return
#     print(i)
#     auto(i+1,n)

# auto(0,5)

# #same code tail recursion it print reverse ot 0 to 5


# def auto(i,n):
#     if i>n:
#         return
 
#     auto(i+1,n)
#     print(i)

# auto(0,5)

#parameter and factorial recursion 
#sum of 1 to N

# def summation(total, i, n):
#     if i > n:
#         print(total)
#         return
#     summation(total + i, i + 1, n)

# # call function
# summation(0, 1, 5)   # Output = 15

#fuctional recursion 

# def sum_n(n):
#     if n == 1:
#         return 1
#     return n + sum_n(n - 1)

# # test
# print(sum_n(5))  # Output = 15

#factorial recursion using by recursion 

def fac(num):
    if num==0 or num==1:
        return 1
    return num*fac(num-1)



 







