import pickle
import numpy as np
import sklearn
from sklearn.neural_network import MLPClassifier


"""
XOR truth table:

|=========================|
| X1  |  X2  |  X1 XOR X2 |
|=========================|
| 0   |  0   |     0      |
| 0   |  1   |     1      |
| 1   |  0   |     1      |
| 1   |  1   |     0      |
|=========================|

"""


X = np.array([0,0,0,1,1,0,1,1]).reshape(4,2)
print(X)


Y = np.array([0,1,1,0]).reshape(4,)
print(Y)


model = sklearn.neural_network.MLPClassifier(activation='relu', max_iter=1000, hidden_layer_sizes=(4,2))
model.fit(X,Y)


# model.predict(np.array([1,0]).reshape(1,2))[0]


model_filename = "model/XOR_model.pkl"
pickle.dump(model, open(model_filename, 'wb'))

