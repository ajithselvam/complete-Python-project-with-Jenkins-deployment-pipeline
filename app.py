from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Python Flask App!",
        "status": "running",
        "version": "1.0.0"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "python-app"
    })

@app.route('/api/info')
def info():
    return jsonify({
        "app": "Python Jenkins Deployment Demo",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "port": os.getenv("PORT", "5000")
    })

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
