import logging
from flask import Flask

app = Flask(__name__)

count = 0

@app.route('/hello/<name>')
def hello_name(name):
    global count
    count += 1

    # Log when count reaches 5
    if count == 5:
        logging.info('Count reached 5')

    # Log when count reaches 10
    if count == 10:
        logging.info('Count reached 10')

    # Log when count reaches 25
    if count == 25:
        logging.info('Count reached 25')

    return f'Hello, {name}! Count: {count}'

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=80)
