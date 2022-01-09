import random
import string
print("Welcome To The Password Generator")
l=int(input("\n Enter the desired Length of Password: \n"))
a=string.ascii_letters
n=string.digits
s="!#$&%?@*"
c=a+n+s
print(" Here's a Collection of Passwords:")
for i in range(0,10):
    j="".join(random.sample(c,l))
    print("\n",j)