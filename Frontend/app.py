from flask import Flask, render_template, request

import requests    # this module it allows you make HTTP request from inside python

BACKEND_URL = 'http://localhost:9000'

app = Flask(__name__) #instance of Flask

@app.route('/') #create route
def home():    
    return render_template('index.html')

@app.route('/submittodoitem', methods=['POST'])
def submit():

    form_data = dict(request.form)

    requests.post(BACKEND_URL + '/submittodoitem', json=form_data)

    return 'Data submitted successfully'

@app.route('/get_data')
def get_data():

    response = requests.get(BACKEND_URL + '/view')

    data = response.json()
    
    data['hello'] = 'world'
    
    return data


if __name__ == '__main__':  #good practice to run app

    app.run(host='0.0.0.0',port=8000,debug=True)  #debug=True look for the changes and apply changes too