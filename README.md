# Running Django Applications and Managing the Environment

This guide provides instructions to run Django applications on different ports, manage Python dependencies, and configure your environment.

---

## **Setup**

### 1. **Install Required Dependencies**
Install all the dependencies specified in `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### 2. **Set Environment Variables**
Set the `OPENAI_API_KEY` environment variable (replace `"your_api_key_here"` with your actual API key):
```bash
setx OPENAI_API_KEY "your_api_key_here"
```

---

## **Running the Django Server**

### 1. **Default Port (8000)**
Run the development server:
```bash
python manage.py runserver
```

### 2. **Custom Port (e.g., 8001)**
Run the server on a different port:
```bash
python manage.py runserver 8001
```

---

## **Managing Static Files**

To collect static files, run:
```bash
python manage.py collectstatic
```

---

## **Virtual Environment Setup**

### 1. **Create a Virtual Environment**
Create a virtual environment named `audiotrnas`:
```bash
python -m venv audiotrnas
```

### 2. **Activate the Virtual Environment**
- **Windows**:
  ```bash
  cd djangoProjects\project1
  .\audiotrnas\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source audiotrnas/bin/activate
  ```

---

## **Managing Dependencies**

### 1. **Check for Outdated Dependencies**
List outdated dependencies:
```bash
pip list --outdated
```

### 2. **Freeze Dependencies**
Update `requirements.txt` with the currently installed packages:
```bash
pip freeze > requirements.txt
```

---

## **Project Navigation**

### 1. **Change Directory**
Navigate to the project directory:
```bash
cd djangoProjects\project1
```

### 2. **Open Command Palette**  
Press `Ctrl + Shift + P` to open the command palette in supported editors.

---

## **Running Django Projects via Batch File**

### 1. **Create and Run Batch File**
Run your Django project using a batch file:
```bash
.\runproject1.bat
```

---

## **Starting a New Django Application**

### Create a New Application
Start a new Django app (replace `project1` with your app name):
```bash
python manage.py startapp project1
```

