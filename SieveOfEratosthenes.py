# The Sieve of Eratosthenes is an efficient algorithm to find all prime numbers smaller than or equal to a given number n
# The time complexity of this algorithm is O(nloglogn), which is very efficient for finding all primes up to a large number n.
# The space complexity is O(n) because we store the prime status of each number in an array of size n + 1.


def sieve_of_eratosthenes(n):
    
    prime = [ True for _ in range(n+1)]
    prime[0]= prime[1]= False , False
    
    p = 2 
    while p * p <= n:
        if prime[p]:
        
          for i in range(p*p , n+1, p):
              prime[i] = False
        p += 1
    
    primes = []
    for p in range(2,n+1):
        if prime[p]:
            primes.append(p)
            
    return primes

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(sieve_of_eratosthenes(number))
     
