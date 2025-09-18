#if a number of its totall digit is power of its each digit and sum of this num is equal to its original number than its call armstrong number 

def arms(number):
    n=number
    nol=len(str(n))
    totall=0
    while n>0:
        ld=n%10
        totall=totall+(ld**nol)
        n=n//10
    return totall==number#here the original number will define

n=67
if arms(n):
    print(n ,"Is a armstrong number")

else:
    print(n ,"Is  not armstrong number")