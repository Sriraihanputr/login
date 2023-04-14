import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

app = Flask(__name__)
client = MongoClient(MONGODB_URI)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/mypage')
def mypage():  
    return 'This is My Page!'

@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({
        'result':'success', 
        'msg': 'GET this request!'
    })

@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({
        'result':'success', 
        'msg': 'This request is POST!'
    })

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)