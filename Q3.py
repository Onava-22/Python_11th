#Taking Inputs
sl=int(input('Enter Your Salary Amount: '))
yr=int(input('Enter Your No. of Years in Service: '))
#Assigning vars default value
hra,hrp,da,dap=0,'',0,''
#Assigning Unique Vars based on Input
if yr>5 and yr<10:
    hra,hrp=sl/100*5,'(5%)'
    da,dap= sl/100*3,'(3%)'
elif yr>=10 and yr<20:
    hra,hrp=sl/100*4,'(4%)'
    da,dap= sl/100*2,'(2%)'
elif yr>=20:
    hra,hrp=sl/100*6,'(6%)'
    da,dap= sl/100*7,'(7%)'
#Calculating and Displaying Output
net=sl+hra+da
print('''
Base Salary: ₹''',sl,'''
HRA Provided: ₹''',hra,hrp,'''
DA Provided: ₹''',da,dap,'''
Net Salary: ₹''',net)