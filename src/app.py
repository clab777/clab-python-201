from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world! " +datetime.now().strftime("%d/%m/%Y %H:%M:%SS")

if __name__ == "__main__":
    app.run()

