# A prime number is a natural number greater than 1, which is only divisible by 1 and itself. First few prime numbers are: 2 3 5 7 11 13 17 19 23…..
import math

def is_prime(n):
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n%2 == 0 or n%3 == 0:
        return False
    
    for i in range(5,int(math.sqrt(n))+1,6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        
    return True

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("true" if is_prime(number) else "false")
        
    