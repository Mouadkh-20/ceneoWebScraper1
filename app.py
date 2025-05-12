from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

@app.route("/")
@app.route("/<name>")
def greeting(name="World"):
    return f"Hello{name}!"
    return render_template("index.html", name=name)