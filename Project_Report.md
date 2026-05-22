


Stress Management System

A report submitted
In partial fulfilment of the requirements for the Degree of Bachelor of Technology

In Information Technology
Semester – IV



By

Doshi Zalak (12402080503008)



Faculty Guide: Mittal Darji, Assistant Professor

Academic Year 2024-25 (Even)


Department of Information Technology
G H Patel College of Engineering & Technology
Bakrol Road, Vallabh Vidyanagar



---



CERTIFICATE

This is to certify that Seminar work embodied in this report entitled, "Stress Management System" was carried out by Doshi Zalak (12402080503008) at G H Patel College of Engineering & Technology for partial fulfilment of B.Tech. degree to be awarded by the Charutar Vidya Mandal (CVM) University. This seminar work has been carried out under my supervision and is to the satisfaction of department.


Date:
Place:


Guide                                  Head of Department
Mittal Darji                            Dr. Nikhil Gondaliya
Assistant Professor                     Professor & Head



---



Acknowledgement

I would like to express my sincere gratitude to my seminar guide, Ms. Mittal Darji, Assistant Professor, for her valuable guidance, support, and encouragement throughout the course of this seminar. Her insights and suggestions helped me enhance the quality of my work significantly.

I also extend my heartfelt thanks to Dr. Nikhil Gondaliya, Professor & Head of the Department of Information Technology, for providing the opportunity and necessary resources for conducting this seminar.

Lastly, I thank my friends and family for their constant support and motivation throughout the process.


Doshi Zalak (12402080503008)



---



Table of Contents

1. Abstract
2. Introduction
3. Problem Statement
4. Objectives
5. Literature Review / Background
6. System Architecture
7. Tech Stack
8. Methodology
   8.1 Data Collection & Preprocessing
   8.2 Machine Learning Model Development
   8.3 Backend Development (Flask REST API)
   8.4 Frontend Development (React.js)
   8.5 Database Design (MongoDB Atlas)
   8.6 AI Chatbot Integration (Google Gemini)
9. System Implementation
   9.1 User Authentication
   9.2 Stress Prediction Module
   9.3 Stress Trigger Analysis
   9.4 Stress Forecasting
   9.5 Personalized Recommendations
   9.6 Mood Journaling
   9.7 Reports (Weekly, Monthly, Before/After)
   9.8 AI Chatbot
   9.9 Emergency Stress Relief (S.T.O.P. Technique)
10. Results & Discussion
11. Conclusion
12. Future Scope
13. References


List of Figures

Figure 1.    System Architecture Diagram
Figure 2.    Data Flow Diagram (Level 0)
Figure 3.    Data Flow Diagram (Level 1)
Figure 4.    Sequence Diagram – Stress Prediction Flow
Figure 5.    ML Model Training Pipeline
Figure 6.    User Interface – Login Page
Figure 7.    User Interface – Stress Form
Figure 8.    User Interface – Dashboard
Figure 9.    User Interface – Recommendations Page
Figure 10.   User Interface – AI Chatbot
Figure 11.   User Interface – Mood Journal
Figure 12.   User Interface – Reports Page


List of Tables

Table 1.    Tech Stack
Table 2.    Dataset Features
Table 3.    ML Models Comparison
Table 4.    API Endpoints
Table 5.    MongoDB Collections
Table 6.    DFD Symbols
Table 7.    Sequence Diagram Symbols



---



1. Abstract

Stress is a growing concern in today's fast-paced world, affecting millions of individuals physically, mentally, and emotionally. Despite its prevalence, there is a lack of accessible, personalized tools that enable individuals to monitor, analyze, and manage their stress levels effectively. This project report presents the development of an AI-Based Stress Detection & Management System — a full-stack web application that leverages Machine Learning and Generative AI to detect, predict, and manage stress levels.

