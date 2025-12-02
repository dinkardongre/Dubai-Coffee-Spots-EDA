# ☕ Dubai Cold Coffee Finder

A professional Exploratory Data Analysis (EDA) and geospatial filtering project built with **Pandas**, **Streamlit**, and **Geopy**.  
The application helps users find nearby cold coffee spots in Dubai based on their location and several filter options.

---

## 🔍 Features

- Enter your latitude & longitude to find nearby spots  
- Filter by:
  - Distance (km)
  - Minimum rating
  - Spot type (cart, cafe, truck)
  - Open/Closed status (real-time check)
- Sort by distance, rating, or name
- Displays the top N results
- Generates derived features like:
  - **Distance** between user and coffee spot  
  - **Current open/closed status**

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Streamlit**
- **Geopy**

---

## ▶️ How to Run the Project

### 1. Install Required Packages
```bash
pip install streamlit pandas geopy
```
2. Run the Streamlit App
bash
Copy code
```
streamlit run app.py
```
The app will open in your browser automatically.

📄 Dataset
The project uses a CSV file containing Dubai cold coffee spot details, including:

Coordinates (latitude, longitude)

Opening & closing times

Ratings

Spot type (cart/cafe/truck)

🎯 Purpose
This project demonstrates how EDA, feature engineering, and geospatial calculations can be combined to build a functional, interactive data application.
