from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
	name = "바보바보바보야밥버바보바보야"
	short_name = name[0:5]
	fruits = ["apple", "pineapple", "orange", "rkrk"]

	return render_template("index.html", name=name, fruits=fruits, short_name=short_name)

@app.route("/login")
def login():
	return render_template("login.html")



if __name__ == "__main__":
	app.run(port=5000)