The system collects lifestyle data such as sleep duration, work hours, exercise habits, caffeine intake, social interactions, and more through a user-friendly web interface built with React.js. A trained Random Forest classifier (72.9% accuracy) processes this data on the Flask backend to predict stress levels as Low, Medium, or High. The application further provides personalized recommendations, an AI-powered chatbot using Google Gemini 2.5 Flash, mood journaling, and comprehensive weekly/monthly stress reports — all stored in a MongoDB Atlas cloud database.

By bridging Machine Learning with practical mental health support, this system provides students and working professionals with an intelligent, data-driven tool for proactive stress management and early intervention.



---



2. Introduction

Mental health and well-being have become crucial issues of the 21st century. With increasing work pressure, academic expectations, social media influence, and lifestyle changes, stress levels among individuals — particularly students and working professionals — have risen sharply. According to the American Institute of Stress, 77% of people experience stress that affects their physical health, while 73% report that stress impacts their mental health.

Despite the widespread impact of stress, most individuals lack access to personalized tools that can help them understand their stress patterns, identify triggers, and take proactive measures. Existing solutions are either too generic (providing one-size-fits-all advice) or too expensive (professional therapy sessions). There is a significant gap in the market for an accessible, intelligent, and user-friendly tool that combines data-driven prediction with actionable stress management guidance.

This project addresses this gap by developing an AI-Based Stress Detection & Management System. The system uses a Machine Learning model (Random Forest classifier) to predict stress levels based on 21 lifestyle parameters and integrates Google Gemini AI for intelligent conversational support. The application is built as a full-stack web platform using React.js (frontend), Flask (backend), and MongoDB Atlas (database), making it accessible from any web browser.

The system enables users to:
- Take a comprehensive stress assessment (21-parameter form)
- Get instant AI-powered stress level prediction (Low / Medium / High)
- Identify their personal stress triggers
- Receive personalized recommendations based on their stress level
- Track their mood over time through journaling
- View weekly/monthly/before-after progress reports
- Chat with an AI-powered stress support assistant
- Access emergency stress relief techniques (S.T.O.P. method)



---



3. Problem Statement

Stress is a growing epidemic that affects millions of people worldwide, leading to mental health disorders, decreased productivity, relationship problems, and chronic physical health conditions. The World Health Organization (WHO) has identified stress as the "health epidemic of the 21st century."

Key challenges that this project aims to address include:

1. Lack of Self-Awareness: Most individuals are unaware of how their daily habits (sleep, screen time, caffeine, exercise) contribute to their stress levels. They don't recognize stress triggers until symptoms become severe.

2. Generic Solutions: Existing stress management advice is typically generic and does not adapt to individual lifestyles, habits, or patterns. What works for one person may not work for another.

3. Accessibility: Professional mental health consultations are expensive and time-consuming, creating barriers for students and young professionals who are most vulnerable to stress.

4. No Continuous Monitoring: There is no simple, digital tool that allows individuals to continuously monitor their stress over time, identify patterns, and track whether their management strategies are working.

5. Late Intervention: Without predictive tools, individuals often seek help only when stress has already escalated to anxiety, depression, or burnout — missing the opportunity for early intervention.

This project proposes an AI-based solution that predicts stress levels using Machine Learning, provides personalized recommendations, enables continuous monitoring through journaling and reports, and offers immediate support through an AI chatbot — all within a single, accessible web application.



---



4. Objectives

The primary objectives of this project are:

1. To develop an AI-powered stress prediction system using Machine Learning (Random Forest classifier) to classify stress levels into three categories: Low, Medium, and High based on 21 lifestyle parameters.

2. To create a user-friendly web interface using React.js that allows users to input their lifestyle data and receive instant stress level predictions with confidence probabilities.

3. To provide personalized stress management recommendations tailored to the user's predicted stress level (different tips for Low, Medium, and High stress).

4. To implement a stress trigger analysis feature that identifies which lifestyle factors (poor sleep, high screen time, lack of exercise, etc.) are contributing most to the user's stress.

5. To enable continuous stress monitoring through mood journaling, allowing users to record daily moods and notes, building a personal mental health timeline.

