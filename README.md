# 💰 API-Powered Personal Finance Tracker

A professional RESTful backend service for tracking income, expenses, and generating financial summaries. Built with modern best practices including comprehensive input validation, error handling, and automated testing.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 🚀 Features

- **Complete CRUD Operations** - Create, read, update, and delete financial transactions
- **Input Validation** - Comprehensive validation with descriptive error messages
- **Error Handling** - Proper HTTP status codes and graceful error responses
- **Financial Analytics** - Monthly summaries with income vs expense tracking
- **Persistent Storage** - SQLite database with SQLAlchemy ORM
- **RESTful Design** - Clean API architecture following REST principles
- **Comprehensive Testing** - 20+ test cases covering positive, negative, and edge cases

## 🛠️ Tech Stack

- **Backend:** Python 3.8+, Flask
- **Database:** SQLite with SQLAlchemy ORM
- **API Design:** RESTful architecture
- **Testing:** REST Client test suite

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/EzekielB8/finance-tracker-api
cd finance-tracker-api
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python run.py
```

The API will be available at `http://127.0.0.1:5000`

## 📚 API Documentation

### Endpoints

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| POST | `/transactions` | Add a new transaction | 201, 400, 500 |
| GET | `/transactions` | Get all transactions | 200, 500 |
| GET | `/transactions/<id>` | Get single transaction | 200, 404, 500 |
| DELETE | `/transactions/<id>` | Delete a transaction | 200, 404, 500 |
| GET | `/summary/<month>` | Get monthly summary | 200, 400, 500 |

### Example Requests

#### Add a Transaction
```http
POST /transactions
Content-Type: application/json

{
  "amount": 50.00,
  "category": "Food",
  "type": "expense"
}
```

**Success Response (201):**
```json
{
  "message": "Transaction added successfully",
  "transaction": {
    "id": 1,
    "amount": 50.0,
    "category": "Food",
    "type": "expense",
    "date": "2026-01-02"
  }
}
```

**Error Response (400):**
```json
{
  "error": "Validation failed",
  "details": [
    "Amount must be greater than 0"
  ]
}
```

#### Get All Transactions
```http
GET /transactions
```

**Response (200):**
```json
{
  "count": 2,
  "transactions": [
    {
      "id": 1,
      "amount": 50.0,
      "category": "Food",
      "type": "expense",
      "date": "2026-01-02"
    },
    {
      "id": 2,
      "amount": 1000.0,
      "category": "Salary",
      "type": "income",
      "date": "2026-01-02"
    }
  ]
}
```

#### Get Monthly Summary
```http
GET /summary/1
```

**Response (200):**
```json
{
  "month": 1,
  "total_expenses": 50.0,
  "total_income": 1000.0,
  "net": 950.0,
  "expense_count": 1,
  "income_count": 1
}
```

## 🗄️ Database Schema

### Transaction Model

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | Integer | Primary Key | Unique identifier |
| amount | Float | NOT NULL | Transaction amount |
| category | String(50) | NOT NULL | Transaction category |
| type | String(10) | NOT NULL | 'income' or 'expense' |
| date | DateTime | Auto-generated | Transaction timestamp |

## 🧪 Testing

The project includes a comprehensive test suite in `test.http` with 20+ test cases.

### Run Tests
1. Ensure Flask is running: `python run.py`
2. Install REST Client extension in VS Code
3. Open `test.http`
4. Click "Send Request" above any test

### Test Coverage
- Positive tests (valid inputs)
- Negative tests (invalid inputs, missing fields)
- Edge cases (boundary values, long strings)
- Error handling (404s, 500s)

## 🎯 What I Learned

Building this project helped me develop skills in:

- **Backend Development:** Designing and implementing RESTful APIs with Flask
- **Database Design:** Creating normalized schemas and using ORMs effectively
- **Input Validation:** Implementing comprehensive validation logic and error handling
- **SQL:** Writing queries with SQLAlchemy and understanding database relationships
- **Testing:** Writing test suites and validating API behavior
- **Git:** Managing version control with meaningful commits
- **Professional Practices:** Code organization, documentation, and project structure

## 🔮 Future Enhancements

Potential features for future development:

- [ ] User authentication and authorization (JWT tokens)
- [ ] Budget tracking with spending alerts
- [ ] Data visualization dashboard
- [ ] Export functionality (CSV, PDF reports)
- [ ] Category management endpoints
- [ ] Recurring transaction support
- [ ] Multi-currency support
- [ ] Date range filtering for analytics

## 📁 Project Structure
```
finance-tracker-api/
│
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models
│   └── routes.py            # API endpoints
│
├── test.http                # API test suite
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## 🤝 Contributing

This is a portfolio project, but feedback and suggestions are welcome! Feel free to open an issue or reach out.

## 👤 Author

**Ezekiel Babara**
- GitHub: [@EzekielB8](https://github.com/EzekielB8)
- LinkedIn: [Ezekiel Babara](https://www.linkedin.com/in/ezekiel-babara-624560281/)

## 📝 License

This project is open source and available under the MIT License.

---

⭐ If you found this project helpful, please consider giving it a star!