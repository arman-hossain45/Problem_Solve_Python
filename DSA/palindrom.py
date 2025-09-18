# Check if a number is a palindrome

def palindrome(num):
    n = num
    res = 0
    while n > 0:
        ld = n % 10
        res = res * 10 + ld
        n = n // 10

    return res == num   # compare with original number


# Test numbers
number = 1234
if palindrome(number):
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")

number = 1221
if palindrome(number):
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")
