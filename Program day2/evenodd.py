a=int(input("enter a number"))
if (a%2==0 and a>0):
    print("it is a even-positive number")
elif(a%2!=0 and a>0):
    print("it is a odd-positive number")
elif(a%2==0 and a<0):
    print("it is a even-negative number")
elif(a%2!=0 and a<0):
    print("it is a odd-negitive number")
else:
    print("error")
