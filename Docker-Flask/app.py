from flask import Flask, jsonify, request
import pickle
import sys

app = Flask(__name__)



#Functions--------------------------------------------------------
def load_model():
    with open('clf.pickle','rb') as f:
        clf_loaded = pickle.load(f)
    return clf_loaded




#Routes--------------------------------------------------------
@app.route("/") # @ sign wraps the code for the route
def hello_world():
    return "<p>Hello, World!</p> Adri"


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


model = None

model = load_model()

@app.route('/predict', methods=[ 'POST'])
def predict():
    """
    "expects request.get_json to return a string that expects a valid url"
    """

    response_object = {'status': 'success'}
    if request.method == 'POST':
        url = request.get_json()
        length = len(url)
        prediction = model.predict_proba([[length]])
        print(prediction, file = sys.stderr)
        response_object['prediction'] = prediction.tolist()[0][1]
    return jsonify(response_object)



#Notes--------------------------------------------------------
