# Given a number N, the task is to return the count of digits in this number.

def countDigit(n):
    if n == 0:
        return 1
    count = 0
    while n != 0:
        n = n//10
        count +=1
    return count


number = int(input("Enter the number"))
print("Number of digits:", countDigit(number))
    
    