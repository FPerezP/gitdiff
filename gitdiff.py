import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'Hello from GitDiff!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)