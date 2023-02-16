#Assigning Default Vars
d={}
ch='Y'
print('Welcome to Your Contact Directory!\nThe Menu will Guide You Through:')
#Looping Whole Program
while ch.upper()=='Y':
#Displaying Menu and Taking Choice as Input
    print('''
    (A) Add Contacts
    (B) Display Contact Book
    (C) Search and Display Contact
    (D) Search and Edit Contact No.
    (E) Search and Delete Contact
    (F) Exit Contact Directory
    ''')
    ch2=input('Choose an Option: ')
#Calculating and Displaying Output based on Input
    if ch2.upper()=='A':
        print()
        ch3='Y'
        while ch3.upper()=='Y':
            nm=input('Enter Contact Name: ')
            no=input('Enter Contact No.: ')
            ad=input('Enter Contact Address: ')
            d[nm.title()]=[no,ad]
            ch3=input('\nAdd Another Contact? (Y/N): ')
            print()
        print('Updated Data...')
        ch=input('\nGo Back To Menu? (Y/N): ')
    elif ch2.upper()=='B':
        if len(d)!=0:
            for i in d.keys():
                print('\n',i,':',d[i][0],':',d[i][1])
        else:
            print('\nNo Contacts Available to Display...')
        ch=input('\nGo Back To Menu? (Y/N): ')
    elif ch2.upper()=='C':
        n=input('\nEnter Name of Contact to be Displayed: ')
        if n.title() in d.keys():
            print('''
    Name:''',n.title(),'''
    Contact No:''',d[n.title()][0],'''
    Address:''',d[n.title()][1])
        else:
            print('\nContact not Found in Directory...')
        ch=input('\nGo Back To Menu? (Y/N): ')
    elif ch2.upper()=='D':
        n=input('\nEnter Name of Contact to be Edited: ')
        if n.title() in d.keys():
            no=input('\nEnter New No.: ')
            d[n.title()][0]=no
            print('\nUpdated Data...')
        else:
            print('\nContact not Found in Directory...')
        ch=input('\nGo Back To Menu? (Y/N): ')
    elif ch2.upper()=='E':
        n=input('\nEnter Name of Contact to be Deleted: ')
        if n.title() in d.keys():
            del(d[n.title()])
            print('\nUpdated Data...')
        else:
            print('\nContact not Found in Directory...')
        ch=input('\nGo Back To Menu? (Y/N): ')
    elif ch2.upper()=='F':
        break
    else:
        print('\nEnter a Valid Choice')
        ch=input('\nGo Back To Menu? (Y/N): ')