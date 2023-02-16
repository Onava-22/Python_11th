#Assigning Default Vars
ch='Y'
#Looping Whole Program
while ch.upper()=='Y':
#Displaying Menu and Taking Choice as Input
    print('''
    (A) Display a List with Integers 0 to 49
    (B) Display a List with Sqaure of Integers 1 to 50
    (C) Exit Program.
    ''')
    ch=input('Choose an Option: ')
#Calculating and Displaying Output based on Input
    l=[]
    if ch.upper()=='A':
        for i in range(0,50):
            l.append(i)
        print(l)
        ch=input('\nReturn Back to Menu? (Y/N): ')
    elif ch.upper()=='B':
        for i in range(1,51):
            l.append(i**3)
        print(l)
        ch=input('\nReturn Back to Menu? (Y/N): ')
    elif ch.upper()=='C':
        break
    else:
        print('\nEnter a Valid Choice')
        ch=input('\nReturn Back to Menu? (Y/N): ')