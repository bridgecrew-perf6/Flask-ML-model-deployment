import numpy as np
import sklearn
import pickle
from sklearn.neural_network import MLPClassifier
from flask import Flask, request, jsonify


def predict_xor(x1, x2):
    out = {"predicted_xor_value":0}
    X_in = np.array([x1,x2]).reshape(1,2)
    model_filename = "model/XOR_model.pkl"
    model = pickle.load(open(model_filename, 'rb'))
    out['predicted_xor_value'] = str(model.predict(X_in)[0])
    return out


app = Flask(__name__)


@app.route("/")
def health_ckeck():
    return "Server is Running!!!"


@app.route("/xor_predict", methods = ['GET'])
def xor_prediction():
    """
    /xor_predict?x1=1&x2=1
    """    
    try:
        X1 = int(request.args['x1'])
        X2 = int(request.args['x2'])
        if (X1 != None) and (X2 != None) and (X1 in [0,1]) and (X2 in [0,1]):
            response = predict_xor(X1,X2)
        else:
            response = {
                'success': False,
                'message': 'Invalid input data!'
            }
    except:
        response = {
            'success': False,
            'message': 'Unknown Error...'
        }
    return jsonify(response)


if __name__ == "__main__":
    app.run()

