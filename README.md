# 📊 Page Pulse

Page Pulse is a Flask-based web application that performs a quick website audit. It analyzes a webpage and displays important SEO and performance metrics in a clean, user-friendly dashboard.

---

## ✨ Features

- 🌐 HTTP Status Code
- ⚡ Response Time
- 📄 Page Title
- 📝 Meta Description
- 🏷️ H1 Tag Count
- 🖼️ Image Count
- 📚 Word Count
- ❌ Invalid URL Handling
- 📱 Responsive User Interface

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Libraries:**
  - Requests
  - BeautifulSoup4
- **Testing:** Pytest

---

## 📂 Project Structure

```
page-pulse/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_app.py
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/PreethaDevi28/page-pulse.git
```

### 2. Navigate to the project folder

```bash
cd page-pulse
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
py app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧪 Running Tests

Run the test suite using:

```bash
py -m pytest
```

Example Output:

```text
=========================
2 passed
=========================
```

---

## 📸 Application Preview

The application allows users to:

- Enter any website URL
- Perform a website audit
- View SEO and performance metrics
- Handle invalid URLs with proper error messages

---

## 👩‍💻 Author

**Preetha Devi**

GitHub: https://github.com/PreethaDevi28

---

## 📄 License

This project was created as part of a technical assessment and is intended for educational and demonstration purposes.