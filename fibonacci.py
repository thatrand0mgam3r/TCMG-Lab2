# from flask import Flask
# app = Flask(__name__)

# @app.route('/fibonacci/<int:n>')
fib = [0,1]
result = 0

while result < n: 
# will continue looping until the process reaches the same number as we input/ stop just before it reaches it
    result = fib[-1] + fib[-2]
    #adds up the 2 previous spots together
    if (result < n):
        fib.append(result)# will overwrite the original fib so it mathces the new data set
if n > 0:
    print(fib) 
elif n <= 0:
    print("ERROR")
