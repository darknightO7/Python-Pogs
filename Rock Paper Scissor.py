import random
Mov={1:'Rock',2:'Paper',3:'Scissors'}
print("Welcome to Rock-Paper-Scissor :\n")
print("Rules:\n Enter '1' for 'Rock'\n Enter '2' for 'Paper'\n Enter '3' for 'Scissor' \n")
n=int(input("Enter the Win Score:\t"))
print("\n Let the Game Begin:\n ")
z,c,p,q=0,0,0,1
def Valid(x):
    y=0
    if(x>0 and x<4):
        y=y+1
    return y
def Random ():
    cp=random.randint(1,3)
    return cp
def Score(p,c):
    print("Score: Player - Computer")
    print("\t",p,"-",c)
    global q
    if(p==n or c==n):
        q=0
def Result(x):
    global c
    global p
    cm=Random()
    print("Computer Choose:  ",Mov[cm])
    if(x==1 and cm==3 or x==3 and cm==1):
        if(x>cm):
            print("Computer Wins \n")
            c=c+1
        else:
            print("You Win \n")
            p=p+1
    else:
        if(x>cm):
            print("You Win\n")
            p=p+1
        elif(x==cm):
            print("It's a Tie\n")
        else:
            print("Computer Wins\n")
            c=c+1
    Score(p,c)
while (q != 0):
    z=z+1
    print("\n Round ",z,":")
    x=int(input("Enter your Move:\t"))
    k=Valid(x)
    if(k>0):
        print("You Choose: ",Mov[x])
        Result(x,)
    else:
        print("Please enter a vaild Input and Try again !!")
    if(q==0):
        if(p==n):
            print("Congratulations You Won !!")
        else:
            print("You Lost Better Luck next Time !!")