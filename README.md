# 🕒 SimpleTimeService

A minimalist Python microservice that returns the client's IP address and the current UTC timestamp in JSON format.

---

## 🔧 Tech Stack

- Python 3.11 (Flask)
- Docker (non-root user)
- RESTful microservice

---

## 📦 Docker Instructions

### ✅ Build the image

From the `simple-time-service` project root directory:
```docker build -t simpletimeservice ./app```

Pull image from Docker Hub

`docker pull gabbarjarwar/simpletimeservice:latest`

Run the container
`docker run -d -p 8000:8000 --name simpletimeservice gabbarjarwar/simpletimeservice:latest`

Stop and remove the container
`docker stop simpletimeservice`
`docker rm simpletimeservice`

Project Structure

particle41-assessment/devops-test-senior/
├── app/
│   ├── app.py             # Flask app
│   ├── Dockerfile         # Docker build file
│   ├── requirements.txt   # Python dependencies
├── README.md              # Project instructions
