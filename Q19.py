#Taking Inputs
l=eval(input('Enter Your List of Integers: '))
n=int(input('Enter No. to be searched for in the list: '))
#Displaying Data
print('\nInput List:',l)
#Calculating and Displaying Output based on Input
for i in range(0,len(l)):
    if n==l[i]:
        print(n,'found in the list provided at',i,'index.')
        break
else:
    print(n,'not found in the list provided.')