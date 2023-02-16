#Taking Input
l=eval(input('Enter Your List of Integers: '))
#Displaying Data
print('\nOriginal List:',l)
#Calculating and Displaying Output
for i in range(0,len(l)):
    if l[i]%5==0:
        l[i]=5
    else:
        l[i]=0
print('Updated List:',l)