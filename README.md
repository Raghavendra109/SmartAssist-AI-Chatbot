  SmartAssist AI Chatbot

SmartAssist is an AI-powered, retrieval-based chatbot developed using Python and Flask. It provides instant responses to user questions through an interactive web interface.

The chatbot uses a predefined knowledge base and Wikipedia search fallback to help answer general questions.

  Live Demo

http://13.55.92.6/chatbot/

  Project Overview

The main objective of this project is to develop a simple and interactive chatbot that can understand user queries and provide relevant answers.

 Features

- Interactive chatbot interface.
- Retrieval-based response system.
- Predefined knowledge base.
- Wikipedia search fallback.
- Animated chatbot responses.
- Typing indicator.
- Responsive web interface.
- Cloud deployment using AWS EC2.

  Technologies Used

Technology| Purpose
Python| Backend programming
Flask| Web application framework
HTML5| Webpage structure
CSS3| Styling and animations
JavaScript| Frontend interaction
Requests| HTTP requests
AWS EC2| Cloud hosting
Ubuntu Linux| Server operating system
Nginx| Reverse proxy
Gunicorn| Python application server
Git & GitHub| Version control

  Project Structure

SmartAssist-AI-Chatbot/
│
├── chat.py
│
├── templates/
│   └── index.html
│
└── README.md
  
  Installation and Setup

1. Clone the repository

git clone https://github.com/Raghavendra109/SmartAssist-AI-Chatbot.git

2. Navigate to the project

cd SmartAssist-AI-Chatbot

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:

venv\Scripts\activate

Linux:

source venv/bin/activate

5. Install dependencies

pip install flask requests gunicorn

6. Run the application

gunicorn --bind 127.0.0.1:5001 chat:app

☁️ Cloud Deployment

The application is deployed on AWS EC2 using:

1. AWS EC2 – Cloud server.
2. Ubuntu – Operating system.
3. Gunicorn – Application server.
4. Nginx – Reverse proxy.
5. Systemd – Background service management.

  Project Objective

To develop a user-friendly chatbot capable of answering general questions through a retrieval-based approach and provide an accessible web-based interface.

  Developer

Raghavendra

BCA Graduate | Python Developer | Cloud Engineering & DevOps Learner

GitHub: https://github.com/Raghavendra109

---

  If you find this project useful, consider giving the repository a star!