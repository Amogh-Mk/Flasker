from flask import Flask, render_template


# Create a Flask Instance
app=Flask(__name__)

# Create a route director
@app.route('/')

# def index():
#	return "<h1>Hello World!</h1>"

# def index():
#	return render_template("index.html")

# Some Examples Of FILTERS!!

# upper
# lower
# capitalize
# safe
# title
# trim
# striptags

def index():
	first_name = "Amogh"
	stuff = "This is <strong>Bold</strong> Text"
	favourite_pizza = ["Pepperoni", "Cheese", "Mushrooms", "41"]
	return render_template("index.html", first_name=first_name, stuff=stuff, favourite_pizza=favourite_pizza)

# localhost:5000/user/name (in my case Amogh)
@app.route('/user/<name>')

# def user(name):
#	return "<h1>Hello {}</h1>".format(name)

def user(name):
    return render_template("user.html", user_name=name)

# Create Custom Error Pages

# Invalid URL (404)
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error (500)
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500