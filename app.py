from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "haiii 😆"

@app.route("/greetings/<name>")
def greetings(name):
    return f"haiii, {name}! 😆😆"

if __name__ == '__main__':
    app.run(debug=True)
