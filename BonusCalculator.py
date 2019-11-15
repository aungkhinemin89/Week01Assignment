workingHrs=input("Enter your working hours : \n")
payRate=input("Enter your payment rate by hour : \n")
if(int(workingHrs)>40):
    print("your working hours is not over 40")
    print("your payment amount is ", int(workingHrs)*int(payRate)*2)
else:
    print("your working hours is over 40")
    print("your payment amount is ", int(workingHrs)*int(payRate))