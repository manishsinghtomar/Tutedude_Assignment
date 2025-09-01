from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI) #client is an object (or instance) of the MongoClient class from the pymongo library. 

db = client.test #create database called 'test'

collection = db['flask-tutorial'] #creating collection that resides into test db called 'flask-tutorial'

app = Flask(__name__) #instance of Flask

@app.route('/submittodoitem', methods=['POST'])
def submit():
  
    form_data = dict(request.json)
  
    collection.insert_one(form_data) #inserting form's data into collection
  
    return 'Data submitted successfully'

@app.route('/view')
def view():

    data = collection.find() #collection.find() returns entire collection or cursor, a cursor is basically iteratable object but not exactly list similar to  list of objects(dictionaries) 
    # a collection is a list of JSON document which means that it's a list of dictionaries. 
    data = list(data) # making a python list
    
    for item in data:

        print(item)

        del item['_id']

    data = {
        'data':data
    }

    return jsonify(data)

if __name__ == '__main__':  #good practice to run app
    app.run(host='0.0.0.0',port=9000,debug=True)  #debug=True look for the changes and apply changes too