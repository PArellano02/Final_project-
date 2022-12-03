'''
This is a "hello world" flask webpage.
During the last 2 weeks of class,
we will be modifying this file to demonstrate all of flask's capabilities.
This file will also serve as "starter code" for your Project 5 Twitter webpage.

NOTE:
the module flask is not built-in to python,
so you must run pip install in order to get it.
After doing do, this file should "just work".
'''

from flask import Flask, render_template
app = Flask(__name__)
# anythinhg that starts with an @ is called a decorator in python
#  in generall, decorators modify the functions that follow them 
@app.route('/')     
def root():
    # messages= [{'username': 'Pedro', 'age': 20, 'time' : time.now,  },{}]
    # render template does preprocessing of the input html file
    # tehcnically the input to the render template fucntion is in a language called jinja2
    # the output of render template is html
    return render_template('root.html')

# scheme://hostname/path
# @app.route  defines the path 
#  the hostname and scheme are fiven to you in the output of running the program
# for settings, the url is http://127.0.0.1:5000/login  to get this route
@app.route('/login') 
def login():
    return render_template('login.html')

@app.route('/logout') 
def logout():
    return render_template('logout.html')

app.run()
