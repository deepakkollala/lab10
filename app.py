#This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle

print("Test")
print("Test 2")
print(os.getcwd())
path = os.getcwd()

with open('Models/Pickle_RL.pkl', 'rb') as f:
    logistic = pickle.load(f)


def get_predictions(price, Tax, Driver_Age, Licence_Length_Years, req_model):
    mylist = [Driver_Age, Tax, price, Licence_Length_Years]
    mylist = [float(i) for i in mylist]
    vals = [mylist]
    req_model == 'Logistic'
    if req_model == 'Logistic':
        #print(req_model)
        return logistic.predict(vals)[0]
    else:
        return "Cannot Predict"


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']



        req_model = 'Logistic'

        target = get_predictions(age,	sex,	cp,	trestbps,	chol,	fbs,	restecg,	thalach,	exang,	oldpeak,	slope,	ca,	thal, req_model)

        if target==1:
            sale_making = 'Have heart disease'
        else:
            sale_making = 'Doesnt have heart disease'

        return render_template('home.html', target = target, sale_making = sale_making)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)