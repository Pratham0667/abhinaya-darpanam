# Security and Access Document (SAD)

**Project:** ABHINAYA DARPANAM — AI-Powered Bharatanatyam Mudra Recognition System
**Version:** 1.0

---


## Table of Contents

1. [Purpose](#1-purpose)
2. [Security Objectives](#2-security-objectives)
3. [User Roles and Access Levels](#3-user-roles-and-access-levels)
4. [Authentication](#4-authentication)
5. [Authorization](#5-authorization)
6. [Data Security](#6-data-security)
7. [Database Security](#7-database-security)
8. [API Security](#8-api-security)
9. [Communication Security](#9-communication-security)
10. [Frontend Security (React)](#10-frontend-security-react)
11. [Access Control Matrix](#11-access-control-matrix)
12. [Threat Analysis](#12-threat-analysis)
13. [Backup and Recovery](#13-backup-and-recovery)
14. [Audit and Monitoring](#14-audit-and-monitoring)
15. [Compliance](#15-compliance)
16. [Conclusion](#16-conclusion)

---

## 1. Purpose

This document defines the security policies, authentication mechanisms, authorization rules, data protection measures, and access control implemented in the ABHINAYA DARPANAM system. The objective is to ensure confidentiality, integrity, and availability of user information and AI-generated recognition data.

---

## 2. Security Objectives

- Protect user accounts and personal information.
- Secure communication between client and server.
- Prevent unauthorized access to system resources.
- Maintain integrity of mudra reference data.
- Ensure privacy of captured camera images.
- Protect the database against unauthorized modification.
- Maintain availability of the application.

---

## 3. User Roles and Access Levels

| Role | Permissions |
|---|---|
| **Guest** | View home page and project information only |
| **Registered Student** | Login, practice mudras, receive feedback, view progress |
| **Dance Instructor** | View student progress, analyze performance, manage learning activities |
| **Administrator** | Full access to users, mudra database, analytics, and system settings |

---

## 4. Authentication

### User Registration

Users register using:

- Full Name
- Email Address
- Password

Passwords are securely hashed using bcrypt before being stored in the database.

### Login

Authentication uses:

- Email
- Password

Upon successful authentication, the backend generates a secure JSON Web Token (JWT), which is returned to the React frontend. The frontend securely stores the authentication token and includes it in authorized API requests.

### Password Security

- Passwords are hashed using bcrypt.
- Plain-text passwords are never stored.
- Minimum password length: 8 characters.
- Password reset is available through registered email.
- Strong password validation is enforced during registration.

---

## 5. Authorization

The system implements **Role-Based Access Control (RBAC)** using JWT-based authentication.

Protected routes are secured on both the backend and the React frontend. Users can only access resources permitted by their assigned role.

### Student

**Allowed to:**

- Practice mudras
- Receive AI feedback
- View personal history
- Update personal profile

**Cannot:**

- Modify reference mudras
- Access other users' data
- View administrative settings

### Instructor

**Allowed to:**

- Review assigned students
- View performance reports
- Monitor student progress

**Cannot:**

- Delete users
- Modify system settings

### Administrator

**Allowed to:**

- Manage users
- Manage mudra database
- Update reference vectors
- View analytics
- Configure the system
- Manage backups

----


## 6. Data Security

### User Data
Stored securely:
- Name
- Email
- Practice history
- Recognition statistics

Sensitive information is encrypted or hashed where applicable.

### Camera Data
- Camera frames are processed in real time.
- Images are not permanently stored unless explicitly enabled.
- Temporary frames are deleted after processing.

### Mudra Reference Data
Stored securely:
- Mudra name
- Landmark vectors
- Descriptions
- Categories

Only administrators may update the reference dataset.

---

## 7. Database Security

**Database:** PostgreSQL with PGVector

Security measures include:
- Strong administrator credentials
- Restricted database access
- Principle of least privilege
- Regular backups
- Input validation
- SQL injection protection using parameterized queries

---

## 8. API Security

All REST APIs implement:

- JWT Authentication
- Role-Based Authorization
- Input Validation
- JSON Request Validation
- Secure Error Handling
- Rate Limiting (Recommended)
- CORS Configuration
- Parameterized Database Queries

**Example Secured Endpoints**

| Endpoint | Method | Access |
|----------|--------|--------|
| `/api/login` | POST | Public |
| `/api/register` | POST | Public |
| `/api/profile` | GET | Authenticated User |
| `/api/progress` | GET | Authenticated User |
| `/api/recognize` | POST | Authenticated User |
| `/api/admin/users` | GET | Administrator |

---

## 9. Communication Security

The application ensures secure communication through:

- HTTPS encryption
- TLS 1.2 or higher
- Secure REST API communication
- JWT Bearer Authentication
- CORS Policy Configuration
- Secure HTTP Headers

---

---
## 10. Frontend Security (React)

The React frontend implements the following security measures:

- Protected Routes using React Router DOM
- Authentication State managed through React Context API
- Secure API requests using JWT Bearer Tokens
- Client-side form validation
- Prevention of unauthorized route access
- Secure logout by clearing authentication state

----

## 11. Access Control Matrix

| Resource | Guest | Student | Instructor | Admin |
|---|---|---|---|---|
| Home Page | ✓ | ✓ | ✓ | ✓ |
| Login | ✓ | ✓ | ✓ | ✓ |
| Practice Session | ✗ | ✓ | ✓ | ✓ |
| AI Recognition | ✗ | ✓ | ✓ | ✓ |
| Progress Reports | ✗ | Own Only | Assigned Students | All |
| User Management | ✗ | ✗ | ✗ | ✓ |
| Mudra Database Management | ✗ | ✗ | ✗ | ✓ |
| System Settings | ✗ | ✗ | ✗ | ✓ |

---

## 12. Threat Analysis

| Threat | Risk | Mitigation |
|---|---|---|
| **Unauthorized Access** | Unauthorized users accessing the system. | Secure authentication and role-based access control. |
| **SQL Injection** | Database manipulation through malicious queries. | Parameterized SQL queries and input validation. |
| **Data Breach** | Exposure of user information. | Password hashing, HTTPS, restricted database access. |
| **Camera Privacy** | Misuse of captured images. | Real-time processing without permanent image storage. |
| **Session Hijacking** | Unauthorized use of active sessions. | Secure session tokens, session expiration, HTTPS. |

---

## 13. Backup and Recovery

- Daily database backups.
- Weekly full system backup.
- Recovery procedures tested periodically.
- Backup files stored securely with restricted access.

---

## 14. Audit and Monitoring

The system records the following activities:

- User Registration
- User Login
- Failed Login Attempts
- Logout Events
- Mudra Recognition Requests
- Administrative Actions
- API Errors
- System Errors

Application logs are periodically reviewed to identify suspicious activity and improve system security.

---

## 15. Compliance

The system follows standard software security best practices, including:

- Principle of Least Privilege (PoLP)
- Role-Based Access Control (RBAC)
- JWT Authentication
- Secure Password Hashing using bcrypt
- HTTPS/TLS Communication
- Data Privacy Protection
- Input Validation and Sanitization
- SQL Injection Prevention
- Cross-Origin Resource Sharing (CORS) Configuration
- Regular Backup Strategy

---

## 16. Conclusion

The ABHINAYA DARPANAM Security and Access framework provides a secure environment for users by combining strong authentication, role-based authorization, encrypted communication, secure database practices, and privacy-preserving AI processing. These measures ensure that the system remains reliable, scalable, and suitable for educational deployment while protecting user data and maintaining the integrity of the mudra recognition platform.
