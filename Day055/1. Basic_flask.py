
from flask import Flask

app = Flask(__name__)
# def make_bold(function):
#     def wrapper():
#         return "<b>" + function() + "</b>"
#     return wrapper
#
# def make_emphasis(function):
#     def wrapper():
#         return "<em>" + function() + "</em>"
#     return wrapper
#
# def make_underlined(function):
#     def wrapper():
#         return "<u>" + function() + "</u>"
#     return wrapper

# @app.route("/")
# def hello_world():
#     return "Hello, World!"

# @app.route("/bye")
# def bye():
#     return "Bye!"

# @app.route("/username/<name>")
# def greet(name):
#     return f"Welcome {name}."

# @app.route("/username/<path:name>")
# def greet(name):
#     return f"Welcome {name}."

# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Welcome {name}. You are {number} years old."

"""#Adding html attributes"""
# @app.route("/")
# def hello_world():
#     return "<h1>Hello, World!</h1>"

# @app.route("/")
# def hello_world():
#     #return '<h1 style="text-align: center">Hello, World!</h1>'
#     return '<h1 style="text-align: center">Hello, World!</h1>' \
#            '<p>This is a paragraph.</p>' \
#            '<img src="https://assets.entrepreneur.com/content/3x2/2000/20180703190744-rollsafe-meme.jpeg?width=700&crop=2:1">' \
#            '<br>' \
#            '<img src="https://media.giphy.com/media/xL7PDV9frcudO/giphy.gif">'

# @app.route("/")
# @make_underlined
# @make_emphasis
# @make_bold
# def hello_world():
#     return "Hello, World!"

"""Advanced Decorators"""
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
# new_user = User("angela")
# new_user.is_logged_in = True
# create_blog_post(new_user)

"""#Exercise"""
def decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned {result}.")
    return wrapper

@decorator
def logging_decorator(a, b, c):
    return a*b*c
logging_decorator(1, 2, 3)

if __name__ == "__main__":
    app.run(debug=True)