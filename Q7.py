#Taking Input
n=int(input('Enter no of Prime No.s Required: '))
#Assigning Vars Default Values
i,a=3,0
#Calculating and Displaying Output
for i in range(1,1000000000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=',')
        i+=1
        a+=1
    if a==n:
        break