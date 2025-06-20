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

## ## 🔧 Enhancement Idea

This backend can be enhanced to support **evaluations aligned with having multiple managers**. The improvement would introduce a `Manager` entity and extend the data model as follows:

- 👤 **Managers** are related to a group of team members (1:N relationship).
- 🧑‍🤝‍🧑 **Team Members** are assigned to a manager but do not appear in the answer data.
- 📝 **Answers** are submitted anonymously, they are **not linked to team members**, ensuring confidentiality.
- 🔗 However, answers are **linked to a specific manager ID**, allowing the aggregation of feedback per manager.
- 📊 The report generation logic can be extended to support breakdowns **by manager and their team**.

Implementing this structure would enable confidential leadership assessments that are structured, scalable, and compliant with anonymity requirements.

## 📌 Documentation of Assumptions

The following assumptions have been made during the development of this backend system:

1. **Fixed Question Set**

   - The survey operates with a fixed set of questions. New questions are not added dynamically once the survey cycle starts.

2. **One Submission per Member**

   - Each member can submit answers only once. There is no option to edit or re-submit.

3. **Anonymous Responses (for future enhancement)**

   - In the enhanced version, team members submit answers anonymously. While member records exist, answers are not linked to them.

4. **Manager-Team Relationship (planned)**

   - Each manager is expected to have multiple team members.

5. **Survey Results Are Read-Only Once Submitted**

   - No modification or deletion of answers is supported after submission, in order to preserve integrity of analytics.

6. **PDF Reports Are Generated On Demand**

   - Report generation is dynamic and does not persist PDFs to disk or cloud storage unless implemented separately.

7. **No Authentication Layer Yet**

   - This backend assumes it is used in a secure, internal environment or behind an API gateway. Authentication (JWT, OAuth) is not yet implemented.

8. **Database Schema Auto Creation**
   - Tables are auto-generated using `SQLAlchemy` on app startup via `Base.metadata.create_all`. This is acceptable for development, but not recommended for production without migrations.

## 👨‍💻 Author

Developed by Elvira Vargas 😸
