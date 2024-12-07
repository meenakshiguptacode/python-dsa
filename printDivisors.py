import math

def print_divisors(n):
    divisors = []
    
    for i in range(1,int(math.sqrt(n)+1)):
        if n % i == 0: 
            if n // i == i:
                print(i,end = " ")
                
            else:
                print(i, end = " ")
                divisors.append(n//i)
                
    
    for divisor in reversed(divisors):
        print(divisor,end = " ")
        

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print_divisorgits(number)

            
    
        
