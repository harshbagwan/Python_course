n =int ( input ("enter the number \n"))
for i in range(2,n):
    if(n%i)==0:
        print("Number is not prime")
        break
else:
    print("number is prime")