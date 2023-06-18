
from flask import Flask, jsonify
from model import predict_group_img
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    if request.method == "POST":

        image = request.files.get('groupimg', '')
        input = "./static/groupimg.jpeg"
        output = "./static/result.jpeg"
        image.save("./static/groupimg.jpeg")
        res = predict_group_img("./static/groupimg.jpeg")
        if res:
            # return render_template('predict.html', input=input, output=output)
            return jsonify({'input': input, 'output': output})

        else:
            return jsonify({'msg': "Please Try Again"})
    else:
        return render_template('predict.html')


@app.route("/about")
def about():
    return render_template('about.html')
