from flask import Flask, render_template, request

import re

app = Flask(__name__)

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['text']
        extracted_emails = extract_emails(user_text)
        return render_template('result.html', emails=extracted_emails)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
