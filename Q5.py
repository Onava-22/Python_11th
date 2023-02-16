#Taking Input
n=int(input('Enter a No.: '))
#Assigning Default Var Values
res=0
#Calculating and Displaying Output
for i in range(1,n):
    if n%i==0:
        res+=i
if res==n:
    print('\nThe Provided No. is a Perfect No.')
else:
    print('\nThe Provided No. is Not a Perfect No.')