# Product Requirements Document (PRD)

**Product Name:** ABHINAYA DARPANAM — AI-Powered Bharatanatyam Mudra Recognition System
**Version:** 1.0
**Prepared By:** Pratham Pai, Anantha Krishna Kamath, Ved N Pattar, Anvesha U Shetty, sowjanaya

---

## Table of Contents

1. [Product Overview](#1-product-overview)
2. [Problem Statement](#2-problem-statement)
3. [Goals](#3-goals)
4. [Target Users](#4-target-users)
5. [User Stories](#5-user-stories)
6. [Functional Requirements](#6-functional-requirements)
7. [Non-Functional Requirements](#7-non-functional-requirements)
8. [System Features](#8-system-features)
9. [Technology Stack](#9-technology-stack)
10. [Product Workflow](#10-product-workflow)
11. [Success Metrics](#11-success-metrics)
12. [Future Enhancements](#12-future-enhancements)
13. [Risks](#13-risks)
14. [Acceptance Criteria](#14-acceptance-criteria)

---

## 1. Product Overview

ABHINAYA DARPANAM is an AI-powered educational platform designed to recognize Bharatanatyam mudras in real time using computer vision. The system provides instant corrective feedback, enabling students to practice independently without requiring continuous supervision from a dance instructor.

The application uses MediaPipe hand landmark detection, geometric normalization, PostgreSQL with PGVector, and vector similarity matching to recognize 28 Bharatanatyam mudras accurately.

---

## 2. Problem Statement

Traditional Bharatanatyam training depends heavily on expert instructors. Students practicing independently often:

- Receive delayed feedback.
- Repeat mistakes unknowingly.
- Have limited access to qualified gurus.
- Spend excessive time reviewing practice videos.
- Lack objective evaluation of hand gestures.

There is currently no affordable, real-time AI system capable of recognizing mudras while providing instant corrective guidance.

---

## 3. Goals

The product aims to:

- Recognize 28 Bharatanatyam mudras accurately.
- Achieve more than 90% recognition accuracy.
- Process gestures in real time.
- Provide instant AI-based corrective feedback.
- Work using a standard webcam or smartphone.
- Deliver a responsive React-based user interface.
- Support secure user authentication and profile management.
- Support cross-platform accessibility.
- Preserve Indian cultural heritage through Artificial Intelligence.

---

## 4. Target Users

**Primary Users**
- Bharatanatyam students
- Dance beginners
- Professional dancers

**Secondary Users**
- Dance instructors
- Dance academies
- Cultural institutions
- Researchers

---

## 5. User Stories

**Student**
- I want the system to recognize my mudra.
- I want immediate correction.
- I want to monitor my learning progress.

**Teacher**
- I want to review student performance.
- I want objective feedback for students.
- I want progress reports.

**Administrator**
- Manage users.
- Maintain mudra database.
- Update reference samples.

---

## 6. Functional Requirements

### FR1 — User Authentication
- Register
- Login
- Logout

### FR2 — Camera Module
- Webcam support
- Mobile camera support
- Live video preview

### FR3 — Hand Detection
- Detect one or two hands
- Extract 21 hand landmarks
- Track hands continuously

### FR4 — Mudra Recognition
- Normalize landmarks
- Compare with reference database
- Identify nearest mudra
- Display confidence score

### FR5 — Corrective Feedback
System should provide:
- Finger corrections
- Palm orientation corrections
- Overall accuracy
- Improvement suggestions

### FR6 — Progress Tracking
Store:
- Practice history
- Accuracy
- Frequently mistaken mudras
- Improvement statistics

### FR7 — Mudra Database
Store:
- Mudra name
- Landmark vectors
- Reference images
- Descriptions
- Categories

### FR8 — Dashboard
Display:
- Current mudra
- Accuracy
- Practice duration
- Performance charts

### FR9 — Frontend Navigation

The system shall:

- Provide client-side routing using React Router DOM.
- Protect authenticated routes after successful login.
- Maintain application state using React Context API.
- Ensure smooth navigation without full page reloads.

---

## 7. Non-Functional Requirements

| Category | Requirements |
|---|---|
| **Performance** | Recognition latency < 100 ms · 30 FPS processing · High responsiveness |
| **Accuracy** | Target accuracy > 90% |
| **Scalability** | Support future mudras · Support additional dance forms |
| **Security** | Secure authentication · Protected user data · Safe database access |
| **Reliability** | Stable recognition · Continuous tracking · Error recovery |
| **Usability** | Beginner-friendly interface · Simple navigation · Responsive design |

---

### 8. System Features

- User Registration and Authentication
- Real-time mudra recognition
- AI-based corrective feedback
- Vector similarity search using PGVector
- MediaPipe hand landmark detection
- Live camera integration
- Recognition confidence score
- Progress analytics dashboard
- Responsive React-based user interface
- Cross-platform browser support
- Offline-capable recognition
---

## 9. Technology Stack

| Layer | Technologies |
|-------|--------------|
| **Frontend** | React.js, Vite, Tailwind CSS, JavaScript (ES6+), React Router DOM |
| **Backend** | Python, Flask |
| **AI / Computer Vision** | MediaPipe Hands, OpenCV, NumPy, SciPy |
| **Database** | PostgreSQL, PGVector |
| **API Communication** | REST API (JSON) |
| **Deployment** | Docker, GitHub Actions, AWS / Azure ||

---

## 10. Product Workflow

1. User opens the React web application.
2. User registers or logs into the system.
3. Camera permission is requested.
4. Live camera feed starts.
5. MediaPipe detects one or two hands.
6. Hand landmarks are extracted.
7. Landmark coordinates are normalized.
8. PGVector performs vector similarity matching.
9. The closest Bharatanatyam mudra is identified.
10. AI generates confidence score and corrective feedback.
11. Recognition results are displayed to the user.
12. Practice session is saved to the database.
13. User progress is updated on the dashboard.
---

## 11. Success Metrics

- Recognition Accuracy ≥ 90%
- Latency < 100 ms
- 30 FPS processing
- User Satisfaction ≥ 4.5/5
- Faster learning compared with traditional practice

---

## 12. Future Enhancements

- Full-body pose recognition
- Multiple camera support
- AR guidance
- VR training
- Voice assistant
- Emotion recognition
- Cloud synchronization
- Additional Indian classical dance forms

---

## 13. Risks

- Poor lighting
- Finger occlusion
- Similar mudra confusion
- Camera quality limitations
- Rapid hand movement

---

## 14. Acceptance Criteria

The product will be considered successful if it:

- Correctly recognizes at least 28 mudras.
- Achieves more than 90% accuracy.
- Responds within 100 milliseconds.
- Provides meaningful corrective feedback.
- Operates on consumer hardware without specialized equipment.
- Successfully stores user practice history.
