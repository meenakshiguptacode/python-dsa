# Factorial of a Number

def fact(n):
    fact =1
    for i in range(1,n+1):
        fact *= i
    return fact

number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {fact(number)}")