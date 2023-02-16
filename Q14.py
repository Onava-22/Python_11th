#Displaying Directions
print("Press 'Enter' if no input required.")
#Taking Inputs
f=input('Enter Your First Name: ')
m=input('Enter Your Middle Name: ')
l=input('Enter Your Last Name: ')
#Calculating and Displaying Output based on Inputs
if f=='' and m=='':
    ini=l[0].upper()+'.'
if f=='' and l=='':
    ini=m[0].upper()+'.'
if m=='' and l=='':
    ini=f[0].upper()+'.'
elif f=='':
    ini=m[0].upper()+'.'+l[0].upper()+'.'
elif m=='':
    ini=f[0].upper()+'.'+l[0].upper()+'.'
elif l=='':
    ini=f[0].upper()+'.'+m[0].upper()+'.'
else:
    ini=f[0].upper()+'.'+m[0].upper()+'.'+l[0].upper()+'.'
print('''
Your Name is''',f,m,l,'''
Your Initials are''',ini)    