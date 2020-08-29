from flask import Flask, render_template, jsonify, request
import joblib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

model = joblib.load('RSModelRF')

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data_visualization')
def data_visualization():
    return render_template('datavisualization.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        input = request.form
        Administrative = float(input['Administrative'])
        Administrative_Duration = float(input['Administrative_Duration'])
        Informational = float(input['Informational'])
        Informational_Duration = input['Informational_Duration']
        ProductRelated = float(input['ProductRelated'])
        ProductRelated_Duration = float(input['ProductRelated_Duration'])
        BounceRates = float(input['BounceRates'])
        ExitRates = float(input['ExitRates'])
        PageValues = float(input['PageValues'])
        SpecialDay = float(input['SpecialDay'])
        OperatingSystems = float(input['OperatingSystems'])
        Browser = float(input['Browser'])
        Region = float(input['Region'])
        TrafficType = float(input['TrafficType'])
        VisitorType = float(input['VisitorType'])
        Weekend = float(input['Weekend'])
        Month = float(input['Month'])

        prediction = model.predict([[Administrative,Administrative_Duration,Informational, Informational_Duration, ProductRelated,ProductRelated_Duration,BounceRates,ExitRates,PageValues,SpecialDay, OperatingSystems,Browser,Region,TrafficType,VisitorType,Weekend,Month]])
        if prediction < 0.5:
            result = "This visitor is predicted not to purchase! Let's give them a dicount code to seal the deal!"
        else:
            result = "This visitor is predicted to purchase! Great!"
            
        return render_template('result.html', pred=result)

if __name__ == '__main__':
    model = joblib.load('RSModelRF')
    # countmatrix = joblib.load('') 
    df = pd.read_csv('Final Project Clean.csv')
    # dfNFRec = pd.read_csv('')
    app.run(debug=True)