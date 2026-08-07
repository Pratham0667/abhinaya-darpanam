<div align="center">

#  ABHINAYA DARPANAM
### AI-Powered Bharatanatyam Mudra Recognition System

<p align="center">
An AI-powered learning platform that recognizes Bharatanatyam mudras in real time using Computer Vision, MediaPipe Hands, and PostgreSQL PGVector while providing instant corrective feedback to students.
</p>

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react)
![Flask](https://img.shields.io/badge/Flask-REST_API-black?style=for-the-badge&logo=flask)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-4-38BDF8?style=for-the-badge&logo=tailwindcss)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-Academic-green?style=for-the-badge)

</div>

---

# 📖 Overview

**ABHINAYA DARPANAM** : is an Artificial Intelligence powered educational platform designed to assist Bharatanatyam students in practicing hand mudras independently.

The application captures hand movements using a webcam or smartphone camera, extracts hand landmarks through **MediaPipe Hands**, performs geometric normalization, compares the generated feature vector against stored reference vectors using **PostgreSQL + PGVector**, and instantly provides corrective feedback.

Unlike conventional learning methods that require continuous supervision by an instructor, ABHINAYA DARPANAM enables students to receive **real-time AI-based evaluation**, improving learning efficiency while preserving the rich heritage of Indian classical dance.

---

# 🎯 Objectives

The primary objectives of the project are:

- Recognize 28 Bharatanatyam Mudras.
- Achieve more than **90% recognition accuracy**.
- Provide real-time AI feedback.
- Detect incorrect finger positions.
- Track individual learning progress.
- Assist students in self-practice.
- Reduce dependency on continuous instructor supervision.
- Preserve Bharatanatyam knowledge using Artificial Intelligence.

---

# ✨ Key Features

### 👤 User Management

- Secure Registration
- Login & Logout
- JWT Authentication
- User Profiles

---

### 🎥 Camera Module

- Webcam Support
- Mobile Camera Support
- Live Camera Preview
- Real-Time Frame Capture

---

### 🤖 AI Recognition

- MediaPipe Hand Detection
- 21 Hand Landmark Detection
- Landmark Normalization
- 63-Dimensional Feature Vector Generation
- PGVector Similarity Search
- Confidence Score Calculation

---

###  Bharatanatyam Learning

- Real-Time Mudra Recognition
- AI-Based Corrective Feedback
- Finger Position Analysis
- Palm Orientation Analysis
- Improvement Suggestions

---

### 📈 Analytics

- Practice History
- Recognition Accuracy
- Weekly Progress
- Learning Statistics
- Performance Dashboard

---

### 🔒 Security

- JWT Authentication
- Password Hashing (bcrypt)
- HTTPS Communication
- Role-Based Access Control
- Secure REST APIs

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Frontend | React.js |
| Build Tool | Vite |
| Styling | Tailwind CSS |
| Programming Language | JavaScript (ES6+) |
| Backend | Python Flask |
| AI Framework | MediaPipe Hands |
| Computer Vision | OpenCV |
| Scientific Computing | NumPy, SciPy |
| Database | PostgreSQL |
| Vector Database | PGVector |
| Authentication | JWT |
| Password Security | bcrypt |
| API | REST API |
| Containerization | Docker |
| Version Control | Git & GitHub |
| Deployment | AWS / Azure |

---

# 🏗 System Architecture

```text
                        User
                          │
                          ▼
                 React Frontend (Vite)
                          │
                 React Router DOM
                          │
                    REST API (JSON)
                          │
                          ▼
                   Flask Backend
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
     Authentication   AI Recognition   Progress
           │              │              │
           │        MediaPipe Hands      │
           │              │              │
           │          OpenCV Frames      │
           │              │              │
           │      Landmark Extraction    │
           │              │              │
           │      Geometric Normalization
           │              │
           │        Feature Vector
           │              │
           └──────────────┼──────────────┘
                          ▼
                PostgreSQL + PGVector
                          │
                          ▼
               Similarity Matching Engine
                          │
                          ▼
                  AI Feedback Generator
                          │
                          ▼
                React Dashboard Interface
```

---

# 🧠 AI Recognition Pipeline

```text
Camera
   │
   ▼
Frame Capture
   │
   ▼
MediaPipe Hands
   │
   ▼
21 Landmark Extraction
   │
   ▼
Landmark Normalization
   │
   ▼
63-Dimensional Feature Vector
   │
   ▼
PGVector Similarity Search
   │
   ▼
Nearest Mudra Detection
   │
   ▼
Confidence Calculation
   │
   ▼
Corrective Feedback
   │
   ▼
Dashboard Update
```

---



# 📚 Documentation

The project documentation includes:

- 📄 Product Requirements Document (PRD)
- 📄 Software Requirements Specification (SRS)
- 📄 Frontend Specification Document (FSD)
- 📄 Technical Architecture Document (TAD)
- 📄 Security & Access Document (SAD)
- 📄 Feature Ticket List
- 📄 API Documentation

---

# 🚀 Why This Project?

Traditional Bharatanatyam training relies heavily on expert instructors, making continuous personalized guidance difficult.

ABHINAYA DARPANAM bridges this gap by combining **Artificial Intelligence**, **Computer Vision**, and **Vector Similarity Search** to create an intelligent learning assistant capable of recognizing mudras, evaluating performance, and providing instant corrective feedback.

The system enables learners to practice anytime, anywhere, using only a standard webcam or smartphone camera while preserving the authenticity of Bharatanatyam through technology.

---


# ⚙️ Installation Guide

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

| Software | Version |
|-----------|----------|
| Node.js | 20+ |
| npm | Latest |
| Python | 3.11+ |
| PostgreSQL | 15+ |
| Git | Latest |
| Docker *(Optional)* | Latest |

Verify your installations:

```bash
node -v
npm -v
python --version
psql --version
git --version
```

---

# 📥 Clone the Repository

```bash
git clone https://github.com/your-username/ABHINAYA-DARPANAM.git
```

Navigate into the project directory:

```bash
cd ABHINAYA-DARPANAM
```

---




# 🌐 Frontend Setup

Navigate to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The React application will be available at:

```
http://localhost:5173
```

---

# 🐍 Backend Setup

Open a new terminal.

Navigate to the backend folder:

```bash
cd backend
```

Create a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask server:

```bash
python app.py
```

The backend server will run at:

```
http://localhost:5000
```

---

# 🗄 Database Setup

Start PostgreSQL.

Create a new database:

```sql
CREATE DATABASE abhinaya_darpanam;
```

Enable the PGVector extension:

```sql
CREATE EXTENSION vector;
```

Run the database migration scripts:

```bash
python migrate.py
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend directory.

```env
SECRET_KEY=your-secret-key

JWT_SECRET_KEY=your-jwt-secret

DATABASE_URL=postgresql://username:password@localhost:5432/abhinaya_darpanam

FLASK_ENV=development

UPLOAD_FOLDER=uploads

MAX_CONTENT_LENGTH=16777216
```

---

# ▶️ Running the Complete Application

### Start PostgreSQL

↓

### Start Backend

```bash
python app.py
```

↓

### Start Frontend

```bash
npm run dev
```

↓

Open

```
http://localhost:5173
```

---

# 🧪 Development Workflow

```
Developer
    │
    ▼
React Frontend
    │
    ▼
REST API
    │
    ▼
Flask Backend
    │
    ▼
MediaPipe Recognition
    │
    ▼
PostgreSQL + PGVector
```

---

# 📸 Application Workflow

```
User Login
      │
      ▼
Dashboard
      │
      ▼
Start Practice
      │
      ▼
Camera Access
      │
      ▼
Hand Detection
      │
      ▼
Landmark Extraction
      │
      ▼
Mudra Recognition
      │
      ▼
AI Feedback
      │
      ▼
Save Session
      │
      ▼
Progress Dashboard
```

---

# 🛡 Authentication Flow

```
Register
   │
   ▼
Hash Password (bcrypt)
   │
   ▼
Store User
   │
   ▼
Login
   │
   ▼
Verify Password
   │
   ▼
Generate JWT
   │
   ▼
React Stores Token
   │
   ▼
Authenticated API Requests
```

---

# 📱 Supported Platforms

- ✅ Windows
- ✅ Linux
- ✅ macOS
- ✅ Android (Web Browser)
- ✅ iOS (Safari / Chrome)
- ✅ Tablets
- ✅ Desktop Browsers

---

# 🌍 Browser Compatibility

| Browser | Supported |
|----------|-----------|
| Google Chrome | ✅ |
| Microsoft Edge | ✅ |
| Mozilla Firefox | ✅ |
| Safari | ✅ |
| Opera | ✅ |

---

# 📊 Performance Targets

| Metric | Target |
|---------|---------|
| Recognition Accuracy | >90% |
| Recognition Latency | <100 ms |
| API Response Time | <1 sec |
| Camera Frame Rate | 30 FPS |
| Initial Page Load | <3 sec |
| Database Query | <20 ms |

---

# 🧰 Recommended VS Code Extensions

- ESLint
- Prettier
- Tailwind CSS IntelliSense
- Python
- Pylance
- PostgreSQL
- Docker
- GitLens
- Error Lens
- Thunder Client

---

# 📦 Useful Commands

### Frontend

```bash
npm install
npm run dev
npm run build
npm run preview
```

### Backend

```bash
pip install -r requirements.txt

python app.py
```

### Git

```bash
git pull

git add .

git commit -m "message"

git push
```

---

# 🐳 Docker (Optional)

Build the Docker image:

```bash
docker build -t abhinaya-darpanam .
```

Run the container:

```bash
docker run -p 5000:5000 abhinaya-darpanam
```

---

# 📝 Notes

- Allow camera permissions in your browser before starting practice.
- Ensure PostgreSQL and the `pgvector` extension are installed and running.
- Use a well-lit environment for better hand detection and recognition accuracy.
- Keep your dependencies updated for security and performance improvements.

---

# 🔌 API Documentation

The frontend communicates with the backend using RESTful APIs over HTTPS. All requests and responses are exchanged in **JSON** format.

---

## Authentication APIs

### Register

```http
POST /api/register
```

#### Request

```json
{
  "name": "Pratham Pai",
  "email": "pratham@example.com",
  "password": "********"
}
```

#### Response

```json
{
  "success": true,
  "message": "User registered successfully."
}
```

---

### Login

```http
POST /api/login
```

#### Request

```json
{
  "email": "pratham@example.com",
  "password": "********"
}
```

#### Response

```json
{
  "token": "JWT_TOKEN",
  "user": {
    "id": 1,
    "name": "Pratham Pai"
  }
}
```

---

### Logout

```http
POST /api/logout
```

---

## Recognition API

```http
POST /api/recognize
```

### Input

- Camera Frame
- User ID

### Response

```json
{
  "mudra": "Tripataka",
  "confidence": 96.82,
  "accuracy": 95.60,
  "feedback": [
    "Straighten your index finger.",
    "Raise the thumb slightly."
  ]
}
```

---

## Progress API

```http
GET /api/progress
```

Returns:

- Practice History
- Accuracy
- Recent Sessions
- Performance Statistics

---

## Profile API

```http
GET /api/profile
```

Returns:

- User Information
- Practice Summary
- Achievement Statistics

---

## Mudra API

```http
GET /api/mudras
```

Returns:

- Mudra Name
- Description
- Category
- Reference Image

---

# 🤖 AI Recognition Pipeline

The AI pipeline follows a sequence of computer vision and machine learning operations.

```
Camera
   │
   ▼
Frame Capture
   │
   ▼
RGB Conversion
   │
   ▼
MediaPipe Hands
   │
   ▼
21 Landmark Detection
   │
   ▼
Landmark Normalization
   │
   ▼
63-Dimensional Feature Vector
   │
   ▼
PGVector Similarity Search
   │
   ▼
Nearest Mudra Selection
   │
   ▼
Confidence Calculation
   │
   ▼
Corrective Feedback
   │
   ▼
Dashboard Update
```

---

# 🗄 Database Schema

## Users

| Column | Type |
|----------|------|
| id | Integer |
| name | Text |
| email | Text |
| password | Text |
| created_at | Timestamp |

---

## Mudra Reference

| Column | Type |
|----------|------|
| id | Integer |
| mudra_name | Text |
| category | Text |
| landmark_vector | Vector(63) |
| description | Text |

---

## Practice History

| Column | Type |
|----------|------|
| id | Integer |
| user_id | Integer |
| mudra | Text |
| confidence | Float |
| accuracy | Float |
| practiced_at | Timestamp |

---

## Feedback Log

| Column | Type |
|----------|------|
| id | Integer |
| session_id | Integer |
| feedback | Text |
| created_at | Timestamp |

---

# 📂 Documentation

The project includes complete software engineering documentation.

| Document | Description |
|-----------|-------------|
| PRD | Product Requirements Document |
| SRS | Software Requirements Specification |
| FSD | Frontend Specification Document |
| TAD | Technical Architecture Document |
| SAD | Security & Access Document |
| Feature Tickets | Development Roadmap |

---

# 🧪 Testing Strategy

## Functional Testing

- User Registration
- Login
- Camera Access
- Recognition
- Dashboard
- Progress Tracking

---

## API Testing

- Authentication APIs
- Recognition APIs
- Progress APIs
- Profile APIs

---

## UI Testing

- Responsive Layout
- Navigation
- Forms
- Error Messages

---

## Browser Testing

- Chrome
- Firefox
- Edge
- Safari

---

## Performance Testing

- Recognition Latency
- Database Queries
- API Response
- Frontend Rendering

---

# 📸 Screenshots

## Home Page

> *later*

---

## Login

> *later*

---

## Dashboard

> *later*

---

## Live Recognition

> *later*

---

## AI Feedback

> *later*

---

## Progress Dashboard

> *later*

---




# 🔒 Security Features

- JWT Authentication
- Password Hashing (bcrypt)
- HTTPS/TLS Communication
- Role-Based Access Control (RBAC)
- Protected React Routes
- Input Validation
- SQL Injection Prevention
- Secure REST APIs
- CORS Configuration

---



# 📚 References

- MediaPipe Hands Documentation
- OpenCV Documentation
- Flask Documentation
- React Documentation
- PostgreSQL Documentation
- PGVector Documentation

---

# 🙏 Acknowledgements

We express our sincere gratitude to:

- Canara Engineering College, Mangalore
- Department of Computer Science & Design
- Project Guide and Faculty Members
- Open Source Community
- Google MediaPipe Team
- PostgreSQL Community
- React Community
- Flask Community

---

# 👥 Project Team

This project was developed as part of the **Bachelor of Engineering (B.E.) Final Year Project**.

|# 👥 Project Team

- Pratham Pai
- Ved N. Pattar
- Anvesha U. Shetty
- Sowjanya

## 🎓 Project Guide

Mr. Anantha Krishna Kamath  
Assistant Professor  
Department of Computer Science & Design  
Canara Engineering College, Mangalore
---

# 🤝 Contributing

We welcome contributions that improve the project.

## Contribution Workflow

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

Example:

```bash
git checkout -b feature/new-feature

git add .

git commit -m "Add new feature"

git push origin feature/new-feature
```

---

# 📋 Coding Standards

### Frontend

- React.js
- Functional Components
- React Hooks
- Tailwind CSS
- Component-Based Architecture
- ESLint & Prettier

### Backend

- Python
- Flask
- RESTful API Design
- Modular Architecture

### Database

- PostgreSQL
- PGVector
- Parameterized Queries

---

# 📂 Branch Strategy

```
main
│
├── development
│
├── frontend
│
├── backend
│
├── ai-recognition
│
├── documentation
│
└── testing
```

---

# 📌 Git Commit Convention

Examples

```text
feat: Add mudra recognition

fix: Resolve camera initialization issue

docs: Update README

refactor: Optimize recognition pipeline

style: Improve dashboard layout

test: Add authentication tests
```

---




# 🏆 Project Highlights

✔ AI-Powered Bharatanatyam Mudra Recognition

✔ Real-Time Computer Vision

✔ MediaPipe Hand Landmark Detection

✔ PostgreSQL + PGVector Similarity Search

✔ React.js Frontend

✔ Flask REST API Backend

✔ Docker Ready

✔ Scalable Architecture

✔ Responsive Design

✔ Industry-Standard Documentation

---

# 📊 Project Statistics

| Category | Details |
|----------|----------|
| Programming Languages | JavaScript, Python |
| Frontend Framework | React.js |
| Backend Framework | Flask |
| AI Libraries | MediaPipe, OpenCV |
| Database | PostgreSQL + PGVector |
| Documentation | PRD, SRS, FSD, TAD, SAD, Feature Tickets |
| Recognition Accuracy Target | ≥ 90% |
| Recognition Latency | < 100 ms |
| Supported Mudras | 28 |
| Supported Platforms | Desktop, Mobile, Tablet |

---

# 📜 License

This project is developed for **academic and educational purposes** as part of the Bachelor of Engineering curriculum.

Copyright © 2026

Permission is granted to use this project for learning, research, and academic reference with proper attribution.

---

# 🛡 Disclaimer

This project is intended for educational and research purposes.

The recognition accuracy may vary depending on:

- Lighting conditions
- Camera quality
- Hand positioning
- Background complexity
- Occlusion of fingers

This application is designed to assist Bharatanatyam learners and is **not intended to replace professional dance instruction**.

---

# 📞 Contact

### Project Team

**Project Name**

**ABHINAYA DARPANAM — AI-Powered Bharatanatyam Mudra Recognition System**

**Institution**

Canara Engineering College  
Mangalore, Karnataka, India

For academic queries, suggestions, or collaboration, please contact the project team through the repository issues section.

---

# ⭐ Support the Project

If you found this project useful:

⭐ Star this repository

🍴 Fork the repository

🐞 Report issues

💡 Suggest improvements

🤝 Contribute to the project

---

<div align="center">

# 🩰 ABHINAYA DARPANAM

### Preserving Indian Classical Dance through Artificial Intelligence

**Built with ❤️ using React, Flask, MediaPipe, OpenCV & PostgreSQL**

---

### Thank you for visiting our project!

⭐ **Don't forget to Star the Repository!** ⭐

</div>