6. To generate comprehensive stress reports — weekly, monthly, and before/after comparison — to help users track their progress over time.

7. To integrate an AI-powered chatbot using Google Gemini 2.5 Flash that provides empathetic, evidence-based conversational support for stress relief.

8. To implement emergency stress relief features such as the S.T.O.P. technique (Stop, Breathe, Observe, Proceed, Ground) for immediate stress intervention.

9. To use a cloud-based NoSQL database (MongoDB Atlas) for secure, scalable data storage with indexed collections for users, stress history, and mood journals.



---



5. Literature Review / Background

5.1 Stress and Its Impact

Stress is a physiological and psychological response to perceived threats or challenges. While short-term (acute) stress can improve focus and performance, chronic stress leads to serious health consequences including cardiovascular disease, weakened immune system, anxiety, depression, and cognitive impairment. The American Psychological Association (APA) reports that chronic stress is linked to the six leading causes of death globally.

5.2 Machine Learning in Mental Health

Machine Learning has been increasingly applied in the mental health domain for prediction, classification, and intervention. Studies have demonstrated the effectiveness of ML algorithms such as Random Forest, SVM, and Neural Networks for predicting mental health conditions based on lifestyle and behavioral data. Random Forest, in particular, has been shown to perform well on health-related classification tasks due to its ability to handle mixed feature types and its robustness to overfitting.

5.3 Chatbot-Based Mental Health Support

AI chatbots have emerged as a promising tool for mental health support. Applications such as Woebot and Wysa use conversational AI to provide cognitive behavioral therapy (CBT) techniques, mindfulness exercises, and emotional support. The integration of Large Language Models (LLMs) like Google Gemini has further enhanced the quality and contextual understanding of chatbot responses.

5.4 Web-Based Health Applications

The proliferation of web technologies (React.js, Flask, Node.js) has made it feasible to build sophisticated health applications accessible through browsers. The combination of responsive frontend frameworks, RESTful APIs, and cloud databases enables real-time health monitoring without requiring native app installations.

5.5 Existing Gap

While individual solutions exist for stress assessment, mood tracking, or chatbot support, there is a lack of a unified platform that combines ML-based prediction, personalized recommendations, continuous monitoring, and AI conversational support in a single application. This project fills that gap.



---



6. System Architecture

The system follows a three-tier client-server architecture:

6.1 Frontend Layer (React.js – Port 3000)

The frontend is a Single Page Application (SPA) built with React.js. It consists of 10 components:
- App.js – Main application router and layout
- Navbar.js – Navigation bar component
- Login.js – User login page with form validation
- Register.js – New user registration page
- Dashboard.js – Main dashboard showing latest stress level and history
- StressForm.js – Comprehensive 21-input stress assessment form
- Recommendations.js – Personalized tips based on stress level
- Journal.js – Mood journaling (add and view entries)
- Reports.js – Weekly, monthly, and before/after comparison reports
- Chatbot.js – AI-powered stress support chatbot

The frontend communicates with the backend via REST API calls using Axios.

6.2 Backend Layer (Flask – Port 5000)

The backend is built using Flask (Python) and provides 15+ REST API endpoints organized into modules:
- Authentication (Register, Login)
- Stress Prediction (Predict, Triggers, Forecast)
- Recommendations (Level-based tips, Emergency tips)
- Mood Journal (Add, Get entries)
- Reports (Weekly, Monthly, Before/After)
- Chatbot (Gemini AI-powered)
- Health Check

The backend loads a pre-trained ML model (stress_model.pkl) using joblib and processes user input through preprocessing pipelines (OneHotEncoding, StandardScaler).

6.3 Database Layer (MongoDB Atlas)

MongoDB Atlas is used as the cloud-hosted NoSQL database. It has 3 collections:
- users: Stores user accounts with hashed passwords (Werkzeug security)
- stress_history: Stores every stress prediction with input data, stress level, and timestamp
- mood_journal: Stores mood entries with user_id, mood, notes, and date

