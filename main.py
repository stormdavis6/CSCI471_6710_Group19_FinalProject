from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/introductions")
def introductions():
	return render_template("introductions.html")

@app.route("/motivations")
def motivations():
	return render_template("motivations.html")

if __name__ == "__main__":
	app.run(debug=True)