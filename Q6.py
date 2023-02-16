#Taking Input
n=int(input('Enter a No.: '))
#Assigning Var Default Value
hf=1
#Calculating and Displaying Output
for i in range(1,n):
    if n%i==0:
        hf=i
if hf==1:
    print('\nThe Provided No. is a Prime No.')
else:
    print('\nThe Provided No. is Not a Prime No.')