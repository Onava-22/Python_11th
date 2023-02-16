#Taking Input
l=eval(input('Enter Your List of Integers: '))
#Displaying Data
print('\nOriginal List:',l)
#Calculating and Displaying Output
for i in range(0,len(l)):
    if l[i]%7==0:
        l[i]=l[i]*7
    else:
        l[i]=l[i]*3
print('Updated List:',l)