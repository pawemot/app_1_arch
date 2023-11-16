from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
	return "<h1> Pierwsza aplikacja w Pythonie (Flask)123</h1>"

if __name__ == "__main__":

	app.run(host='0.0.0.0')
