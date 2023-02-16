#Taking Input
l=eval(input('Enter Your List of Integers: '))
#Displaying Data
print('\nOriginal List:\n',l)
#Calculating and Displaying Output
nl=[]
for i in l:
    if i not in nl:
        nl.append(i)
l=nl
print('The Updated List:\n',l)