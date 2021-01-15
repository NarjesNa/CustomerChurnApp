# -*- coding: utf-8 -*-

import os
import numpy as np
import pickle
from flask import Flask, request, render_template, flash 
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

# Load ML model
model = pickle.load(open('model_LR.pkl', 'rb'))

DATA_DIR = "/Users/narjes/PycharmProjects/churnpredictionapp/venv"
# Create application
app = Flask(__name__)
# DB configuation
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(DATA_DIR, 'clients.sqlite3')
app.config['SECRET_KEY'] = "random string"


class clients(db.Model):
    id = db.Column('client_id', db.Integer, primary_key=True)
    gender = db.Column(db.Integer())
    education_level = db.Column(db.Integer())
    marital_status = db.Column(db.Integer())
    card_category = db.Column(db.Integer())
    income_category = db.Column(db.Integer())
    age = db.Column(db.Integer())
    nbcount = db.Column(db.Integer())
    seniority = db.Column(db.Integer())

    def __init__(self, gender, education_level, marital_status, card_category, income_category, age, nbcount, anciennete):
        self.gender = gender
        self.education_level = education_level
        self.marital_status = marital_status
        self.card_category = card_category
        self.income_category = income_category
        self.age = age
        self.nbcount = nbcount
        self.anciennete = anciennete



# Bind home function to URL
@app.route('/')
def home():
    return render_template('home.html')


# Bind predict function to URL
@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        if not request.form['gender'] or not request.form['education'] or not request.form['maritstatus']:
            flash('Please enter all the fields', 'error')
        else:
            client = clients(request.form['gender'], request.form['education'], request.form['maritstatus'],
                             request.form['cardcat'], request.form['incomecat'], request.form['age'],
                             request.form['nbcount'], request.form['anciennete'])

            db.session.add(client)
            db.session.commit()
            flash('Record was successfully added')

            data = [request.form['gender'], request.form['education'], request.form['maritstatus'],
                             request.form['cardcat'], request.form['incomecat'], request.form['age'],
                             request.form['nbcount'], request.form['anciennete']]


            #data = [int(i) for i in data]
            #df = pd.DataFrame(columns=["Gender", "Education_Level", "Marital_Status", "Card_Category", "Income_Category", "Customer_Age","Dependent_count",
                    #"Months_on_book"])

            data = {'Gender': request.form['gender'],
                    'Education_Level': request.form['education'],
                    'Marital_Status':request.form['maritstatus'],
                    'Card_Category':request.form['cardcat'],
                    'Income_Category': request.form['incomecat'],
                    'Customer_Age': request.form['age'],
                    'Dependent_count':request.form['nbcount'],
                    'Months_on_book':request.form['anciennete']}


            # Create DataFrame
            df = pd.DataFrame(data, index=[0])
            df.apply(pd.to_numeric)
            output = model.predict(df)

            if output == 1 :
                return render_template('prediction.html',
                                   result='The client is likely to churn!')
            else:
                return render_template('prediction.html',
                                   result='The client is not likely to churn!')



if __name__ == '__main__':
    # create & run application
    db.create_all()
    app.run(debug=True)


