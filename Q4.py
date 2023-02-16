#Taking Input
n=input('Enter a No.: ')
#Saving Values in Vars & assigning Default Values
org,val,res=int(n),int(n),0
#Calculating and Displaying Output
for i in range(0,len(n)):
    d,org=org%10,org//10
    res+=d**3
if res==val:
    print('\nThe Provided No. is an Armstrong No.')
else:
    print('\nThe Provided No. is Not an Armstrong No.')