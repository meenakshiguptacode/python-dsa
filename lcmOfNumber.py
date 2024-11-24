# LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers. 
#  LCM(a, b) = (a x b) / GCD(a, b)


def gcd_modulo(a,b):
    if b==0:
        return a
    else:
        return gcd_modulo(b,a%b)


def lcm_module(a,b):
   
        return (a*b)/ gcd_modulo(b,a%b)

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(f"LCM of {number1} and {number2} is {lcm_module(number1, number2)}")
