from flask import Flask, render_template, request, send_file
import json
from scraper import get_google_results

app = Flask(__name__)
last_results = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    global last_results
    last_results = get_google_results(query)
    print(last_results)
    return render_template("index.html", results=last_results)

@app.route("/download", methods=["GET"])
def download():
    global last_results
    filename = "results.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(last_results, f, ensure_ascii=False, indent=2)
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
