# This program takes a number from the user 
# and says whether it is the first or not. 
# This program is written with def.

def prime_number(a):
    for b in range(2,a):
        if a%b==0:#a is devidable to b so it is not a prime number
            # return 2
            print("it is not prime ")
            return
    print("it is prime ")
               
a=int(input("enter a number "))
if a<0:
    print("It is not a natrual number! ")
else:
    prime_number(a)   
# if b==1: #a is not devidable to b so it is a prime number
#     print("it is not prime ")
# else:
    # print("it is prime ")