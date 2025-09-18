
# Count digits in a number

def CountDigit(num):
    n = num
    count = 0

    while n > 0:
        n = n // 10   # remove last digit
        count = count + 1
    
    return count


# Example
number = 12345
print("Number of digits:", CountDigit(number))

