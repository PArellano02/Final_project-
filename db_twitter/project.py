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
from datetime import datetime
import random

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

offset =0
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
    if username == None:
        return False 
    print(username)
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

def create_messages(offset):
    con = sqlite3.connect(args.db_file)
     
    pg_num = 0 
    if request.form.get('next_page'):
        pg_num +=1
    if request.form.get('back_page'):
        pg_num -= 1
    offset += 50 * pg_num
    messages = []
    sql = """
    SELECT sender_id,message, created_at
    FROM messages
    ORDER BY created_at DESC LIMIT 1000 OFFSET ?;
    """
    cur_messages = con.cursor()
    cur_messages.execute(sql,[offset])
    for row_messages in cur_messages.fetchall():
        id = str(row_messages[0])
        # convert sender_id into a username
        sql=  """
        SELECT username, age
        FROM users
        WHERE id= ?;
        """
        cur_users = con.cursor()
        cur_users.execute(sql,[id])
        for row_users in cur_users.fetchall():
            pass

        # build the message dictionary
        messages.append({
            'message': row_messages[1],
            'username': row_users[0],
            'age' :row_users[1],
            'posted_at' : row_messages[2],
            'prof_pic' : 'https://robohash.org/'+row_users[0], 
            })
    return messages


def create_cookie(username, password):
            template = render_template('root.html', messages=create_messages(offset), logged_in= True)
            response = make_response(template)
            response.set_cookie('username',username)
            response.set_cookie('password',password)
            return response

def log_out():
    response = make_response(render_template('logout.html'))
    response.delete_cookie('username')
    response.delete_cookie('password')
    return response
    # username = request.cookies.get('username')
    # password = request.cookies.get('password')
    # response = create_cookie(username,password)
    # response.set_cookie('unsername','')
    # response.set_cookie('password', '')
 


@app.route('/')     
def root():
    print_debug_info()
    
   
    username = request.cookies.get('username')
    password = request.cookies.get('password')

    []
    messages = create_messages(offset)
    for message in messages:
        message 

    
    # render the jinja2 template and pass the result to firefox
    good_credentials = are_credentials_good(username, password)
    return render_template('root.html', messages=create_messages(offset), logged_in= good_credentials)
# print(create_messages())



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
    return log_out()

    # render the jinja2 template and pass the result to firefox
    
#  FIXME create button on logout html using the following code:
# <button onclick="Log_out()">Log out</button>
 




@app.route('/create_user', methods=['GET', 'POST']) 
def create_user():
    print_debug_info()
    con = sqlite3.connect(args.db_file)
    cur = con.cursor()  #also dont know why this is not accesible 
    username = request.form.get('username')
    password = request.form.get('password') # IDK why this is 'password' is not accesible
    password1=request.form.get('password1')
    age = request.form.get('age')
    sql = """
    SElECT username From users
    """
    cur_users = con.cursor()
    cur_users.execute(sql) 
    con.commit() 
    cur_users.fetchall()
    if username and password:
        if username in cur_users.fetchall():
            return render_template('create_user.html', existing_credentials =True)
        else: 
            if password == password1:
                try: 
                    password=password
                    age = age
                    sql = """
                    INSERT INTO users (username, password, age) VALUES (?, ?, ?);  
                    """
                    cur.execute(sql, [username, password, age])
                    con.commit()
                    return  create_cookie(username,password)
                except:
                    return render_template('create_user.html', existing_credentials = True )
            else:
                return render_template('create_user.html', password_error = True )
    else:

        return render_template('create_user.html')







@app.route('/create_message', methods=['GET', 'POST']) 
def create_message():
    print_debug_info()

    username = request.cookies.get('username')
    password = request.cookies.get('password')
    good_credentials = are_credentials_good(username, password)
    time_stamp = datetime.now()
    new_message = request.form.get('new_message')

    if request.cookies.get('username') and request.cookies.get('password'):
        print ('inside of for if ')
        if new_message:
            print('inside of second if')
            try:
                con = sqlite3.connect('twitter_clone.db')
                cur = con.cursor()
                sql = """
                Select id from USERS where username = ?
                """
                cur.execute(sql ,[username])
                con.commit()
                for row in cur.fetchall():
                    sender_id = row[0]
                
                sql= """
                 INSERT INTO messages (sender_id, message, created_at) values (?, ?, ?);
                """
                cur.execute(sql, [sender_id, request.form.get('new_message'), time_stamp.strftime("%Y-%m-%d %H:%M:%S") ]) 
                con.commit()
                return make_response(render_template('create_message.html', message_failed = False , logged_in= good_credentials))
            except:
                return render_template('create_message.html', message_failed =True, logged_in= good_credentials)
        else: 
            return render_template('create_message.html', message_failed = False, logged_in = good_credentials)
    else:
        return login()

