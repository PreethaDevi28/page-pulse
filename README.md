# 📊 Page Pulse

Page Pulse is a Flask-based web application that performs a quick website audit by analyzing a webpage and displaying useful SEO and performance information.

---

## Features

- 🌐 HTTP Status Code
- ⚡ Response Time
- 📄 Page Title
- 📝 Meta Description
- 🏷️ H1 Tag Count
- 🖼️ Image Count
- 📚 Word Count
- ❌ Invalid URL Handling

---

## Technologies Used

- Python
- Flask
- Requests
- BeautifulSoup4
- HTML
- CSS
- JavaScript
- Pytest

---

## Installation

Clone the repository:

```bash
git clone https://github.com/PreethaDevi28/page-pulse.git
```

Move into the project folder:

```bash
cd page-pulse
```

Create a virtual environment:

```bash
py -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
py app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Running Tests

```bash
py -m pytest
```

---

## Project Structure

```
page-pulse/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── tests/
    └── test_app.py
```

---

## Author

Preetha