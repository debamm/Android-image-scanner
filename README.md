# Android-image-scanner

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)](https://fastapi.tiangolo.com/)
[![Android](https://img.shields.io/badge/Android-Studio-green)](https://developer.android.com/studio)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)


## 🌟 Highlights

- Real-time object detection on Android devices
- FastAPI backend with Docker containerization for easy deployment
- End-to-end machine learning pipeline from training to production
- Cloud-ready architecture with scalable inference service
- Seamless Android client integration for cloud-based AI inference

## ℹ️ Overview
This repo is created for me to learn how to develop a deployable model onto cloud service provider. The goal is to create an Android app which can do request to a server i host, where a service for inference using a simple AI is hosted. 
The key learning points of this project includes:
- Basic FastAPI & Docker use in python.
- Basic DL training. 
- Basic Android app Deployment.

# How This Repo Works
The project is splitted into 4 milestone :
- Project Week 1 - Docker + FastAPI
- Project Week 2 - Python Modeling
- Project Week 3 - Cloud Deployment
- Project Week 4 - Android Client + Documentation
each milestone covers smaller tasks which documented in the project tab. 

## Project Structure
```
android-image-scanner/
├── feature/
│   ├── main.py              # FastAPI application
│   ├── models/              # ML model files
│   ├── Dockerfile           # Docker configuration
│   └── requirements.txt      # Python dependencies
├── android-client/
│   ├── app/
│   ├── build.gradle         # Android build config
│   └── src/                 # Android source code
├── data/                    # Training data
├── notebooks/               # Jupyter notebooks for experimentation
└── README.md
```

## 📦 Installation & Setup
```
# Clone repository
git clone https://github.com/debamm/Android-image-scanner.git
cd Android-image-scanner

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## API Endpoints
list of API endpoints
# Health Check
```HTTP
localhost:8080:<#port>/health
```

# Image Detection
```HTTP
<TODO>
```

# POST /detect
```
{
  "status": "success",
  "detections": [
    {
      "class": "object_name",
      "confidence": 0.95,
      "bbox": [x, y, width, height]
    }
  ],
  "processing_time": 0.234
}
```

### ✍️ Authors
Debamm - Deep Learning solution engineer, software developer in training 🤓

TODO:
Create this two sections
## 🚀 Usage
#with docker
first build the docker image
```bash
docker build . -t <tag>
```
then you can run the container
```bash
docker run -p host:8080 <tag>
```
#using FastAPI:
```bash
fastapi run fasthello.py
```
## ⬇️ Installation

Simple, understandable installation instructions!

```bash
pip install my-package
```

And be sure to specify any other minimum requirements like Python versions or operating systems.

*You may be inclined to add development instructions here, don't.*


