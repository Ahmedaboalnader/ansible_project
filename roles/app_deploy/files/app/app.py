from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    app_version = os.environ.get('APP_VERSION', 'unknown')
    return f"<h1>Hello from the App!</h1><p>Version: {app_version}</p><p>Hostname: {os.uname()[1]}</p>"

@app.route('/health')
def health():
    return jsonify(status="ok", version=os.environ.get('APP_VERSION', 'unknown'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
