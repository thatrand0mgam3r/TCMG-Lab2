#from flask import Flask
#app = FLask (__name__)
@app.route("factorial/<int:n>") 

def factorial(n):
    fact = 1
    if n == 1:
        print("input:", n, "output:", 1)
    elif n == 0:
        print("input:", n, "output:", 1)
    elif n < 0:
        print("Factorial cannot be found for negative integer")
    else:
        for i in range(1, n + 1):
            fact = fact * i
        print("input:", n, "output:", fact)
        
