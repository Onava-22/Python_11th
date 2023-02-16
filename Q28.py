#Taking Inputs
print('You are requested to enter 10 Integers.')
l=[]
for i in range(10):
    n=int(input('Enter Integer: '))
    l.append(n)
#Displaying Data
print('\nThe List of Numbers Provided:\n',l)
#Calculating and Displaying Output
l.sort()
print('''
The List in Ascending Order:
''',l,'''

The 3rd Largest Integer is:
''',l[-3])