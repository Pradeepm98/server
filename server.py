from flask import Flask

app = Flask(__name__)

count = 0

@app.route('/hello/<name>')
def hello_name(name):
    global count
    count += 1
    return f'Hello, {name}! Count: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
