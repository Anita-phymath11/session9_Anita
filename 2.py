# This program takes a number from the user
# and shows its Fibonacci series. This program is written with def.

def fibona(num):
    fib1=1
    fib2=1
    fib=0
    print(fib1)
    print(fib2)
    while fib<=num:    
        fib=fib1+fib2
        fib1=fib2
        fib2=fib
        if(fib<num):
            print(fib)

num1=int(input("enter a number:"))
fibona(num1)

