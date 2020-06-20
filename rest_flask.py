from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'You sent': some_json}), 201
    else:
        return jsonify({'About':'Welcome to this workshop :)'})

@app.route('/multiply/<int:num>')
def get_product10(num):
    return jsonify({'result':num*10})

if __name__ == '__main__':
    app.run(debug=True)

