#Taking Input
s=input('Enter Your String: ')
#Displaying Data and Assigning Default Var Values
print('\nInput String:',s)
v,c,u,l=0,0,0,0
#Calculating and Displaying Output
for i in s:
    if i.isalpha():
        if i in 'AEIOUaeiou':
            v+=1
        else:
            c+=1
        if i.isupper():
            u+=1
        else:
            l+=1
print('''
Vowels:''',v,'''
Consonants:''',c,'''
Uppercase:''',u,'''
Lowercase:''',l)