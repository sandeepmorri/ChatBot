from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = 'AIzaSyCwy9DfNeaJRGTLbHveLuAyeNYQaF7CvIw'
API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_message
                    }
                ]
            }
        ]
    }
    response = requests.post(API_URL, json=data)
    bot_reply = response.json()['candidates'][0]['content']['parts'][0]['text']
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
