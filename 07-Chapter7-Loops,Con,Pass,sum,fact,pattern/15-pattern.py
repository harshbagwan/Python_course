n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)  # Print a full row of stars
    else:
        print("*" + " " * (n - 2) + "*")  # Print stars at the sides

