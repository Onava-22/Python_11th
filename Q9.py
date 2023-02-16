#Taking Inputs
n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
#Calculating and Displaying Outputs
if n1<n2:
    n1,n2=n2,n1
for i in range(1,n2+1):
    if n1%i==0 and n2%i==0:
        hcf=i
for j in range(n1,(n1*n2)+1):
    if j%n1==0 and j%n2==0:
        lcm=j
        break
print('\nFor the Numbers',n1,'and',n2,':')
print('The HCF is:',hcf,'\nThe LCM is:',lcm)