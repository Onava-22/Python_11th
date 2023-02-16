#Assigning Default Vars
d={}
ch='Y'
#Looping Whole Program
while ch.upper()=='Y':
#Displaying Menu and Taking Choice as Input
    print('''
    (A) Add Student Profiles
    (B) Display Student Profiles
    (C) Display Names of Students with Marks > 75
    (D) Delete Profiles of Students with Marks < 50
    (E) Exit Student Directory
    ''' )
    ch2=input('Choose An Option: ')
#Calculating and Displaying Output based on Input
    if ch2.upper()=='A':
        print()
        ch3='Y'
        while ch3.upper()=='Y':
            rn=int(input('Enter Student Roll No.: '))
            nm=input('Enter Student Name: ')
            mk=int(input('Enter Student Marks out of 100: '))
            ch3=input('\nContinue adding more student profiles? (Y/N): ')
            print()
            d[rn]=[nm.title(),mk]
        print('Updated Data...')
        ch=input('\nGo Back To Menu? (Y/N): ')
    elif ch2.upper()=='B':
        if len(d)!=0:
            for i in d.keys():
                print('\n',i,':',d[i][0],':',d[i][1])
        else:
            print('\nNo Student Profiles Available to Display...')
        ch=input('\nGo Back To Menu? (Y/N): ')
    elif ch2.upper()=='C':
        if len(d)!=0:
            print('\nThe Names of Students with Marks > 75 are:')
            for i in d.keys():
                if d[i][1] >75:
                    print(d[i][0])
        else:
            print('\nNo Student Profiles in Directory...')
        ch=input('\nGo Back To Menu? (Y/N): ')
    elif ch2.upper()=='D':
        if len(d)!=0:
            while True:
                for i in d.keys():
                    if d[i][1]<50:
                        del(d[i])
                        break
                else:
                    break
            print('\nUpdated Data...')
        else:
            print('\nNo Student Profiles in Directory...')
        ch=input('\nGo Back To Menu? (Y/N): ')
    elif ch2.upper()=='E':
        break
    else:
        print('\nEnter a Valid Choice')
        ch2=input('\nGo Back To Menu? (Y/N): ')