#Write a menu driven program to input any number from user and check it is prime, factorial of the number,
#and armstrong number
def prime(n):
    if n > 1:
        if n == 2:
            print(n, "is a Prime Number")
        else:
            for i in range(2, n):
                if n % i == 0:
                    print(n, "is not a Prime Number")
                    break
            else:
                print(n, "is a Prime Number")
    else:
        print(n, "is not a Prime Number")
    
def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    print("The factorial of", n, "is", product)
    
def armstrong(n):
    sum = 0
    num = 0
    temp = n
    while temp > 0:
        num = temp % 10
        sum += num**3
        temp = temp // 10
    if sum == n:
        print(n, "is an Armstrong Number")
    if sum != n:
        print(n, "is not an Armstrong Number")
    
while True:
    print("Welcome to Number Checker")
    print("1. Check if a Number is a Prime Number")
    print("2. Check a Number's Factorial")
    print("3. Check if a Number is an Armstrong Number")
    print("4. Exit Program")
    choice = int(input("Enter your Desired Choice Number from the above menu: "))
    if choice == 4:
        print()
        break
    
    num = int(input("Enter a Number: "))
    if choice == 1:
        prime(num)
        
    if choice == 2:
        factorial(num)
        
    if choice == 3:
        armstrong(num)        
print("Thank You for Using the Program")
