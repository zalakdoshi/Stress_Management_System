# 🧘 AI-Based Stress Detection & Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat-square&logo=react)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=flat-square&logo=mongodb)
![Gemini AI](https://img.shields.io/badge/Gemini-AI%20Powered-4285F4?style=flat-square&logo=google)

**A comprehensive AI-powered web application for detecting, analyzing, and managing stress levels using Machine Learning and Generative AI.**

🔗 **Live Demo:** [https://stressss-management-system.vercel.app](https://stressss-management-system.vercel.app)

[Features](#features) • [Installation](#installation) • [Tech Stack](#tech-stack) • [API Reference](#api-endpoints)

</div>

---

## 🌟 Overview

This Stress Detection & Management System uses **Machine Learning** to predict stress levels based on lifestyle factors like sleep, work hours, exercise, and more. It provides personalized recommendations, AI-powered chat support, mood journaling, and comprehensive reports to help users understand and manage their stress effectively.

<a id="features"></a>
## ✨ Features

### Core Features
- 🔐 **User Authentication** - Secure login/registration with password hashing
- 🧠 **ML Stress Prediction** - Predicts Low/Medium/High stress using Random Forest
- 📊 **Trigger Analysis** - Identifies key stress factors from your lifestyle
- 📈 **Stress Forecasting** - Predicts future stress trends based on history

### AI-Powered Features
- 🤖 **Gemini AI Chatbot** - Dynamic, intelligent stress support conversations
- 💡 **Smart Recommendations** - Dynamic, editable recommendations per stress level
- 🚨 **Emergency Relief** - S.T.O.P. technique for immediate stress relief

### Tracking & Reports
- 📝 **Mood Journaling** - Track daily moods and feelings
- 📅 **Weekly/Monthly Reports** - Visualize stress patterns over time
- 📉 **Before/After Analysis** - Track your improvement journey

<a id="tech-stack"></a>
## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React.js 18, Axios, Modern CSS |
| **Backend** | Flask 3.0, Python 3.9+ |
| **Database** | MongoDB Atlas (Cloud) / SQLite (Local) |
| **ML Model** | scikit-learn (Random Forest, SVM, LR) |
| **AI Chatbot** | Google Gemini 2.5 Flash |
| **Authentication** | Werkzeug Security (Password Hashing) |

<a id="installation"></a>
## 🚀 Installation

### Prerequisites
- Python 3.9+
- Node.js 16+
- MongoDB Atlas account (free) or local MongoDB
- Google Gemini API key (free)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/stress-detection-system.git
cd stress-detection-system
```

### 2. Backend Setup

```bash
# Navigate to backend
cd backend/src

# Install Python dependencies
pip install -r requirements.txt

# Create virtual environment (recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Train the ML model (run once)
python stress_model.py

# Create .env file with your credentials (see section below)
cp ../../.env.example .env

# Run the server
python app_mongodb.py
```

### 2a. Environment Setup (IMPORTANT - Security)

Create a `.env` file in the `backend/src` directory with your credentials:

```bash
# MongoDB Connection
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/

# Gemini AI API Key
GEMINI_API_KEY=<your-gemini-api-key>

# Flask Configuration
FLASK_ENV=production
FLASK_SECRET_KEY=<your-random-secret-key>
```

**Never commit `.env` file to git!** It's already listed in `.gitignore`.

### 3. Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

### 4. Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5000

## 🗄️ Database Setup

### MongoDB Atlas (Recommended)

1. Create a free account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a new cluster (free M0 tier available)
3. Create a database user with a strong password
4. Whitelist your IP address (or use 0.0.0.0/0 for development only)
5. Copy your connection string
6. Add it to your `.env` file:

```bash
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/stress_detection_db?retryWrites=true&w=majority
```

### Gemini AI Setup (For AI-Powered Chatbot)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a free API key (requires Google account)
3. Add it to your `.env` file:

```bash
GEMINI_API_KEY=<your-api-key-here>
```

Without this key, the chatbot will use fallback rule-based responses.

## 🚀 Deployment

### Deploy Frontend to Vercel

1. Push your code to GitHub
2. Go to [Vercel](https://vercel.com) and sign in with GitHub
3. Click "New Project" and import your repository
4. Set environment variables:
   - `REACT_APP_API_URL=https://your-backend-url.com`
5. Deploy

### Deploy Backend to Render/Railway/Heroku

1. Create account on [Render](https://render.com) or similar platform
2. Create new Web Service from GitHub repository
3. Set environment variables in deployment dashboard:
   ```
   MONGODB_URI=<your-atlas-connection-string>
   GEMINI_API_KEY=<your-gemini-key>
   FLASK_ENV=production
   FLASK_SECRET_KEY=<your-secret-key>
   ```
4. Set build command: `pip install -r backend/src/requirements.txt`
5. Set start command: `cd backend/src && python app_mongodb.py`

**Live Demo:** Currently deployed at [https://stressss-management-system.vercel.app](https://stressss-management-system.vercel.app)

## 🔐 Security & Best Practices

### Credentials Management

**DO NOT** commit sensitive information to git:
- Never commit `.env` files with real credentials
- Use `.env.example` to document required variables
- Use environment variables in production
- Rotate API keys periodically

### MongoDB Security
- Use strong, unique passwords
- Enable IP whitelist in MongoDB Atlas (restrict to known IPs in production)
- Use read-only credentials for non-admin operations
- Enable MongoDB encryption at rest

### API Security
- All passwords hashed with Werkzeug security
- CORS configured to allow only frontend origin
- Implement rate limiting for API endpoints (recommended)
- Use HTTPS only in production

## 📁 Project Structure

```
stress_management_sys/
├── backend/
│   └── src/
│       ├── app_mongodb.py       # Flask API (MongoDB + Gemini AI)
│       ├── app.py               # Flask API (SQLite version)
│       ├── stress_model.py      # ML model training script
│       ├── stress_model.pkl     # Trained ML model
│       ├── stress_detection_data.csv
│       └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.js              # Main React app
│   │   ├── App.css             # Global styles
│   │   ├── components/
│   │   │   └── Navbar.js
│   │   └── pages/
│   │       ├── Login.js
│   │       ├── Register.js
│   │       ├── Dashboard.js    # Main dashboard
│   │       ├── StressForm.js   # Stress assessment form
│   │       ├── Recommendations.js  # Dynamic recommendations
│   │       ├── Journal.js      # Mood journaling
│   │       ├── Reports.js      # Weekly/Monthly reports
│   │       └── Chatbot.js      # AI-powered chatbot
│   └── package.json
└── README.md
```

<a id="api-endpoints"></a>
## 🔗 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register` | Register new user |
| POST | `/api/login` | Login user |

### Stress Analysis
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/predict` | Predict stress level (ML) |
| POST | `/api/analyze-triggers` | Analyze stress triggers |
| POST | `/api/forecast` | Forecast stress trends |
| GET | `/api/history/:userId` | Get stress history |

### Recommendations
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/recommendations/:level` | Get recommendations by level |
| POST | `/api/recommendations` | Add new recommendation |
| PUT | `/api/recommendations/:id` | Update recommendation |
| DELETE | `/api/recommendations/:id` | Delete recommendation |
| GET | `/api/emergency-tips` | Emergency relief tips |

### Journaling & Reports
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/journal` | Add journal entry |
| GET | `/api/journal/:userId` | Get journal entries |
| GET | `/api/reports/weekly/:userId` | Weekly stress report |
| GET | `/api/reports/monthly/:userId` | Monthly stress report |
| GET | `/api/reports/before-after/:userId` | Progress comparison |

### AI Chatbot
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chat` | AI-powered chat (Gemini) |

## 🧠 Machine Learning Model

The stress detection model is trained using machine learning algorithms to predict stress levels (Low/Medium/High) based on lifestyle and health factors.

### Model Specifications

| Aspect | Details |
|--------|---------|
| **Dataset Size** | 774 samples |
| **Feature Count** | 22 features |
| **Algorithms Tested** | Random Forest, Support Vector Machine (SVM), Logistic Regression |
| **Best Performing Model** | Random Forest Classifier |
| **Accuracy Score** | 72.9% |
| **Training/Test Split** | 80/20 |
| **Model File** | `backend/src/stress_model.pkl` (trained model serialized with joblib) |

### Features Used for Prediction

The model uses 22 input features across 5 categories:

**Lifestyle Factors (9 features):**
- Age, Gender, Occupation, Marital Status, Smoking Habit

**Sleep Metrics (3 features):**
- Sleep Duration, Sleep Quality, Wake/Bed Times

**Activity & Nutrition (7 features):**
- Physical Activity, Screen Time, Caffeine Intake, Alcohol Intake
- Exercise Type, Work Hours, Travel Time

**Health Metrics (3 features):**
- Blood Pressure, Cholesterol Level, Blood Sugar Level

**Behavioral (2 features):**
- Social Interactions, Meditation Practice

### Model Training

The model is trained on a comprehensive stress detection dataset using scikit-learn:

```python
# See backend/src/stress_model.py for full training pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

# Training steps:
# 1. Load and preprocess data
# 2. Encode categorical variables (OneHotEncoder)
# 3. Scale numerical features (StandardScaler)
# 4. Split into training/testing sets (80/20)
# 5. Train Random Forest with optimized hyperparameters
# 6. Evaluate on test set (72.9% accuracy achieved)
# 7. Save model using joblib
```

### Predictions Provided

For each user input, the model provides:

- **Primary Prediction**: Stress Level (Low, Medium, or High)
- **Confidence Scores**: Probability distribution across all three stress levels
- **Trigger Analysis**: Identifies the top factors contributing to stress

### Model Accuracy & Limitations

**Accuracy: 72.9%** on the test dataset

**Limitations to consider:**
- Model is trained on aggregated data and may not capture all individual variations
- Predictions should be viewed as a guide, not a clinical diagnosis
- For mental health concerns, consult qualified professionals
- Regular model retraining recommended as new data is collected

## 📸 Screenshots

### Authentication
| Login Page |
|:----------:|
| ![Login](frontend/src/Screenshots/Login.png) |

### Dashboard
| Dashboard Overview | Dashboard Statistics |
|:------------------:|:--------------------:|
| ![Dashboard 1](frontend/src/Screenshots/Dashboard_1.png) | ![Dashboard 2](frontend/src/Screenshots/Dashboard_2.png) |

### Stress Assessment
| Stress Check Form |
|:-----------------:|
| ![Stress Check](frontend/src/Screenshots/StressCheck.png) |

### Recommendations
| Recommendations Overview | Recommendations Details |
|:------------------------:|:-----------------------:|
| ![Recommendations 1](frontend/src/Screenshots/Recommendations_1.png) | ![Recommendations 2](frontend/src/Screenshots/Recommendations_2.png) |

### AI Chatbot & Journaling
| AI Support Chatbot | Mood Journal |
|:------------------:|:------------:|
| ![AI Support](frontend/src/Screenshots/AiSupport.png) | ![Mood Journal](frontend/src/Screenshots/MoodJournal.png) |

### Reports & Database
| Stress Reports | MongoDB Database |
|:--------------:|:----------------:|
| ![Reports](frontend/src/Screenshots/Reports.png) | ![MongoDB](frontend/src/Screenshots/MongoDB.png) |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👥 Team

| Name | Role |
|:-----|:-----|
| **Zalak Doshi** | Team Leader |
| **Shreya Patel** | Team Member |
| **Sohani Pangotra** | Team Member |


## 📝 License

This project is developed for educational purposes (B.Tech Final/Mini Project).

---

<div align="center">

⭐ **Star this repo if you find it helpful!** ⭐

Made with ❤️ for stress-free living

</div>
