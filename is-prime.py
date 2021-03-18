# from flask import Flask
# app = Flask(__name__)

# @app.route('/is-prime/<int:num>')
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

# @app.errorhandler(404)
def not_found(error):
    return "Input is not an integer"

# app.run()

print(is_prime(90))
print(is_prime(5))
print(is_prime(7))
print(is_prime(7.54))
print(is_prime("word"))
