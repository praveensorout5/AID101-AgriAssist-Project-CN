# 🌾 AgriAssist AI

AgriAssist AI is a farmer-focused advisory platform that combines **machine learning**, **deep learning**, and **data-driven insights** to support agricultural decision-making.  
It provides personalized advisories, crop health analysis, irrigation scheduling, yield prediction, and market insights — all accessible through a clean web dashboard.

---

## 🚀 Key Features

- **Farmer Portal**
  - Register farm profiles with crop type, acreage, soil type, and region.
  - Manage farm data with full CRUD operations.

- **Advisory Engine**
  - Generates personalized advisories based on farm profile and conditions.
  - Logs advisories in the database for dashboard display.

- **Crop Health Analysis**
  - Upload crop images via dashboard.
  - CNN model (`crop_health_cnn.h5`) detects diseases and returns health status + confidence.

- **Yield & Irrigation Models**
  - `yield_model.pkl` predicts expected yield based on farm parameters.
  - `irrigation_model.pkl` recommends irrigation scheduling using weather and soil data.

- **Market Insights**
  - Analyzes `market_prices.csv` dataset.
  - Provides average price trends and actionable recommendations.

- **Farmer Dashboard**
  - Web interface (`dashboard.html`) for advisories, crop health uploads, and market insights.
  - Styled with `style.css` and powered by `advisory.js` + `upload_health.js`.

---

## 🏗️ Project Structure

```
AgriAssist/
│
├── backend/
│   ├── app.py                # Flask app factory
│   ├── db.py                 # SQLAlchemy setup
│   ├── routes.py             # API endpoints
│   ├── models/               # ORM models (FarmProfile, AdvisoryLog)
│   ├── services/             # ML/DL services (advisory_engine, crop_health_infer, market_insight)
│   └── utils/                # Validators, file paths, helpers
│
├── frontend/
│   ├── index.html            # Landing page
│   ├── dashboard.html        # Farmer dashboard
│   ├── style.css             # Civora Nexus theme
│   └── scripts/              # advisory.js, upload_health.js
│
├── database/
│   ├── schema.sql            # SQL schema
│   └── migrate.py            # Migration script
│
├── models_store/
│   ├── irrigation_model.pkl  # Irrigation ML model
│   ├── yield_model.pkl       # Yield prediction model
│   └── crop_health_cnn.h5    # CNN for crop disease detection
│
└── datasets/
    └── market_prices.csv     # Market data for insights
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/agriassist.git
cd agriassist
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database
```bash
python backend/database/migrate.py
```

### 5. Run Backend Server
```bash
flask run
```
Backend runs at: `http://127.0.0.1:5000`

### 6. Open Frontend
Open `frontend/index.html` or `frontend/dashboard.html` in your browser.

---

## 🔗 API Endpoints

| Endpoint                        | Method | Description                          |
|---------------------------------|--------|--------------------------------------|
| `/farm-profiles`                | GET    | List all farm profiles               |
| `/farm-profiles/<id>`           | GET    | Get farm profile by ID               |
| `/farm-profiles`                | POST   | Add new farm profile                 |
| `/farm-profiles/<id>`           | PUT    | Update farm profile                  |
| `/farm-profiles/<id>`           | DELETE | Delete farm profile                  |
| `/advisory/<farm_id>`           | GET    | Fetch advisories for a farm          |
| `/advisory/<farm_id>`           | POST   | Add advisory log                     |
| `/crop-health/upload`           | POST   | Upload crop image + metadata         |
| `/crop-health/infer`            | POST   | Run CNN inference on crop image      |

---

## 🧠 Models

- **Yield Model (`yield_model.pkl`)**  
  Linear regression model predicting yield based on acreage, rainfall, and soil nutrients.

- **Irrigation Model (`irrigation_model.pkl`)**  
  Decision tree model recommending irrigation schedules.

- **Crop Health CNN (`crop_health_cnn.h5`)**  
  Deep learning model classifying crop images into healthy/diseased categories.

---

## 🎨 Frontend

- **Landing Page (`index.html`)**  
  Farmer registration form + advisory preview.

- **Dashboard (`dashboard.html`)**  
  Displays advisories, crop health upload form, and market insights.

- **Scripts**
  - `advisory.js`: Fetches advisories and handles registration.
  - `upload_health.js`: Handles crop image uploads and inference results.

- **Styling (`style.css`)**  
  Clean, modern Civora Nexus theme with green accents.

---

## 🛠️ Utilities

- **validators.py** → Validates farm profiles, advisories, and crop health uploads.
- **file_paths.py** → Centralized file path management for datasets, uploads, and models.
- **migrate.py** → Applies schema migrations programmatically.

---

## 📊 Example Workflow

1. Farmer registers via **index.html** → `/farm-profiles`.
2. Advisory engine generates recommendations → `/advisory/<farm_id>`.
3. Farmer uploads crop image via **dashboard.html** → `/crop-health/upload`.
4. CNN model runs inference → `/crop-health/infer`.
5. Market insights displayed from `market_prices.csv`.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.  
See the LICENSE file for details.

---

## 👨‍💻 Author

Developed by **Praveen Kumar**  
Focused on delivering robust, scalable ML/data science solutions with professional backend architecture.


## Quickstart.md for farmers and non technical users.

# 🌾 AgriAssist AI - Quickstart Guide

This guide helps you set up and run AgriAssist AI quickly.  
Follow these steps to get the farmer portal and dashboard running on your system.

---

## ⚙️ Prerequisites

- Python 3.9+
- Git
- Virtual environment tool (`venv` or `conda`)
- Browser (Chrome/Edge/Firefox)

---

## 🚀 Setup Steps

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/agriassist.git
cd agriassist
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database
```bash
python backend/database/migrate.py
```

### 5. Run Backend Server
```bash
flask run
```
Backend runs at: `http://127.0.0.1:5000`

### 6. Open Frontend
- Open `frontend/index.html` → Register your farm profile.
- Open `frontend/dashboard.html` → View advisories, upload crop images, and check market insights.

---

## 🔗 Key API Endpoints

- **Farm Profiles**
  - `POST /farm-profiles` → Register a farm
  - `GET /farm-profiles/<id>` → View farm profile

- **Advisories**
  - `GET /advisory/<farm_id>` → Fetch advisories
  - `POST /advisory/<farm_id>` → Add advisory

- **Crop Health**
  - `POST /crop-health/upload` → Upload crop image
  - `POST /crop-health/infer` → Run CNN inference

---

## 🧠 Models Used

- `yield_model.pkl` → Predicts crop yield
- `irrigation_model.pkl` → Recommends irrigation schedules
- `crop_health_cnn.h5` → Detects crop diseases from images

---

## 📊 Typical Workflow

1. Register your farm profile on the **landing page**.
2. Receive personalized **advisories** in the dashboard.
3. Upload crop images for **health analysis**.
4. View **market insights** and yield predictions.

---

## ✅ That’s It!

You’re ready to use AgriAssist AI.  
Farmers can now access advisories, crop health analysis, and market insights directly from the dashboard.
