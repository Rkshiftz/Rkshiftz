
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    ip = request.remote_addr
    with open("visitor_ips.log", "a") as log:
        log.write(f"{datetime.now()} - {ip}\n")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
