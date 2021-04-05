#from flask import Flask
#app = FLask (__name__)
@app.route("factorial/<integer>" 
def factorial(num):
    factorial=1
    if num < 0:
        return jsonify(input=num, output="Factorial cannot be found for negative number")
    elif num == 0:
       return jsonify(input=num, output=1)
    else:
        for i in range(1, num+1):
           factorial = factorial*i
       return jsonify(input=num, output=factorial) 
