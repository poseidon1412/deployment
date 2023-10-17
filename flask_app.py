# imports
from flask import Flask
from flask import request
import json
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('project.pkl', 'rb'))
def pred(sample_text):
  predictions = model.predict(np.array([sample_text]))
  print(*predictions[0])
  # Print the label based on the prediction
  if predictions[0] > 0:
    return 'Positive'
  else:
    return 'Negative'

@app.route('/', methods=['GET','POST'])
def handle_request():
    text = str(request.args.get('review')) #requests the ?review=''
    if text == 'None':
      predi = "Prediction"
    else:
      predi = pred(text)

    data_set = {'customer_review': text , 'prediction':predi}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == "__main__":
  app.run()
