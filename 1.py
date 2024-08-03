
#this is a calculator which gtes two numbers and one operator from the user and
# and if the user enters break, breaks the game and if the user enters
# continue, continues the game.
def sums(num1,num2):
    return num1+num2
def minus(num1,num2):
    return num1-num2
def mult(num1,num2):
    return num1*num2
def devide(num1,num2):
    return num1/num2

    
counter=0
b="c"
while b=="c":
    if(counter==0):
        num1=int(input("enter a number:"))
        op1=input("enter an operator:")
        num2=int(input("enter another number:"))
    else:
        op1=input("enter an operator:")
        num1=int(input("enter a number:"))
        num2=answer
        
    if(op1=="*"):
        answer=mult(num1,num2)        
    elif(op1=="+"):
        answer=sums(num1,num2)
    elif(op1=="-"):
        if counter==0:
            answer=minus(num1,num2)
        else:
            answer=minus(num2,num1)
    elif(op1=="/"):        
        if counter==0:
            if num2==0:
                print("invalid input ")
                continue
            answer=devide(num1,num2)
        else:
            if num1==0:
                print("invalid input ")
                continue
            answer=devide(num2,num1)
        
        
    print("answer = ", answer)
    counter+=1
    b=input("enter break or continue: ")
    if b=="b":
        break
    
    