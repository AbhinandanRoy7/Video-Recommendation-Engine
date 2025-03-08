# Assignment
---

# **Video Recommendation Engine 🎬📺**  

## **📌 Project Description**  
The **Video Recommendation Engine** is built using **Deep Neural Networks (DNNs)** and **FastAPI** to provide personalized video recommendations. It integrates **external APIs** for data collection and uses **mood-based recommendations** to tackle the **cold start problem**.  

---

## **⚙️ Tech Stack**  
- **Python** 🐍  
- **FastAPI** 🚀 (for backend API)  
- **Deep Neural Networks (DNNs)** 🤖 (for recommendation model)  
- **PostgreSQL/MySQL** (for database)  
- **Postman** (for API testing)  

---

## **🚀 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/AbhinandanRoy7/Video-Recommendation-Engine.git
cd Video-Recommendation-Engine
```

### **2️⃣ Set Up Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv  
source venv/bin/activate  # For Mac/Linux  
venv\Scripts\activate  # For Windows  
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**  
Create a `.env` file and add the required configurations:  
```
API_KEY=your_api_key_here  
DB_URL=your_database_url_here  
SECRET_KEY=your_secret_key_here  
```

### **5️⃣ Run Database Migrations**  
```bash
alembic upgrade head  # If using Alembic for migrations
```

### **6️⃣ Start the FastAPI Server**  
```bash
uvicorn main:app --reload
```
The API will be available at **`http://127.0.0.1:8000`**.

---

## **📡 API Endpoints**  

### **1️⃣ Get Recommended Videos**  
```http
GET /recommend?user_id=123&mood=happy
```
**Response:**  
```json
{
  "user_id": "123",
  "recommended_videos": [
    {"title": "Video A", "url": "https://example.com/a"},
    {"title": "Video B", "url": "https://example.com/b"}
  ]
}
```

### **2️⃣ Add User Preferences**  
```http
POST /preferences
```
**Request Body:**  
```json
{
  "user_id": "123",
  "liked_genres": ["Action", "Comedy"]
}
```

---

## **📂 Database Migration Scripts**  
All migration scripts are stored in the `/migrations` folder. To apply migrations, run:  
```bash
alembic upgrade head
```

---

## **📨 Postman Collection**  
The Postman collection is available in the repository as **`video_recommendation.postman_collection.json`**. Import it into Postman to test the APIs.  

---

## **👨‍💻 Contributing**  
Feel free to contribute! Fork the repo, create a new branch, and submit a **Pull Request (PR)**.  

---

## **📜 License**  
This project is licensed under the **MIT License**.  

---

This README provides a **clear and structured overview** of your project. You can modify it based on your specific implementation. Let me know if you need any tweaks! 🚀
