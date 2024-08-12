#Write a Program using functions to calculate the nth term of Fibonacci Series
def fibonacci(term):
    a= 1
    b = 0
    c = 0
    fib_list = [0]
    for i in range(term-1):
        c = a+b
        a = b
        b = c
        fib_list.append(c)
    print(fib_list)
    print(fib_list[-1], "is the", n, "th term of the Fibonacci Series")
    
n = int(input("Enter the nth term number: "))
fibonacci(n)