Indexes are created on email (unique) and user_id fields for efficient querying.

6.4 External Service (Google Gemini AI)

Google Gemini 2.5 Flash is used for the AI chatbot. The model is configured with a comprehensive system prompt that instructs it to act as a compassionate stress management assistant. Fallback keyword-based responses are provided when AI is unavailable.


Data Flow:
User fills stress assessment form → React sends data via Axios POST to /api/predict → Flask preprocesses input (time_to_minutes conversion, OneHotEncoding, StandardScaler) → Random Forest model predicts stress level → Result is saved to MongoDB stress_history collection → Response sent back to React → Displayed on Dashboard with probabilities



---



7. Tech Stack

Layer                  Technology                         Purpose
-----                  ----------                         -------
Frontend               React.js 18                        User interface & SPA
                       React Router DOM                   Client-side routing
                       Axios                              HTTP API calls
                       CSS3                               Styling & animations

Backend                Flask (Python)                     REST API web framework
                       Flask-CORS                         Cross-Origin Resource Sharing
                       Werkzeug                           Password hashing & security
                       Joblib                             ML model serialization
                       Pandas, NumPy                      Data preprocessing

Database               MongoDB Atlas                      Cloud NoSQL database
                       PyMongo                            MongoDB Python driver

Machine Learning       scikit-learn                       ML model (Random Forest)
                       Pandas                             Data manipulation
                       NumPy                              Numerical computation

AI Chatbot             Google Gemini 2.5 Flash            Generative AI for chatbot
                       google-generativeai                Gemini Python SDK

Dev Tools              Node.js, npm                       Package management
                       Git & GitHub                       Version control



---



8. Methodology

8.1 Data Collection & Preprocessing

The ML model was trained on a dataset of 774 samples with 22 features. The features capture various lifestyle and health parameters:

Categorical Features: Gender, Occupation, Marital_Status, Smoking_Habit, Meditation_Practice, Exercise_Type
Numerical Features: Age, Sleep_Duration, Sleep_Quality, Physical_Activity, Screen_Time, Caffeine_Intake, Alcohol_Intake, Work_Hours, Travel_Time, Social_Interactions, Blood_Pressure, Cholesterol_Level, Blood_Sugar_Level, Wake_Up_Time, Bed_Time
Target Variable: Stress_Detection (Low / Medium / High)

Preprocessing Steps:
1. Time Conversion: Wake_Up_Time and Bed_Time (stored as strings like "7:00 AM") were converted to minutes since midnight for numerical representation.
2. OneHot Encoding: Categorical features were encoded using scikit-learn's OneHotEncoder, transforming them into binary vectors.
3. Standard Scaling: Numerical features were standardized using StandardScaler to have zero mean and unit variance.
4. Class Balancing: The dataset was resampled to balance the distribution of Low, Medium, and High stress classes.
5. Train-Test Split: 80% training, 20% testing.


8.2 Machine Learning Model Development

Three classification algorithms were evaluated:

Algorithm              Accuracy
---------              --------
Random Forest          72.9% (Selected)
Logistic Regression    ~68%
SVM                    ~65%

Random Forest was selected as the best performing model with the following configuration:
- n_estimators: 100 (100 decision trees)
- Class: RandomForestClassifier from scikit-learn
- Output: 3-class classification (Low, Medium, High)
- Probability output: predict_proba provides confidence percentages for each class

The trained model, along with preprocessing objects (OneHotEncoder, StandardScaler, label encoders), was serialized using joblib into stress_model.pkl for deployment.


8.3 Backend Development (Flask REST API)

The backend was built as a single Flask application (app_mongodb.py, 760 lines) providing REST API endpoints. Key implementation details:

