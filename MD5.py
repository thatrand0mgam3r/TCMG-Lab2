# Lukas Boeck
# TCMG 412
# MD5 hash of a string
import hashlib
# from flask import Flask
# app = Flask(__name__)
# @app.route('/md5/<string:hash>')
def MD5(hash):
    user_input = input("Enter your sting here:")
    hash_object = hashlib.md5(user_input.encode())
    md5_hash = hash_object.hexdigest()
    print("Your string was: ", user_input)
    print("The MD5 hash equivalent of your sting is: ", md5_hash)
