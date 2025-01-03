# Airport-Management-System
This is a Airport Management system built using Django and Vue. The website uses REST APIs to fetch information and display it on various URLs configured using Django. The frontend used is Vue which enables us to add/ delete/change of flights, passengers, employees. The admin website can be accessed using the admin protal of Django. For detailed instructions please follow: 

<h2>  Project Setup Guide</h2>

Follow these steps to set up and run the project on your local machine.

---

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Node.js**
   - Download from [Node.js official website](https://nodejs.org/en/download/).

2. **Python**
   - Download from [Python official website](https://python.org). Ensure you add Python to your system's PATH during installation.

3. **SQLite Studio**
   - Download from [SQLite Studio official website](https://sqlitestudio.pl).

4. **Postman**
   - Download from [Postman official website](https://www.postman.com/downloads/).

5. **A Code Editor**
   - Install Sublime Text, Visual Studio Code, or any preferred code editor.

---

## Setup Instructions

### 1. Verify Node.js Installation
   Open the Node.js command prompt and verify the installation by typing:
   ```bash
   node -v
   ```

### 2. Verify Python Installation
   Open the command prompt and verify the Python installation by typing:
   ```bash
   python --version
   ```

### 3. Create a Virtual Environment
   - Navigate to your project folder in the command prompt.
   - Create a virtual environment by typing:
     ```bash
     python -m venv environmentname
     ```
   - A folder named `environmentname` will be created in your project directory.

### 4. Activate the Virtual Environment
   - Navigate to the `Scripts` folder inside the virtual environment directory.
   - Activate the virtual environment by typing:
     ```bash
     activate
     ```

   **Relative Path:** `\My Project\mysite\env\Scripts`

### 5. Install Python Packages
   With the virtual environment activated, install the required Python packages:
   - **Django:**
     ```bash
     pip install django
     ```
   - **Django Rest Framework:**
     ```bash
     pip install djangorestframework
     ```
   - **CORS Headers:**
     ```bash
     pip install django-cors-headers
     ```

### 6. Configure SQLite Database
   - Open SQLite Studio.
   - Add the `db.sqlite3` file from the following directory: `\My Project\mysite`.

### 7. Start the Django Server
   - Navigate to the project folder (`\My Project\mysite`).
   - Run the following command to start the server:
     ```bash
     python manage.py runserver
     ```

### 8. Access the Admin Site
   - Open your browser and go to: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
   - Use the following credentials to log in:
     - **Email:** `b@gmail.com`
     - **Username:** `b`
     - **Password:** `admin`

### 9. Access the User Website
   - Navigate to `\My Project\frontend`.
   - Open the `index.html` file in a browser to access the user-facing website.

---

## Additional Tools

- **Postman**: Use Postman to test the functionality of APIs.

---

## Notes

- Ensure all prerequisites are correctly installed before proceeding.
- If you encounter issues, verify the environment variables and paths are set correctly.

---

## Contact

For questions or assistance, please reach out to the project maintainer.


<h2>Languages and Utilities Used</h2>

## Backend
- **Python**: Used for backend development and server-side scripting.
- **Django**: Python-based web framework for backend development.
- **Django Rest Framework**: Toolkit for building web APIs with Django.
- **SQLite**: Lightweight database for data storage.

## Frontend
- **HTML**: Structure of the user-facing website.
- **CSS**: Styling for the frontend.
- **Bootstrap**: CSS framework for responsive and modern UI design.
- **Vue.js**: JavaScript framework for building interactive user interfaces.

## Tools
- **Node.js**: Runtime environment for executing JavaScript code outside a browser.
- **Postman**: Tool for testing APIs.
- **SQLite Studio**: Database management tool.







<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)
  
