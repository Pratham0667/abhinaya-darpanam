# Frontend Specification Document (FSD)

**Project:** ABHINAYA DARPANAM — AI-Powered Bharatanatyam Mudra Recognition System
**Version:** 1.0

---

## Table of Contents

## Table of Contents

1. [Purpose](#1-purpose)
2. [Frontend Objectives](#2-frontend-objectives)
3. [Target Platforms](#3-target-platforms)
4. [Technology Stack](#4-technology-stack)
5. [Frontend Architecture](#5-frontend-architecture)
6. [Screen Specifications](#6-screen-specifications)
7. [Navigation Flow](#7-navigation-flow)
8. [State Management](#8-state-management)
9. [User Interface Components](#9-user-interface-components)
10. [Component Communication](#10-component-communication)
11. [Color Scheme](#11-color-scheme)
12. [Typography](#12-typography)
13. [Responsive Design](#13-responsive-design)
14. [API Integration](#14-api-integration)
15. [Validation Rules](#15-validation-rules)
16. [Performance Requirements](#16-performance-requirements)
17. [Accessibility](#17-accessibility)
18. [Future UI Enhancements](#18-future-ui-enhancements)
19. [Conclusion](#19-conclusion)

---

## 1. Purpose

The Frontend Specification Document defines the user interface, navigation flow, screen layouts, user interactions, and frontend technologies used in the ABHINAYA DARPANAM system. The frontend provides an intuitive and responsive interface that enables users to practice Bharatanatyam mudras, receive AI-generated feedback, and track their learning progress.

---

## 2. Frontend Objectives

- Provide a simple and user-friendly interface.
- Display live camera feed for mudra recognition.
- Show AI recognition results in real time.
- Present corrective feedback visually and textually.
- Track and display user progress.
- Support responsive design for desktop and mobile devices.

---

## 3. Target Platforms

- Desktop Web Browsers
- Android Devices
- iOS Devices
- Tablets

---

## 4. Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend Framework | React.js |
| Build Tool | Vite |
| Styling | Tailwind CSS |
| Programming Language | JavaScript (ES6+) |
| Routing | React Router DOM |
| State Management | React Context API |
| API Communication | Fetch API / REST API |
| Camera Access | WebRTC |
| Mobile Application | React Native ||

---

## 5. Frontend Architecture

The frontend follows a Component-Based Architecture using React.js. Each feature of the application is divided into reusable and maintainable components.

### Main Pages

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
- Primary Button
- Input Field
- Modal
- Loader
- Camera View
- Progress Card
- Mudra Card
- Feedback Card
- User Profile Card

### Routing

Navigation between pages is handled using React Router DOM, enabling seamless client-side routing without full page reloads.


-----

## 6. Screen Specifications

### 6.1 Home Page

**Purpose:** Introduce the application.

**Components:**
- Application Logo
- Welcome Banner
- About Project
- Login Button
- Register Button
- Learn More Section

---

### 6.2 Login Screen

**Input Fields:**
- Email
- Password

**Buttons:**
- Login
- Forgot Password
- Register

**Validation:**
- Email format
- Required fields
- Password length

---

### 6.3 Registration Screen

**Fields:**
- Full Name
- Email
- Password
- Confirm Password

**Validation:**
- Required fields
- Password match
- Email uniqueness

---

### 6.4 Dashboard

**Components:**
- User Profile
- Practice Button
- Recent Sessions
- Progress Summary
- Accuracy Chart
- Navigation Menu

---

### 6.5 Practice Screen

**Components:**
- Live Camera Feed
- Hand Landmark Overlay
- Detected Mudra Name
- Confidence Score
- Recognition Status
- Start Button
- Stop Button

---

### 6.6 Feedback Screen

**Displays:**
- Recognized Mudra
- Accuracy Percentage
- Correct Finger Positions
- Incorrect Finger Positions
- Improvement Suggestions
- Try Again Button

---

### 6.7 Progress Screen

**Displays:**
- Total Practice Sessions
- Average Accuracy
- Mudra-wise Performance
- Weekly Progress Chart
- Achievement Statistics

---

### 6.8 User Profile

**Displays:**
- Name
- Email
- Practice History
- Profile Settings
- Logout

---

## 7. Navigation Flow

```
Home
│
├── Login
│    │
│    ▼
│  Dashboard
│    │
│    ├── Practice
│    │     │
│    │     ▼
│    │  AI Recognition
│    │     │
│    │     ▼
│    │  Feedback
│    │
│    ├── Progress
│    │
│    └── Profile
│
└── Register
```

## 8. State Management

The application uses React Context API for managing shared application state across components.

The following data is maintained globally:

- User Authentication
- User Profile Information
- Practice Session Details
- Recognition Results
- Camera Status
- Progress Statistics

Local component state is managed using React Hooks such as useState and useEffect wherever appropriate.


---

## 9. User Interface Components

**Buttons**
- Login
- Register
- Start Practice
- Stop Practice
- Save Progress
- Logout

**Cards**
- Mudra Information Card
- Feedback Card
- Progress Card
- User Profile Card

**Navigation**
- Home
- Dashboard
- Practice
- Progress
- Profile
- Logout

**Dialog Boxes**
- Login Error
- Recognition Complete
- Session Saved
- Logout Confirmation


## 10. Component Communication

Components communicate using React Props and Context API.

Data flows from parent components to child components through props, while shared application data such as authentication and user information is managed using Context API.

---

## 11. Color Scheme

| Element | Color |
|---|---|
| Primary | Deep Blue `#1E3A8A` |
| Secondary | Orange `#F97316` |
| Success | Green `#22C55E` |
| Warning | Yellow `#EAB308` |
| Error | Red `#EF4444` |
| Background | White `#FFFFFF` |
| Text | Dark Gray `#1F2937` |

---

## 12. Typography

- **Heading:** 28–36 px, Bold
- **Subheading:** 20–24 px
- **Body Text:** 16 px
- **Button Text:** 16 px, Medium
- **Font Family:** Poppins / Roboto / Inter

---

## 13. Responsive Design

**Desktop**
- Sidebar Navigation
- Multi-column Dashboard
- Large Camera View

**Tablet**
- Collapsible Navigation
- Medium Camera View

**Mobile**
- Bottom Navigation
- Full-width Cards
- Optimized Camera Preview
- Touch-friendly Buttons

---

## 14. API Integration
##### The React frontend communicates with the backend through RESTful APIs using the Fetch API. Data exchanged between the frontend and backend is in JSON format.
| API | Method | Purpose |
|---|---|---|
| `/api/login` | POST | User Login |
| `/api/register` | POST | User Registration |
| `/api/recognize` | POST | Mudra Recognition |
| `/api/progress` | GET | User Progress |
| `/api/profile` | GET | User Details |

---

## 15. Validation Rules

- Required fields cannot be empty.
- Email must follow valid format.
- Password must contain at least 8 characters.
- Camera permission must be granted before practice.
- Display friendly error messages for invalid input.

---

## 16. Performance Requirements

| Metric | Target |
|---|---|
| Initial page load | < 3 seconds |
| API response time | < 1 second |
| Recognition result display | < 100 ms |
| Camera feed | Smooth at 30 FPS |
| Layout | Responsive across supported devices |


#### Additional React Performance Optimizations:

- Component-based rendering
- Lazy loading of routes using React.lazy()
- Code splitting for faster page loads
- Optimized state updates
- Efficient re-rendering using React Hooks
---

## 17. Accessibility

- Responsive layouts
- Keyboard navigation support
- High-contrast color combinations
- Readable font sizes
- Clearly labeled buttons and forms
- Alternative text for icons and images where applicable

---

## 18. Future UI Enhancements

- Dark Mode
- Voice-assisted navigation
- Multi-language support
- Animated hand guidance
- 3D hand visualization
- Personalized dashboard themes
- Gamification with badges and achievements

---

## 19. Conclusion

The frontend of ABHINAYA DARPANAM is designed to deliver a clean, responsive, and interactive user experience. By combining modern web technologies with real-time AI feedback, the interface enables students and instructors to practice, evaluate, and improve Bharatanatyam mudras efficiently across desktop and mobile platforms.
