# We are given a number. The task is to find the Number of Trailing Zeros in the factorial of the number.

def findTrailingZeros(n):
    if n < 0:
        return -1
    
    count = 0
    
    # Keep dividing n by powers of 5 and update count
    
    for i in range(5,n+1,5):
        count += n // i
        i *= 5
        if n // i < 1:  # Stop the loop when i exceeds n
            break
    return count


number = int(input("Enter a number: "))
print(f"Count of trailing 0s in {number}! is {findTrailingZeros(number)}")
