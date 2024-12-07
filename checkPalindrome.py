# A palindrome number is a number that reads the same forward and backward. In other words, if you reverse the digits of a number, it remains the same.

def checkPalindrome(n):
    reverse =  0
    temp = n
    while(temp != 0):
        ld = temp % 10
        reverse = reverse * 10 + ld
        temp = temp // 10
        
    return (reverse == n)

number = int(input("Enter the number"))
if checkPalindrome(number):
    print("yes")
else:
    print("no")