@app.route('/your_profile')
def your_profile():
    if(request.cookies.get('username') and request.cookies.get('password')):
        username = request.cookies.get('username')
        password =request.cookies.get('password')
        good_credentials = are_credentials_good(username, password)
        con = sqlite3.connect(args.db_file)
    
        cur_users = con.cursor()
        sql = """
        SELECT id, username, age FROM USERS where username = ?
        """
        cur_users.execute(sql, [username])
        con.commit()
        rows = cur_users.fetchall()
        for user_row in rows:
            sender_id = user_row[0]
            print('sender_id=' ,sender_id)
        cur_messages = con.cursor()
        sql = """
        SELECT message, created_at, id FROM MESSAGES where sender_id= ?  ORDER BY created_at DESC;
        """
        cur_messages.execute(sql, [sender_id])
        con.commit()
        rows = cur_messages.fetchall()
        messages = []
        for row in rows:
            messages.append({'message': row[0],
             'posted_at': row[1], 
             'id':user_row[0],
             'age' : user_row[2],
             'prof_pic' : 'https://robohash.org/'+user_row[1],
             })
        return render_template('your_profile.html', messages=messages, logged_in= good_credentials)
    else: 
        return login()

@app.route('/delete_account')
def delete_account():
        username = request.cookies.get('username')
        con = sqlite3.connect('twitter_clone.db') 
        cur_user1 = con.cursor()
        sql = """
        SELECT id FROM users where username = ?
        """
        cur_user1.execute(sql,[username])
        con.commit()
        for row_user1 in cur_user1.fetchall():
            sender_id = row_user1[0]

        cur_messages = con.cursor()
        sql= """
        DELETE from messages where sender_id = ?
        """
        cur_messages.execute(sql,[sender_id])
        con.commit()

        cur_user2 = con.cursor()
        sql = """
        DELETE from users where username= ?
        """
        cur_user2.execute(sql, [username])
        con.commit()


        return render_template('delete_account.html', logged_in = False)



@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    old_password = request.form.get('old_password')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    if old_password == None and password1 == None and password2 == None:
        return render_template('change_password.html', logged_in = are_credentials_good(username, password), blank = True)
    else:
        if old_password == request.cookies.get('password'):
            if password1 == password2:
                con = sqlite3.connect(args.db_file)
                cur = con.cursor()
                sql = """
                UPDATE users SET password = ? WHERE username = ?
                """
                cur.execute (sql, [password1, username])
                con.commit ()
                template = render_template('change_password.html', logged_in = True , changed = True)
                response = make_response(template)
                response.set_cookie('username',username)
                response.set_cookie('password',password1)
                password = request.cookies.get('password')
                return response  
            else:
                return render_template('change_password.html', logged_in = are_credentials_good(username, password), p_perror = True)
        else: 
            return render_template('change_password.html', logged_in = are_credentials_good(username, password), op_error = True )



            # Still need to automatically change cookies 

# To create 200 users
# for num in range(200):
#     con = sqlite3.connect(args.db_file)
#     cur = con.cursor()
#     username = 'Penguin0'+str(num)
    # password = 'Penguin0'+str(num)
    # age = str(num)
    # sql = """
    # INSERT INTO users (username, password, age) VALUES (?, ?, ?);
    # """
    # cur.execute(sql, [username, password, age])
    # con.commit()


#to create 40000 messages
# for num in range(200):
    
#     con = sqlite3.connect(args.db_file)
#     cur = con.cursor()
#     username = 'Penguin0'+str(num)

#     sql =  """
#     Select id from USERS where username = ?
#     """
#     cur.execute(sql ,[username])
#     con.commit()
#     for row in cur.fetchall():
#         sender_id = row[0]

#     for num in range(200):
#         time_stamp = datetime.now()
#         sender_id = sender_id
#         message = generate_comment()
#         sql= """
#         INSERT INTO messages (sender_id, message, created_at) values (?, ?, ?);
#         """
#         cur.execute(sql, [sender_id, message, time_stamp.strftime("%Y-%m-%d %H:%M:%S") ]) 
#         con.commit()



app.run(host="0.0.0.0")

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