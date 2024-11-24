# GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number that divides both of them. 
#  Division-based (Modulo) Euclidean Algorithm


def gcd_modulo(a,b):
    if b==0:
        return a
    else:
        return gcd_modulo(b,a%b)
    

number1 = int(input("Enter first number: "))

number2 = int(input("Enter second number: "))


print(f"GCD of {number1} and {number2} is {gcd_modulo(number1, number2)}")
