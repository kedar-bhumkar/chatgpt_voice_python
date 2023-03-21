from flask import Flask, render_template, request
import ChatGPT_main as C

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')
   


@app.route('/speech-to-text', methods=['GET'])
def speech_to_text():
    print('Hit')
    return C.start_chat()


if __name__ == '__main__':
    app.run(debug=True, port=8000)