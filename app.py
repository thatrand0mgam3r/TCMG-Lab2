from flask import Flask, Response, jsonify
import redis

App = Flask(__name__)
REDIS = None

#JSON payloads

#POST
@app.route("/keyval/<string:key_str>/<string:val>", methods=["POST"])
def post_value(key_str, val):
    cmd1 = "POST " + key_str + "/" + val
    if REDIS.exists(key_str) == True:
        return jsonify(key=key_str,
                       value=val, 
                       command=cmd1, 
                       result=False, 
                       error="Key already exists"), 409
    else:
        setvalue = REDIS.set(key_str, val)
        if setvalue is False:
            return jsonify(key=key_str,
                        value=val,
                        command=cmd1,
                        result=False,
                        error="Invalid request"), 400
        else:
            return jsonify(key=key_str,
                        value=val,
                        command=cmd1, 
                        result=True, 
                        error=""), 200 

#GET
@app.route("/keyval/<string:key_str>", methods=["GET"])
def get_value(key_str):
    cmd2 = "GET " + key_str
    if REDIS.exists(key_str) == False:
        return jsonify(key=key_str, 
                       value=val, 
                       command=cmd2, 
                       result=False, 
                       error="Key does not exist"), 404
    else:                   
        update_value = REDIS.get(key_str)
        if update_value is False:
            return jsonify(key=key_str,
                           value=val, 
                           command=cmd2, 
                           result=False,
                           error="Invalid request"), 400
        else:
            return jsonify(key=key_str,
                           value=val, 
                           command=cmd2, 
                           result=True, 
                           error=""), 200         

#PUT
@app.route("/keyval/<string:key_str>/<string:val>", methods=["PUT"])
def put_value(key_str, val):
    cmd3 = "PUT " + key_str + "/" + val
    if REDIS.exists(key_str, val) == False:
        return jsonify(key=key_str,
                       value=val, 
                       command=cmd3,
                       result=False, 
                       error="Key does not exist"), 404
    else:                   
        check = REDIS.set(key_str, val)
        if check is False:
            return jsonify(key=key_str,
                        value=val, 
                        command=cmd3, 
                        result=False, 
                        error="Invalid request"), 400
        else:
            return jsonify(key=key_str,
                        value=val, 
                        command=cmd3, 
                        result=True, 
                        error=""), 200

#DELETE
@app.route("/keyval/<string:key_str>", methods=["DELETE"])
def delete_value(key_str):
    cmd4 = "DELETE " + key_str
    if REDIS.exists(key_str)==False:
        return jsonify(key=key_str,
                       command=cmd4, 
                       result=False, 
                       error="Key does not exist"), 404
    else:
        deletetion = REDIS.delete(key_str)
        if deletetion is False:
            return jsonify(key=key_str,
                        command=cmd4, 
                        result=False, 
                        error="Invalid request"), 400
        else:
            return jsonify(key=key_str,
                        command=cmd4, 
                        result=True, 
                        error=""), 200











