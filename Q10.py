#Taking Input
s=input('Enter your String: ')
#Displaying Data
print('\nInput String:',s)
#Calculating and Displaying Output
l,s2=list(s),''
l.reverse()
for i in l:
    s2+=i
if s==s2:
    print('The provided string is a palindrome.')
else:
    print('The provided string is not a palindrome.')