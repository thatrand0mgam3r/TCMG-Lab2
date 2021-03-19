from flask import Flask, jsonify, Response
import hashlib

app = Flask(__name__)

@app.route('/fibonacci/<int:term>')
    def term(term):
        fib =[0,1]
        result = 0
        while result < term:
            result = fib[-1] + fib [-2]
            if (result < term):
                fib.append(result)
    return f"Output is: {fib}."


@app.route('/slack_alert/'<str:msg>)
        wekbook_url = 'https://hooks.slack.com/services/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'
    def slack_alert(msg):
        data = {'text':msg}
        resp = requests.post(SLACK_URL, json=data)
        if resp.status_code == 200:
            result = True
            mesg = "Post Accepted"
        else: # gives the error and message should the message result in a failure
            result= False
            mesg: "Please try again (HTTP error: "str(response.status_code)")
        
        return jsonify(#attempts to json the data and give the response code for error.
            input=msg,
            message=mesg,
            output=result
        ),200 if resp.status_code==200 else 400
        
@app.route('/is-prime/<int:num>')
    def is_prime(num):
        if isinstance(num, int):
    # show the post with the given id, the id is an integer
        if num > 1:
      # Iterate from 2 to n / 2
            for i in range(2, int(num/2)+1):
  
          # If num is divisible by any number between
          # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    return False
                    break
            else:
                return True
            else:
                return False
        else:
            return "Input is not an integer. You input a " + str(type(num))
@app.errorhandler(404)
def not_found(error):
    return "Input is not an integer"    
    return

# from flask import Flask
# app = Flask(__name__)
@app.route('/md5/<string:hash>')
def MD5(hash):
    user_input = input("Enter your sting here:")
    hash_object = hashlib.md5(user_input.encode())
    md5_hash = hash_object.hexdigest()
    print("Your string was: ", user_input)
    print("The MD5 hash equivalent of your sting is: ", md5_hash)

    
@app.route('/factorial/<int>')    
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
    
    
    

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
