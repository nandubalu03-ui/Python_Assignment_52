n = int(input("Enter a number: "))
if n>0:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"The factorial of {n} is: {factorial}")
else:
    print("Cannot find factorial for negative numbers..")

    