n1=int(input("enter 1st number = "))
n2=int(input("enter 2nd number = "))
n3=int(input("enter 3rd number = "))

min=n1
max=n1
if min>n2:
    min=n2

if min>n3:
    min=n3

if n2>max:
    max=n2
if n3>max:
    max=n3

print(min,max)
