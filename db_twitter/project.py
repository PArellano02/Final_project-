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
import sqlite3
from flask import Flask, render_template, request, make_response
from flask import Response 
app = Flask(__name__)
con = sqlite3con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()


import argparse
import argparse
parser = argparse.ArgumentParser(description='Create a database for the twitter project')
parser.add_argument('--db_file', default='twitter_clone.db')
args = parser.parse_args()


# FIXME:
# print all of the information from the messages table 

# anythinhg that starts with an @ is called a decorator in python
#  in generall, decorators modify the functions that follow them 


def print_debug_info():
    # Get method
    print('request.args.get("username")=', request.args.get('username'))
    print('request.args.get("password")=', request.args.get('password'))
    # Post Method 
    print('request.form.get("username")=', request.form.get('username'))
    print('request.form.get("password")=', request.form.get('password'))
    # Cookies
    print('request.cookies.get("username")=', request.cookies.get('username'))
    print('request.cookies.get("password")=', request.cookies.get('password'))


def are_credentials_good(username, password):  
    # FIXME check in database 
    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    username = username
    sql = """
    SELECT password FROM users  where username= ?
    """
    cur.execute(sql,[username])
    con.commit()
    for row in cur.fetchall():
        if password == row[0]:
            return True
        else:
            return False 

def create_messages():
    con = sqlite3.connect(args.db_file)

    # construct messages,
    # which is a list of dictionaries,
    # where each dictionary contains the information about a message
    messages = []
    sql = """
    SELECT sender_id,message, created_at
    FROM messages
    ORDER BY created_at DESC;
    """
    cur_messages = con.cursor()
    cur_messages.execute(sql)
    for row_messages in cur_messages.fetchall():

        # convert sender_id into a username
        sql=  """
        SELECT username, age
        FROM users
        WHERE id="""+str(row_messages[0])+""";
        """
        cur_users = con.cursor()
        cur_users.execute(sql)
        for row_users in cur_users.fetchall():
            pass

        # build the message dictionary
        messages.append({
            'message': row_messages[1],
            'username': row_users[0],
            'age' :row_users[1],
            'posted_at' : row_messages[2]
            })
    return messages


def create_cookie(username, password):
            template = root()
            response = make_response(template)
            response.set_cookie('username',username)
            response.set_cookie('password',password)
            return response




@app.route('/')     
def root():
    print_debug_info()
    # # connect to the database
    # con = sqlite3.connect(args.db_file)

    # # construct messages,
    # # which is a list of dictionaries,
    # # where each dictionary contains the information about a message
    # messages = []
    # sql = """
    # SELECT sender_id,message, created_at
    # FROM messages
    # ORDER BY created_at DESC;
    # """
    # cur_messages = con.cursor()
    # cur_messages.execute(sql)
    # for row_messages in cur_messages.fetchall():

    #     # convert sender_id into a username
    #     sql=  """
    #     SELECT username, age
    #     FROM users
    #     WHERE id="""+str(row_messages[0])+""";
    #     """
    #     cur_users = con.cursor()
    #     cur_users.execute(sql)
    #     for row_users in cur_users.fetchall():
    #         pass

    #     # build the message dictionary
    #     messages.append({
    #         'message': row_messages[1],
    #         'username': row_users[0],
    #         'age' :row_users[1],
    #         'posted_at' : row_messages[2]
    #         })
   
    username = request.cookies.get('username')
    password = request.cookies.get('password')

    
    # render the jinja2 template and pass the result to firefox
    good_credentials = are_credentials_good(username, password)
    return render_template('root.html', messages=create_messages(), logged_in= good_credentials)



@app.route('/login', methods=['GET', 'POST']) 



def login():
    print_debug_info()
    username = request.form.get('username')
    password = request.form.get('password')
    print ('username=', username)
    print('password=', password)
    
    good_credentials = are_credentials_good(username, password)
    print ('good_credentials=' , good_credentials)
    # for first time user visits website
    if username is None and password is None:
        return render_template('login.html', bad_credentials = False)
    # for bad credentials
    if not good_credentials:
        return render_template('login.html', bad_credentials = True)
    # once you get good credentials
    else: 
        return create_cookie(username, password)


# print(request.cookies.get)



@app.route('/logout') 
def logout():

    # render the jinja2 template and pass the result to firefox
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    good_credentials = are_credentials_good(username, password)
#  FIXME create button on logout html using the following code:
# <button onclick="Log_out()">Log out</button>
 
    return render_template('logout.html', logged_in= good_credentials)




@app.route('/create_user') 
def create_user():
    print_debug_info()
    con = sqlite3.connect(args.db_file)
    sql = """
    SElECT username, password from users
    """
    cur_users = con.cursor()
    cur_users.execute(sql)
    for row_messages in cur_messages.fetchall():
        if username in 


    # render the jinja2 template and pass the result to firefox
    return render_template('create_user.html', logged_in= False)




@app.route('/create_message') 
def create_message():
    print_debug_info()


    username = request.cookies.get('username')
    password = request.cookies.get('password')
    good_credentials = are_credentials_good(username, password)
    return render_template('create_message.html', logged_in= good_credentials)

app.run()


# sql = """
# SELECT password FROM users  where username= ?
# """
# for row in cur.fetchall():
#     if password == row[0]:
#         return True
#     else:
#         return False 

# sql = """
# DELETE message FROM messages  where username= ?
# """