from flask import Flask, render_template, request
import datetime
# from flask_sse import SSE
# sse = SSE(app)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

messages = []

def add_message(text):
    messages.append({
        'text': text,
        'timestamp': datetime.datetime.utcnow()
    })

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        add_message(request.form['message'])
    return render_template('index.html', messages=messages)
if __name__ == '__main__':
    app.run("0.0.0.0",8080,True)
