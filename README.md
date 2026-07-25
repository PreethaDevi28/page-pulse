# 📊 Page Pulse

Page Pulse is a Flask-based website auditing application that analyzes webpages and provides important SEO and performance insights through a simple and responsive dashboard.

The application helps users quickly understand webpage information such as response speed, HTML structure, and basic SEO elements.

---

## ✨ Features

- 🌐 HTTP Status Code Analysis
- ⚡ Website Response Time Measurement
- 📄 Page Title Extraction
- 📝 Meta Description Detection
- 🏷️ H1 Tag Count Analysis
- 🖼️ Image Count Detection
- 📚 Word Count Calculation
- ❌ Invalid URL Error Handling
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

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
py app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Running Tests

Run tests using:

```bash
py -m pytest
```

Successful output:

```text
5 passed in 1.00s
```

---

## 📸 Application Preview

The application allows users to:

- Enter a website URL
- Perform an automated website audit
- View SEO and performance metrics
- Receive clear error messages for invalid URLs

(Add your screenshot here)

---

## 👩‍💻 Author

**Preetha Devi**

GitHub:
https://github.com/PreethaDevi28

---

## 📄 License

This project was created as part of a technical assessment and is intended for educational and demonstration purposes.