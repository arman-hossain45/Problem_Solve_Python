num=[12,23,45,67,90]
largest=num[0]
n=len(num)
for i in range(0,n):
    largest=max(largest,num[i])

print(largest)