from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__) #instance of Flask

@app.route('/') #create route
def home():    
    
    day_of_week = datetime.today().strftime('%A')

    current_time = datetime.now().strftime('%H:%M:%S')

    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/time')
def time():

    current_time = datetime.now().strftime('%H:%M:%S')

    return current_time

# @app.route('/second')
@app.route('/api/<name>')
def name(name):
    # print(name)
    length = len(name)

    result ="Hello " + name + '!'
    
    if length > 5:
        return 'Name is too long!   '+ result
    else:
        return "Nice Name!"


@app.route('/add/<a>/<b>') #<variable> syntax
def sumofnum(a,b):
    answer = int(a) + int(b)   #we can use multiply operator using '*'
    result ={              #return as dictionary
        'ans': answer
    }
    return result

# fetching data using JSON
@app.route('/api')
def name1():
    
    #for using request we have to import it 
    # this request is an object which is used to get data from the request that the client send to the server
    name = request.values.get('name')
    age = request.values.get('age')
    # result = {
    #     'name' : name,
    #     'age': age
    # }
    # return result
    age = int(age)
    if age > 18:
        return 'Welcome to the site, '+ name + '!'
    else:
        return 'Sorry, you are too young to use this site.'



@app.route('/submit', methods=['POST'])
def submit():
    # name = request.args.get('name')

# not good practice
    # name = request.form.get('name')
    # password = request.form.get('password')
        
    form_data = dict(request.form)
    print(form_data)
    return form_data

    # print(request.args)
    
    # return 'Hello, '+ name + '!'


if __name__ == '__main__':  #good practice to run app
    app.run(debug=True)  #debug=True look for the changes and apply changes too