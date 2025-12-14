p=int(input("Enter principal amount : "))
t=int(input("Enter time period : "))
r=int(input("Enter rate of interest : "))
c=p*(1+(r/100))**t
ci=c-p
print("The compound interest is :  ",ci)
