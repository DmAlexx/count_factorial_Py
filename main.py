number = int(input("Enter any number to count factorial N: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} = {factorial}")
