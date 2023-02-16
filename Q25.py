#Assigning Default Vars
l=[]
ch='Y'
#Taking Inputs in Loop
while ch.upper()=='Y':
    n=input('Enter the Place Name: ')
    ch=input('\nAdd Another Place? (Y/N): ')
    l.append(n)
    print()
#Displaying Data
print('Place Names with More than 5 Letters: ')
#Calculating and Displaying Output
for i in l:
    if len(i)>5:
        print(i.title())