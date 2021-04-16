from flask  import Flask

app = Flask(__name__)

from controllers import controller

if __name__ == "__name__":
    app.run(debug=True)