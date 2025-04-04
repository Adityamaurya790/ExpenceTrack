# Expense Tracker

A Django-based web application to track daily expenses and incomes. This project allows users to manage their financial data, view monthly summaries, and visualize their spending and income trends using interactive charts.

---

## Features

- **User Authentication**: Users can sign up, log in, and log out securely.
- **Add Income**: Users can add their monthly income.
- **Add Expenses**: Users can categorize and add daily expenses.
- **Monthly Summary**: Displays the total income and spending for the current month.
- **Interactive Charts**: Visualize income and expenses using bar and pie charts powered by Chart.js.
- **Real-Time Updates**: Charts and summaries update dynamically without page reloads using Axios.

---

## Technologies Used

- **Backend**: Django 5.1
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
- **Database**: SQLite
- **Charts**: Chart.js
- **AJAX**: Axios

---

## Installation

### Prerequisites
- Python 3.10 or higher
- Django 5.1 or higher
- SQLite (pre-installed with Python)

---

### Steps
1. Clone the repository:
```
git clone https://github.com/your-username/ExpenseTracker.git
cd ExpenseTracker
```
2. Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate  # On Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```
5. Create a superuser (for admin access):
```
python manage.py createsuperuser
```
6. Run the development server:
```
python manage.py runserver
```
7.Open the application in your browser:
```
http://127.0.0.1:8000/
```

---
# Usage

- Sign Up: Create a new account or log in with an existing account.
- Add Income: Enter your monthly income in the "Add Monthly Income" section.
- Add Expenses: Add daily expenses by selecting a category and entering the amount.
- View Summary: Check the monthly summary of income and spending.
- Visualize Data: View interactive charts for income and expenses.

---
# Requirements
Add the following to requirements.txt:
- Django>=5.1
- chart.js
- axios

---
# Screenshots
- Dashboard
<img alt="Dashboard Screenshot" src="https://via.placeholder.com/800x400?text=Dashboard+Screenshot">
- Add Income and Expenses
<img alt="Add Income and Expenses Screenshot" src="https://via.placeholder.com/800x400?text=Add+Income+and+Expenses">

---
# License
This project is licensed under the MIT License. See the LICENSE file for details.



