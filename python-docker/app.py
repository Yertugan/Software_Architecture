import os
import json
import time

from flask import Flask
 
app = Flask(__name__)
app.debug = True
 
@app.route('/health')
def health():
    return '{"status": "ok"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')
