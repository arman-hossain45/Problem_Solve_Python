# n1=int(input("enter 1st number = "))
# n2=int(input("enter 2nd number = "))
# n3=int(input("enter 3rd number = "))

# min=n1
# max=n1
# if min>n2:
#     min=n2

# if min>n3:
#     min=n3

# if n2>max:
#     max=n2
# if n3>max:
#     max=n3

# print(min,max)

# x,min_v,max_v=input("enter numbers =").split()
# x=float(x)
# min_v=float(min_v)
# max_v=float(max_v)


# norm = (x - min_v) / (max_v - min_v)

# print(f"{norm:.2f}")

# x, min_v, max_v = input().split()
# x = float(x)
# min_v = float(min_v)
# max_v = float(max_v)

# norm = (x - min_v) / (max_v - min_v)

# print(f"{norm:.2f}")


# brightness,threshold=input().split()

# brightness=int(brightness)
# threshold=int(threshold)

# if brightness >= threshold:
#     print("ON")
    
# else:
#     print("OFF")

# n=int(input())
# target=float(input())
# total=0.0

# for i in range(n):
#     loss = float(input())
#     total=totall+loss

# avg =total/n

# if avg<=target:
#     print("PASS")
# else:
#     print("RETRY")

n=int(input())
yes=0
no=0

for i in range(n):
    vote=input()
    if vote=="YES":
        yes=yes+1
        
    else:
        no=no+1
        
if yes>no:
    print("ACCEPT")
    
else:
    print("REJECT")
  
