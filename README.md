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

From the `particle41-assessment` project root directory:
```docker build -t simpletimeservice ./app```

To Tag image with Docker Hub username
`docker tag simpletimeservice gabbarjarwar/simpletimeservice:latest`

Push image to the docker hub
`docker push gabbarjarwar/simpletimeservice:latest`

Pull image from Docker Hub
`docker pull gabbarjarwar/simpletimeservice:latest`

Run the container
`docker run -d -p 8000:8000 --name simpletimeservice gabbarjarwar/simpletimeservice:latest`


Or You can also run it directly after build:
`docker run -p 8000:8000 simpletimeservice`

Test the API
`curl http://127.0.0.1:8000/`

Expected Output
`{"ip":"172.17.0.1","timestamp":"2025-05-10T09:55:44.557433"}`

Stop and remove the container
`docker stop simpletimeservice`
`docker rm simpletimeservice`

Non-Root Container
This container uses a dedicated non-root user `(appuser)` for enhanced security:

Created using `useradd` and `groupadd`

File permissions adjusted via `chown`

`USER appuser` enforces non-root execution


Project Structure

particle41-assessment/devops-challenge-senior/
├── app/
│   ├── app.py             # Flask app
│   ├── Dockerfile         # Docker build file
│   ├── requirements.txt   # Python dependencies
├── README.md              # Project instructions
