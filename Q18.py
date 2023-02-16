#Taking Input
l=eval(input('Enter a List with Even No. of Elements: '))
#Displaying Data
print('Original List:',l)
#Calculating and Displaying Output
for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]
print('Updated List:',l)