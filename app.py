from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/audit", methods=["POST"])
def audit():

    data = request.get_json()

    url = data.get("url")

    if not url:
        return jsonify({"error": "Please enter a URL"}), 400

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:

        start = time.time()

        response = requests.get(url, timeout=10)

        end = time.time()

        response_time = round(end - start, 2)

        if "text/html" not in response.headers.get("Content-Type", ""):
            return jsonify({"error": "URL is not an HTML page"}), 400

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"

        meta = soup.find("meta", attrs={"name": "description"})

        meta_description = (
            meta["content"] if meta and meta.get("content") else "No Meta Description"
        )

        h1_count = len(soup.find_all("h1"))

        image_count = len(soup.find_all("img"))

        words = soup.get_text(separator=" ", strip=True)

        word_count = len(words.split())

        return jsonify({
            "status": response.status_code,
            "response_time": response_time,
            "title": title,
            "meta_description": meta_description,
            "h1_count": h1_count,
            "image_count": image_count,
            "word_count": word_count
        })

    except requests.exceptions.Timeout:
        return jsonify({"error": "Request Timed Out"}), 408

    except requests.exceptions.RequestException:
        return jsonify({"error": "Invalid URL"}), 400


if __name__ == "__main__":
    app.run(debug=True)