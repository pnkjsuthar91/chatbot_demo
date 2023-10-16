from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from chat import get_response


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/predict', methods=['POST'])
def redict():
    text = request.get_json().get('message')
    response = get_response(text)
    return jsonify({"message": response})


# @app.route('/train'):


if __name__ == '__main__':
    app.run(debug=True)
