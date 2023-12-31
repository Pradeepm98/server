import logging
from flask import Flask
import requests
import logging
from flask import Flask, request
import assemblyai as aai


app = Flask(__name__)

count = 0

    # Log when count is a multiple of 5



app = Flask(__name__)

count = 0
def jls_extract_def():
    # Your API token is already set here
    aai.settings.api_key = "75ac6609b62e4f47a78aab3a3b6c1982"
    
    # Create a transcriber object.
    transcriber = aai.Transcriber()
    
    # If you have a local audio file, you can transcribe it using the code below.
    # Make sure to replace the filename with the path to your local audio file.
    transcript = transcriber.transcribe("./audio.mp3")
    
    return transcript.text


def download(url):
    output_filename = 'audio.mp3'
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_filename, 'wb') as file:
            file.write(response.content)
    else:
        print('Failed to download audio:', response.status_code)


@app.route('/hello', methods=['POST'])
def hello():
    global count
    count += 1

    # Access the JSON payload
    payload = request.json
    name = payload.get('name')

    download('https://'+name)
    
    return f'Hello, {name}! Count: {count} {jls_extract_def()}'

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=80)
