# Technical Architecture Document (TAD)

**Project:** ABHINAYA DARPANAM — AI-Powered Bharatanatyam Mudra Recognition System
**Version:** 1.0

---

## Table of Contents
## Table of Contents

1. [Introduction](#1-introduction)
2. [System Overview](#2-system-overview)
3. [High-Level Architecture](#3-high-level-architecture)
4. [Architecture Layers](#4-architecture-layers)
5. [Component Architecture](#5-component-architecture)
6. [Frontend Architecture](#6-frontend-architecture)
7. [Database Architecture](#7-database-architecture)
8. [Recognition Workflow](#8-recognition-workflow)
9. [API Architecture](#9-api-architecture)
10. [Technology Stack](#10-technology-stack)
11. [Security Architecture](#11-security-architecture)
12. [Performance Requirements](#12-performance-requirements)
13. [Deployment Architecture](#13-deployment-architecture)
14. [Scalability](#14-scalability)
15. [Conclusion](#15-conclusion)

---

## 1. Introduction

**Purpose**

This Technical Architecture Document describes the overall architecture, components, technologies, workflows, and deployment strategy of the ABHINAYA DARPANAM system. It serves as a reference for developers, testers, and future contributors.

---

## 2. System Overview

ABHINAYA DARPANAM is an AI-powered real-time Bharatanatyam Mudra Recognition System that recognizes hand gestures using computer vision and provides corrective feedback to learners.

The system processes live camera input, extracts hand landmarks using MediaPipe, normalizes the data, compares it against stored reference vectors using PostgreSQL with PGVector, and generates corrective feedback.

---

## 3. High-Level Architecture

```
User
 │
 ▼
React Frontend (Vite + Tailwind CSS)
 │
 ▼
React Router
 │
 ▼
REST API (Fetch)
 │
 ▼
Flask Backend
 │
 ├───────────────┐
 ▼               ▼
MediaPipe      PostgreSQL + PGVector
(OpenCV)          Database
 │
 ▼
Mudra Recognition Engine
 │
 ▼
AI Feedback Generator
 │
 ▼
React Dashboard
```

---

## 4. Architecture Layers

### Presentation Layer

**Responsibilities**

- User Authentication
- Dashboard
- Camera Interface
- Live Recognition Screen
- AI Feedback Display
- Progress Dashboard
- Responsive User Interface

**Technology:** React.js, Vite, Tailwind CSS, React Router DOM, React Context API

---

### Application Layer

**Responsibilities**
- API Management
- Recognition Pipeline
- User Management
- Feedback Logic
- Progress Analytics

**Technology:** Python, Flask REST API

---

### AI Processing Layer

**Responsibilities**
- Hand Detection
- Landmark Extraction
- Feature Generation
- Landmark Normalization
- Similarity Computation

**Technology:** MediaPipe, OpenCV, NumPy, SciPy

---

### Data Layer

**Responsibilities**
- Store Users
- Store Mudra References
- Store Vector Embeddings
- Store Progress History

**Technology:** PostgreSQL, PGVector

---

## 5. Component Architecture

### Camera Module
- **Input:** Webcam, Smartphone Camera
- **Output:** RGB Frames

### Hand Detection Module
- **Functions:** Palm Detection, Hand Tracking, 21 Landmark Detection
- **Library:** MediaPipe Hands
- **Output:** 21 × (x, y, z) coordinates

### Geometric Normalization Module
- **Operations:** Translation Normalization, Scale Normalization, Rotation Normalization, Reflection Normalization
- **Output:** 63-dimensional normalized vector

### Recognition Module
- **Functions:** Query PGVector, Euclidean Distance, K-Nearest Neighbor Search, Confidence Calculation
- **Output:** Recognized Mudra

### Feedback Module
**Responsibilities:**
- Compare user landmarks
- Detect incorrect fingers
- Generate correction instructions
- Display visual feedback

### Progress Module
**Stores:**
- Practice Sessions
- Accuracy
- Mistakes
- Learning Trends


## 6. Frontend Architecture

The frontend follows a Component-Based Architecture using React.js.

### Pages

- Home
- Login
- Register
- Dashboard
- Practice
- Feedback
- Progress
- User Profile

### Reusable Components

- Navbar
- Footer
- Camera Component
- Mudra Card
- Feedback Card
- Progress Card
- Button
- Modal
- Loader

### State Management

- React Context API
- React Hooks (`useState`, `useEffect`, `useContext`)

### Routing

- React Router DOM

---

## 7. Database Architecture

### `Users`
- User ID
- Name
- Email
- Password

### `Mudra_Reference`
- Mudra ID
- Mudra Name
- Category
- Landmark Vector
- Description

### `Practice_History`
- Session ID
- User ID
- Mudra
- Accuracy
- Timestamp

### `Feedback_Log`
- Feedback ID
- Session ID
- Incorrect Fingers
- Suggestions

---

## 8. Recognition Workflow

1. Capture video frame.
2. Convert frame to RGB.
3. Detect hand.
4. Extract 21 landmarks.
5. Normalize landmarks.
6. Generate feature vector.
7. Query PGVector database.
8. Compute Euclidean distance.
9. Find nearest mudra.
10. Generate feedback.
11. Display results.
12. Save practice history.

---

## 9. API Architecture



The React frontend communicates with the Flask backend using REST APIs over HTTPS. All requests and responses are exchanged in JSON format.

### Authentication

- `POST /api/register`
- `POST /api/login`
- `POST /api/logout`

### Recognition

- `POST /api/recognize`

**Input**

- Camera Frame
- User ID

**Output**

- Mudra Name
- Confidence Score
- Accuracy
- AI Feedback

### Progress

- `GET /api/progress`
- `GET /api/profile`

### Mudra

- `GET /api/mudras`

---

## 10. Technology Stack

| Layer | Technologies |
|-------|--------------|
| **Frontend** | React.js, Vite, Tailwind CSS, JavaScript (ES6+), React Router DOM, React Context API |
| **Backend** | Python, Flask REST API |
| **AI / Computer Vision** | MediaPipe Hands, OpenCV, NumPy, SciPy |
| **Database** | PostgreSQL, PGVector |
| **API Communication** | REST API (JSON) |
| **DevOps** | Docker, GitHub Actions, AWS / Azure |

---

## 11. Security Architecture

The system implements multiple layers of security to protect user data and AI services.

- JWT Authentication
- Password Hashing using bcrypt
- HTTPS/TLS Communication
- Role-Based Access Control (RBAC)
- Input Validation
- SQL Injection Prevention
- Cross-Origin Resource Sharing (CORS)
- Protected React Routes
- Secure REST API Communication

---

## 12. Performance Requirements

| Parameter | Target |
|---|---|
| Recognition Accuracy | > 90% |
| End-to-End Latency | < 100 ms |
| Frame Rate | 30 FPS |
| Response Time | < 1 second |
| Database Query | < 20 ms |

---

## 13. Deployment Architecture

```
Client Browser
(React + Vite)
      │
      ▼
 REST API (HTTPS)
      │
      ▼
 Flask Backend
      │
 ┌────┴──────────┐
 ▼               ▼
MediaPipe      PostgreSQL
(OpenCV)       + PGVector
      │
      ▼
 Docker Container
      │
      ▼
 AWS / Azure Cloud
```

---

## 14. Scalability

**Future enhancements include:**
- Multiple camera support
- Full-body pose recognition
- AI choreography analysis
- AR/VR training modules
- Voice-based guidance
- Cloud synchronization
- Support for Kathak, Odissi, and Kuchipudi

---

## 15. Conclusion

The architecture of ABHINAYA DARPANAM is modular, scalable, and optimized for real-time AI inference. By integrating MediaPipe, geometric normalization, PGVector, and Flask APIs, the system delivers fast and accurate Bharatanatyam mudra recognition while remaining lightweight enough to run on standard consumer hardware.
