from flask import Flask, request, jsonify
from products import list_of_products

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'response':'OK'})

@app.route('/ping')
def pong():
    return jsonify({'response':'pong!'})

@app.route('/products')
def get_products():
    return jsonify({'response':'OK', 'data':list_of_products})

@app.route('/message/<string:msg>')
def get_message(msg):
    if msg=='hello':
        return jsonify({'response':'OK', 'data':'good bye!'})
    return jsonify({'response':'OK', 'data':msg})

@app.route('/message', methods=['GET'])
def message_get():
    return request.args
    #return jsonify({'response':'OK', 'data':request.args.get('msg')})
    
@app.route('/message', methods=['POST'])
def message_post():
    return request.data
    #return jsonify({'response':'OK', 'data':request.json['msg']})
    
@app.route('/message', methods=['PUT'])
def message_put():
    return request.data
    #return request.json['msg']

@app.route('/message', methods=['DELETE'])
def message_delete():
    return request.data
    #return request.json['msg']

if(__name__ == '__main__'):
    app.run(debug=True, port=666)