import time
print("The Format is  hrs:min:sec")
H,M,S=int(input("Hrs:\t")),int(input("mins:\t")),int(input("sec:\t"))
print("Timer:\n")
while(H+M+S>0):
    while(S>=0):
        timer = '{:02d}:{:02d}:{:02d}'.format(H,M,S)
        print(timer,end="\r")
        if(S>0):
            time.sleep(1)
        S=S-1   
    if(M>0):
        S=59
        M=M-1
    elif(H>0):
        H=H-1
        M=59
        S=59
    else:
        print("\n Time Up!")