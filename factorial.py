def factorial(num):
    if num == 1:
            return num
    else:
        return num *factorial(num - 1)
num = int(input("Input: "))
if num < 0:
    print("Factorial cannot be found for negative integer")
elif num == 0:
    print("Output: 1")
else:
    print("Output:",factorial(num))