- CORS Support: Flask-CORS enables cross-origin requests from the React frontend (port 3000) to Flask (port 5000)
- Password Security: Werkzeug's generate_password_hash and check_password_hash for secure password storage
- UUID-Based User IDs: Each user gets a unique UUID (uuid.uuid4()) for identification across collections
- Model Loading: The ML model is loaded once at startup using joblib.load()
- Preprocessing Pipeline: User inputs are preprocessed through the same pipeline used during training (time conversion → OneHotEncoding → StandardScaling)
- Error Handling: All endpoints include try-catch error handling with appropriate HTTP status codes

15+ API Endpoints:

Method    Endpoint                          Description
------    --------                          -----------
POST      /api/register                     Register new user
POST      /api/login                        User login
POST      /api/predict                      ML stress prediction
POST      /api/analyze-triggers             Stress trigger analysis
POST      /api/forecast                     Stress trend forecasting
GET       /api/recommendations/<level>      Level-based recommendations
GET       /api/emergency-tips               S.T.O.P. technique tips
POST      /api/journal                      Add journal entry
GET       /api/journal/<user_id>            Get journal entries
GET       /api/reports/weekly/<user_id>     Weekly report
GET       /api/reports/monthly/<user_id>    Monthly report
GET       /api/reports/before-after/<user_id>  Before/After comparison
POST      /api/chat                         AI chatbot (Gemini)
GET       /api/history/<user_id>            Stress history
GET       /api/health                       Health check


8.4 Frontend Development (React.js)

The frontend is a responsive Single Page Application with the following components:

- App.js: Main application entry point with React Router for navigation between pages (Login, Register, Dashboard, StressForm, Recommendations, Journal, Reports, Chatbot)
- Navbar.js: Navigation component with links and logout functionality
- Login.js / Register.js: Authentication forms with validation and error handling
- StressForm.js: Comprehensive form with 21 input fields covering sleep, work, exercise, diet, social interactions, and health parameters
- Dashboard.js: Displays latest stress level, prediction history, and quick access to all features
- Recommendations.js: Shows personalized stress management tips categorized by stress level (Low: 4 tips, Medium: 6 tips, High: 8 tips)
- Journal.js: Mood journaling with mood selection, notes input, and chronological entry display
- Reports.js: Visual reports with weekly and monthly stress distribution, percentages, and before/after progress comparison
- Chatbot.js: Interactive chat interface for the AI-powered stress support assistant

All components use Axios for API communication and CSS3 for styling with animations and responsive design.


8.5 Database Design (MongoDB Atlas)

MongoDB Atlas is used as the cloud-hosted NoSQL database (M0 free tier). The database name is "stress_detection_db" with three collections:

Collection: users
- user_id (String, UUID) — Primary identifier
- name (String) — User's name
- email (String, Unique Index) — Login email
- password (String, Hashed) — Werkzeug-hashed password
- created_at (DateTime) — Account creation timestamp

Collection: stress_history
- user_id (String, Indexed) — Foreign key to users
- stress_level (String) — "Low" / "Medium" / "High"
- input_data (Object) — Raw form input data
- prediction_date (DateTime) — When prediction was made

Collection: mood_journal
- user_id (String, Indexed) — Foreign key to users
- mood (String) — Selected mood
- notes (String) — User's journal notes
- entry_date (DateTime) — Entry timestamp


8.6 AI Chatbot Integration (Google Gemini)

The chatbot uses Google Gemini 2.5 Flash model with the google-generativeai Python SDK. Key implementation:

- System Prompt: A detailed prompt instructs Gemini to act as a compassionate, professional stress management assistant. It covers empathy-first responses, evidence-based techniques, conversational tone, and safety guidelines.
- Topics Covered: Breathing exercises (4-7-8, box breathing), meditation guidance, sleep hygiene, work-life balance, anxiety management, relaxation techniques, and emotional support.
- Fallback System: When Gemini is unavailable, the system uses keyword-based matching against 10 predefined response categories (stressed, anxious, tired, breathing, sleep, work, meditation, relaxation, etc.).
- Safety: The system encourages seeking professional help for crisis situations and never diagnoses conditions.



