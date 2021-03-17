
fib = [0,1]
result = 0
n =  int(input("What number would you like to go up to?  " ))
while result < n:
    result = fib[-1] + fib[-2]
    if (result < n):
        fib.append(result)
if n > 0:
    print(fib)
elif n <= 0:
    print("ERROR")