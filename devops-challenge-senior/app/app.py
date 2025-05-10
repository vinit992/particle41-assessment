# app.py
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def root():
    # Get current UTC time in ISO format
    current_time = datetime.utcnow().isoformat()
    # Get client IP address from Flask request
    client_ip = request.remote_addr
    return {"timestamp": current_time, "ip": client_ip}

if __name__ == "__main__":
    # Run the Flask development server on all interfaces port 8000
    app.run(host="0.0.0.0", port=8000)
