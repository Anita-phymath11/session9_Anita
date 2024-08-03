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
l1=([-3,-2,-1,0,1,2,3])
for i in l1:
    seperator(i)

l2=[]
l2.append(evenl)
l2.append(oddl)
print(tuple(l2))

    
