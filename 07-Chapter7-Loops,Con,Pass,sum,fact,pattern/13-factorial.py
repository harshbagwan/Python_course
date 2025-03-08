n = int (input ("enter the number: \n"))
product = 1
for i in range(1,n+1): ## range 1 se lekar n-1 tak jata h isliye mene n+1 liya bcoz i wanted to include the n 
    product *=i
    
print(f"the factorial of {n} is {product}")
