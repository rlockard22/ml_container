from prediction import predict
from flask import Flask
from flask import jsonify
import connexion
from joblib import load

#load the model

my_model = load('my_model.pkl')

log_model = load('log_model.pkl')

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("myYAML.yml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"Current Working Endpoints": "                                                                                                                                                                                               "
     "Prediction:     " "/prediction/predict/{features (11)}"
    "                                                                                                                                                                                                                                   "
    "Statistics:     " "/prediction/stats" 
    "                                                                                                                                                                                                                                   "
    "Ryan Lockard E222 Final Project"}
   
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)