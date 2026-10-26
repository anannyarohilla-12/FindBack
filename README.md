# FindBack – Lost & Found Smart Matching System

FindBack is a web-based Lost and Found Management System developed using Django. It helps users report lost and found items, browse reports, and identify possible matches between lost and found belongings.

## Features

* **User Registration and Login:** Users can create accounts and sign in.
* **Lost Item Reporting:** Submit reports for items that have been lost.
* **Found Item Reporting:** Submit reports for items that have been found.
* **Browse Items:** View available lost and found reports.
* **My Reports:** Manage your submitted reports.
* **Smart Matching:** Identify potential matches between lost and found items.
* **Data Analytics Dashboard:** View statistics and interactive charts for lost and found reports.
* **Recent Reports:** View the latest item reports.

## Technologies Used

* Python
* Django
* HTML
* CSS
* JavaScript
* Plotly
* Pandas
* NumPy
* SQLite

## Project Structure

```text
FindBack/
├── accounts/
├── analytics/
├── claims/
├── config/
├── matching/
├── reports/
├── templates/
├── manage.py
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/anannyarohilla-12/FindBack.git
```

### 2. Open the project folder

```bash
cd FindBack
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

Install the packages required by the project:

```bash
pip install django pandas numpy plotly
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

## Analytics Dashboard

The analytics dashboard provides:

* Total active reports
* Lost and found report counts
* Found report percentage
* Category distribution chart
* Monthly reports analysis
* Lost vs. found summary
* Recent reports table

## Project Purpose

The purpose of FindBack is to make the process of reporting and finding lost belongings more organized and convenient through a centralized web application.

## Future Scope

* Email notifications for potential matches
* Improved matching accuracy
* Image-based item matching
* Administrative analytics and reporting

## Author

**Anannya Rohilla**

## License

This project was developed as an academic minor project.
