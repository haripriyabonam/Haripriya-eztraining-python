import random
n=random.randrange(1,100)
guess=int(input("enter a number"))
while n!=guess:
    if(guess<n):
        print("Too low")
        guess=int(input("enter another number"))
    elif(guess>n):
        print("Too high")
        guess=int(input("enter another number"))
    else:
        break
print("your guess is correct")
    
