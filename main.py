from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # Bind to 0.0.0.0:5000 as required
    app.run(host='0.0.0.0', port=5000)
