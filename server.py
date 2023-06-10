import logging
from flask import Flask

app = Flask(__name__)

count = 0

@app.route('/hello/<name>')
def hello_name(name):
    global count
    count += 1

    # Log when count is a multiple of 5
    if count % 5 == 0:
        logging.info(f'Count is a multiple of 5: {count}')

    return f'Hello, {name}! Count: {count}'

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=80)
