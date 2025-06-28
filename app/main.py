from flask import Flask, request, jsonify
import random
from datetime import datetime, time

app = Flask(__name__)


import base64

@app.route("/data", methods=["POST"])
def data():
    input_str = request.json['data']
    encoded = base64.b64encode(input_str.encode()).decode()
    return jsonify({"result": encoded})


TICK_START = 8160000  # Could be any large arbitrary number

@app.route("/time", methods=["GET"])
def get_time():
    now = datetime.now()
    midnight = datetime.combine(now.date(), time(0, 0))
    seconds_passed = int((now - midnight).total_seconds())

    tick_value = max(0, TICK_START - seconds_passed)
    return jsonify(tick_value)


@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz():
    return jsonify(False)

@app.route('/zap', methods=['POST'])
def zap():
    input_str = request.json['data']
    no_digits = ''.join(c for c in input_str if not c.isdigit())
    return jsonify(no_digits)

@app.route('/alpha', methods=['POST'])
def alpha():
    input_str = request.json['data']
    return jsonify(input_str[0].isalpha())

@app.route('/glitch', methods=['POST'])
def glitch():
    input_str = request.json['data']
    if len(input_str) % 2 == 1:
        return jsonify(input_str[::-1])
    else:
        return jsonify(''.join(random.sample(input_str, len(input_str))))

if __name__ == '__main__':
    app.run(debug=True)
