import uuid
from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/predict', methods=['POST'])
def predict():
    "this expects requests.get_json to return a string that is a valid url"

    response_object = {'status': 'success'}
    if request.method == 'POST':
        url = request.get_json()
        length(url)
        #post_data = request.get_json()
        prediction = model.predict(url)
        response_object['message'] = prediction.tolist()[1]

    return jsonify(response_object)


def load_model():
    """
    load your fitted sklearn classifier from disk.

    """
    with open('clf.pickle', 'rb') as f:
        clf_loaded = pickle.load(f)

    return clf_loaded


def load_prediction_data():
    """
    load your fitted sklearn classifier from disk.

    """
    test_data_sample = pd.read_json('test.json')

    return test_data_sample


model = load_model()

if __name__ == "__main__":
    app.run()
