#Taking Input
s=input('Enter Your String: ')
#Displaying data
print('\nInput String:',s)
#Calculating and Displaying Output
l,s3=s.title().split(),''
for i in l:
    l2=list(i)
    l2[-1]=l2[-1].capitalize()
    s2=''
    for i in l2:
        s2+=i
    s3=s3+s2+' '  
s=s3[:-1]
print('Updated String:',s)