import random
import math
print("Hello player:Welcome to the guessing game")
print("NOTE: Range should have at least 5 numbers")
l=int(input("Enter Lower Limit:\t"))
u=int(input("Enter Upper Limit:\t"))
k=round(math.log(u-l+1,2))
x=random.randint(l,u)
s=k*100
print("\n You've only ",k,"chances to guess the integer\n")
print("you are allotted",s," pointsand with each wrong guess 100 points will be deducted from your score")
c=1
y=0
for j in range (2,x) :
    if(x%j==0) :
        y+=1
z=0
while(c<=k):
    guess=int(input("Guess the number:\t"))
    if(x==guess):
        print("congratulations you guessed it in ",c," try")
        print("total score",s)
        break
    else :
        s=s-100
        print("Wrong guess")
        print("score:",s)
        if(c==1 and x%2==0) :
            print("Hint:Number is even")
        elif (c==2 and y==0) :
            z+=1
            print("Hint:Number is prime")
        elif (z==0 and c>1)  :  
            for i in range (c+1,x+1):
                if(x%i==0):
                    print("Hint:It is multiple of" ,i)
                    z+=1
                    break
        else :
           if(c<k):
            if(c==1) :
                print("Number is odd")
            elif (guess > x) :
                print("Guessed High")
            else :
                print("Guessed low")
    c+=1
if(c>=k) :
        print("\n You ran out of guesses")
        print("\n The number is",x)
        print("Better luck next time")