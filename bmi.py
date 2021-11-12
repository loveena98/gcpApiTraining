from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['POST'])

def bmi():
    data = request.get_json()
    height = data['height']
    weight = data['weight']
    bmi = weight/(height**2)
    if bmi < 18.4:
        status = 'You are underweight!'
    elif bmi >= 18.4 and bmi <=24.9:
        status = 'Perfect!'
    else:
        status = 'You are overweight!'

    return jsonify({"Body mass index" : bmi, "msg" : status})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)