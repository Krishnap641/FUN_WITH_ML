'''
Project: Fun with Machine Learning
Created by: Krishna Prakash
Date created : 17-Oct-2016
Purpose:
This is a sample web based online Gender Prediction model 
Features:
1. Online submission of Fitness data
2. Predicting the Gender of the person baseed on fitness data
'''

from flask import Flask, render_template, request

# Gender prediction model development

# step 1 -- import package
import numpy as np
from sklearn import linear_model

#step 2 -- load training data
# data points
X = [[165,19],[175,32],[136,35],[174,65],[141,28],[176,15],[131,32],
[166,6],[128,32],[179,10],[136,34],[186,2],[126,25],[176,28],[112,38],
[169,9],[171,36],[116,25],[196,25]]

# labels for outcomes
Y = ['Man','Woman','Woman','Man','Woman','Man','Woman','Man','Woman',
'Man','Woman','Man','Woman','Woman','Woman','Man','Woman','Woman','Man']
data_feature_names = ['height','age']

# step 3 -- create a model
gender_model = linear_model.LogisticRegression()


# step 4 -- fit model to data
gender_model.fit(X, Y)


# REST API service
app = Flask(__name__)
@app.route('/',methods=['POST', 'GET'])
def home():
    home_page = '<html><h1>FITNESS DATA BASED GENDER PREDICTION</h1><body><a href="/fitness_data.html">Click here to submit your fitness data</a></html>'
    return home_page

@app.route('/fitness_data.html',methods=['POST', 'GET'])
def predict_gender():
    ht = 0
    age = 0
    gender = 'NA'
    if request.method == 'POST':
        ht = int(request.form['height'])
        age = int(request.form['age'])
        print(ht,age)
        # step 5 -- predicting outcome with new data
        gender = gender_model.predict([[ht,age]])
            
    return render_template('fitness_data.html',ht=ht, age=age, gender=gender)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

