#Q1. What is Flask Framework? What are the advantages of Flask Framework?

"""Flask is a lightweight web framework in Python.
Its advantages include simplicity, flexibility, and extensibility."""

#Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in Jupyter Notebook.


from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<h1>Hello, World!</h1>"



#Q3. What is App routing in Flask? Why do we use app routes?


"""App routing in Flask refers to defining the URLs or routes that a web application can handle.
 We use app routes to map specific URLs to functions or views within the Flask application,
 allowing users to access different pages or perform specific actions based on the requested URL."""


 #Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
#route to show the following details:
#Company Name: ABC Corporation
#Location: India
#Contact Detail: 999-999-9999
#Attach the screenshot of the output in Jupyter Notebook.



@app.route("/welcome")
def wel ():
    return "welcome to ABC Corporation "


@app.route("/")
def show ():
    return "Company Name: ABC Corporation, Location: India, Contact Detail: 999-999-9999"

if __name__=="__main__":
    app.run(host="0.0.0.0")



    #Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of theurl_for() function.


    """The `url_for()` function in Flask is used for URL building. 
    It generates a URL for a specific function or view based on the provided endpoint and any arguments passed to it."""

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/user/<username>')
def user_profile(username):
    return f'Profile Page of {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

with app.test_request_context():
    print(url_for('index'))  # Output: /

    print(url_for('user_profile', username='john'))  # Output: /user/john

    print(url_for('show_post', post_id=1))  # Output: /post/1

