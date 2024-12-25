import random

guess=int(input("enter the number you guessed ")) #number from 1 to 10

computer=random.randint(1,10) # the range is inclusive 
print("computer generated :",computer)
print("your guess:",guess)

if(guess==computer):
    print("congrats, u picked the right number")
elif(guess!=computer):
    print("Oops, u couldnt guess the number")
else:
    print("sometin went wrong ")
