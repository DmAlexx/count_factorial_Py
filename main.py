while True:
    number = int(input("Enter any number above zero to count factorial N: or 0 to exit "))
    factorial = 1

    if number >= 1:
        for i in range(1, number + 1):
            factorial *= i
        print(f"Factorial of {number} = {factorial}")
    elif number < 0:
        print("Wrong number!")
    elif number == 0:
        break