---



9. System Implementation

9.1 User Authentication

Users register with name, email, and password. Passwords are securely hashed using Werkzeug's generate_password_hash() before storage. During login, check_password_hash() verifies credentials. Each user receives a UUID-based user_id that links all their data across collections.

9.2 Stress Prediction Module

The core feature of the system. Users fill a 21-field form covering:
- Demographics: Age, Gender, Occupation, Marital Status
- Sleep: Sleep Duration, Sleep Quality, Wake Up Time, Bed Time
- Work: Work Hours, Screen Time, Travel Time
- Lifestyle: Physical Activity, Exercise Type, Caffeine Intake, Alcohol Intake, Smoking Habit
- Social: Social Interactions
- Health: Blood Pressure, Cholesterol Level, Blood Sugar Level
- Wellness: Meditation Practice

The backend preprocesses this data through the same pipeline used during training and the Random Forest model predicts the stress level. The model also provides probability percentages for each class (e.g., Low: 15%, Medium: 25%, High: 60%).

9.3 Stress Trigger Analysis

The system analyzes the user's input and identifies specific lifestyle factors contributing to their stress. For example:
- Sleep Duration < 6 hours → High impact trigger
- Work Hours > 9 hours → High impact trigger
- Screen Time > 6 hours → Medium impact trigger
- No Physical Activity → High impact trigger
- No Meditation → Medium impact trigger
- High Caffeine Intake → Medium impact trigger
- Low Social Interactions → Medium impact trigger

Each trigger includes a recommendation for improvement.

9.4 Stress Forecasting

Based on the user's historical predictions stored in MongoDB, the system calculates stress trend direction:
- Increasing: Recent stress levels are higher than earlier ones → Warning message
- Decreasing: Recent stress levels are lower → Positive encouragement
- Stable: No significant change → Maintain current routine

9.5 Personalized Recommendations

The system provides curated recommendations based on stress level:
- Low Stress (4 tips): Maintain routine, daily meditation, stay active, quality sleep
- Medium Stress (6 tips): Deep breathing, regular breaks, reduce caffeine, connect with others, nature walk, journaling
- High Stress (8 tips): STOP & breathe, progressive muscle relaxation, prioritize sleep, limit screen time, talk to someone, light exercise, avoid stimulants, calming music

9.6 Mood Journaling

Users can add daily mood journal entries with a mood selection and optional notes. Entries are stored with timestamps and displayed chronologically. The last 30 entries are fetched for viewing.

9.7 Reports (Weekly, Monthly, Before/After)

- Weekly Report: Aggregates stress predictions from the last 7 days. Shows total assessments, distribution (Low/Medium/High counts), percentages, and dominant stress level.
- Monthly Report: Same analysis for the last 30 days.
- Before/After Report: Compares the user's first-ever prediction with their most recent one to show improvement, decline, or stability.

9.8 AI Chatbot

An interactive chat interface where users can have conversations about stress, anxiety, breathing exercises, sleep tips, etc. The Google Gemini AI provides contextual, empathetic responses. If Gemini is unavailable, keyword-based fallback responses maintain basic functionality.

9.9 Emergency Stress Relief (S.T.O.P. Technique)

For users in acute stress, the system provides the S.T.O.P. technique:
1. STOP — Stop whatever you are doing
2. BREATHE — Take 5 slow, deep breaths
3. OBSERVE — Notice your thoughts without judgment
4. PROCEED — Continue with awareness
5. GROUND — Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste



---



10. Results & Discussion

10.1 Machine Learning Model Performance

The Random Forest classifier achieved 72.9% accuracy on the test set for 3-class stress level classification (Low, Medium, High). This is a reasonable result considering:
- The dataset has only 774 samples
- Stress is subjective and influenced by unmeasured factors
- 3-class classification is inherently more challenging than binary

The model provides probability outputs, giving users insight into the confidence of each prediction (e.g., "60% High, 25% Medium, 15% Low").

