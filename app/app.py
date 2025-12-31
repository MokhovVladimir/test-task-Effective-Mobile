from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Effective Mobile!"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ["PORT_APP"])
    )
