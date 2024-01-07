from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("outlook.html")

@app.route('/login')
def login():
   return "under construction"

@app.route('/signup')
def signup():
   return "under construction"

@app.route('/aboutus')
def aboutus():
   return "under construction"

if __name__ == '__main__':
   app.run("0.0.0.0",port=443)