10.2 System Performance

- Stress Prediction Response Time: Less than 1 second (model inference + database write)
- AI Chatbot Response Time: 2-3 seconds (Google Gemini API call)
- Page Load Time: Under 2 seconds (React SPA with lazy loading)
- Database Operations: Sub-second for all CRUD operations (MongoDB Atlas with indexes)

10.3 Feature Completeness

All planned features were successfully implemented and tested:
- User registration and login with secure password hashing
- 21-parameter stress assessment with ML prediction
- Stress trigger identification and analysis
- Stress trend forecasting based on history
- Level-specific personalized recommendations
- Mood journaling with chronological history
- Weekly, monthly, and before/after comparison reports
- AI-powered chatbot with Gemini 2.5 Flash integration
- Emergency stress relief (S.T.O.P. technique)
- Health check API for monitoring system status

10.4 Deployment

The system runs as a full-stack local application:
- Frontend: React development server on port 3000
- Backend: Flask server on port 5000
- Database: MongoDB Atlas cloud cluster (accessible globally)
- AI: Google Gemini API via cloud endpoint



---



11. Conclusion

This project successfully developed an AI-Based Stress Detection & Management System as a full-stack web application. The system demonstrates the practical application of Machine Learning and Generative AI in the mental health domain by:

1. Predicting stress levels (Low/Medium/High) using a Random Forest classifier with 72.9% accuracy based on 21 lifestyle parameters.

2. Providing a comprehensive stress management platform that includes prediction, trigger analysis, forecasting, recommendations, journaling, reports, and AI chatbot support — all within a single web application.

3. Integrating modern technologies — React.js for a responsive frontend, Flask for a robust backend API, MongoDB Atlas for scalable cloud storage, and Google Gemini 2.5 Flash for intelligent conversational support.

4. Enabling continuous monitoring through mood journals and progress reports, allowing users to track their stress journey over time.

5. Offering immediate stress relief through the S.T.O.P. technique and personalized recommendations tailored to each user's stress level.

The system addresses the key gaps identified in the problem statement: it provides personalized (not generic) stress management, it is accessible (web-based, free), it enables continuous monitoring (journals and reports), and it supports early intervention (predictive ML model + AI chatbot).



---



12. Future Scope

1. Dynamic AI-Powered Recommendations: Replace static recommendations with Gemini AI-generated personalized tips based on the user's specific stress triggers and history.

2. Wearable Device Integration: Connect with smartwatches and fitness bands to automatically capture heart rate, sleep patterns, and physical activity data for more accurate predictions.

3. Deep Learning Models: Improve prediction accuracy beyond 72.9% using deep learning architectures (Neural Networks, LSTM for temporal patterns).

4. Mobile Application: Develop a native mobile app (React Native) with push notifications for daily mood check-ins and stress alerts.

5. Community Features: Add anonymous peer support groups and forums where users can share experiences and coping strategies.

6. Professional Integration: Connect users with certified mental health professionals for teleconsultation when stress levels remain consistently high.

7. Multi-Language Support: Add support for multiple languages to make the system accessible to non-English speaking users.

8. Advanced Analytics: Implement correlation analysis between specific lifestyle factors and stress levels, providing users with deeper insights into their patterns.



---



13. References

1. scikit-learn Documentation — https://scikit-learn.org/
2. Flask Documentation — https://flask.palletsprojects.com/
3. React.js Documentation — https://react.dev/
4. MongoDB Atlas Documentation — https://www.mongodb.com/docs/atlas/
5. Google Gemini AI Documentation — https://ai.google.dev/docs
6. American Institute of Stress — https://www.stress.org/
7. World Health Organization – Mental Health — https://www.who.int/health-topics/mental-health
8. Werkzeug Security Documentation — https://werkzeug.palletsprojects.com/
9. Pandas Documentation — https://pandas.pydata.org/docs/
10. NumPy Documentation — https://numpy.org/doc/



---
