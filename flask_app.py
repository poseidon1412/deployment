# imports
from flask import Flask
from flask import request
import json
import pickle
import numpy as np
import tensorflow as tf

app = Flask(__name__)
# model = pickle.load(open('project.pkl', 'rb'))
model = tf.keras.models.load_model('finale_model')
def pred(sample_text):
  print("Received the text!")
  predictions = model.predict(np.array([sample_text]))
  # Print the label based on the prediction
  if predictions[0] > 0:
    return 'Positive'
  else:
    return 'Negative'
  pass

@app.route('/', methods=['GET','POST'])
def handle_request():
    text = str(request.args.get('input')) #requests the ?input=''
    print(text)
    if text == 'None':
      predi = "Prediction"
    else:
      predi = pred(text)

    data_set = {'customer_review': text , 'prediction':predi}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == "__main__":
  app.run()
