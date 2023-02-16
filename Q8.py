#Taking Input
n=int(input('Enter No. of Elements Required from the Fibonacci Series: '))
#Assigning Vars default Values
m,a,b=0,0,1
#Calculating and Displaying Output
while m!=n:
    print(a,end=',')
    a,b=b,a+b
    m+=1