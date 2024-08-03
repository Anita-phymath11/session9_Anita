# A list of integers is given. The separator function
# is completed in such a way that by taking a list of 
# integers, it returns a tuple of two lists in the same
# order as they are in the input 
# list, that the first list contains even numbers and the
# second list contains odd numbers.


def seperator(x):
    if x%2==0:
        evenl.append(x)
    else:
        oddl.append(x)
evenl=[]
oddl=[]
l1=[]
while 1:
    inp=input("nums: ")
    if inp=='':
        break
    else:
        nums=int(inp)
        seperator(nums)

l2=[]
l2.append(evenl)
l2.append(oddl)
print(tuple(l2))

    