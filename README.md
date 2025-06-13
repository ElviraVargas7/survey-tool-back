# ⚙️ Survey Backend API - FastAPI

This is the backend for the **Survey Tool**, built with **FastAPI** and connected to a database via SQLAlchemy. It supports managing members, questions, answers, analytics, and generating survey reports in PDF.

---

## 🚀 Features

- 📋 CRUD for Members
- ❓ Dynamic question loading
- 📝 Answer submission without member tracking
- 📊 Survey average analysis
- 🧾 PDF report generation (ReportLab)
- 🔐 CORS enabled for Next.js frontend

---

## 📁 Project Structure

├── main.py # FastAPI app instance and router setup
├── routes/
│ ├── members.py # Member endpoints
│ ├── answers.py # Survey answers and report
│ └── questions.py # Survey questions
├── db/
│ ├── setup.py # Engine, session, base
│ └── schema.py # Pydantic & SQLAlchemy models
├── models/ # SQLAlchemy database models
├── services/ # Business logic and data operations
│ ├── membersServices.py
│ ├── answersServices.py
│ ├── analyticsServices.py
│ └── reportGenerator.py

---

## 🧠 Tech Stack

| Tech           | Purpose                         |
| -------------- | ------------------------------- |
| **FastAPI**    | Web framework (async REST APIs) |
| **SQLAlchemy** | ORM for DB operations           |
| **Pydantic**   | Request/response validation     |
| **ReportLab**  | PDF generation                  |
| **Uvicorn**    | ASGI server for development     |

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-org/survey-backend.git
cd survey-tool-backend
```

## 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload
```

Your FastAPI server will be running at:
👉 http://localhost:8000/docs (interactive Swagger UI)

## 🗃️ Database Initialization

Step 1: Create the database manually
Make sure your database (PostgreSQL) is created.
Tables will be created automatically when you run the FastAPI app for the first time (models.Base.metadata.create_all(bind=engine) is used).

Step 2: Insert initial survey questions
Once the tables are created, insert the questions manually:

```bash
INSERT INTO questions (question) VALUES ('question 1');
INSERT INTO questions (question) VALUES ('question 2');
INSERT INTO questions (question) VALUES ('question 3');
```

This ensures that the survey has questions to display in the frontend.

## 🌐 CORS Configuration

```bash
allow_origins=["http://localhost:3000"]
```

This enables connection with the Next.js frontend.

## 📌 API Endpoints

🧑 Members /members
Method Path Description
GET / Get all members
GET /{id} Get member details by ID
POST / Create a new member
PUT /{email} Update a member
DELETE /{email} Delete a member

📋 Questions /questions
Method Path Description
GET / Get all survey questions

✍️ Answers /answers
Method Path Description
POST /{memberGuid} Submit answers for a member
GET /averages Get average survey results
GET /averages/report Download PDF of results

## 🧾 PDF Report Example

Generated using ReportLab
Aggregates all questions with average responses
Downloads as survey_report.pdf

## 🛠 Environment Variables

You can configure your .env file

```bash
DATABASE_URL='postgresql://user:password@localhost:5432/dbName'
```

## 📌 Notes

SQLAlchemy models are defined in models/
All DB interaction logic is in services/
All routes are modular under routes/ and registered in main.py

## 👨‍💻 Author

Developed by Elvira Vargas 😸
