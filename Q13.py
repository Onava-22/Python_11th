#Taking Input
s=input('Enter Your String: ')
#Displaying Data
print('\nInput String:',s)
#Calculating and Displaying Output
l,n=s.split(),0
for i in l:
    if i.startswith('a'):
        n+=1
print('Your string contains',n,"words starting with 'a'.")