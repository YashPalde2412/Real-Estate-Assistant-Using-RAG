from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from rag import process_urls, generate_answer

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return send_from_directory(".", "estateiq_ui.html")

@app.route("/process", methods=["POST", "OPTIONS"])
def process():
    if request.method == "OPTIONS":
        return _cors_preflight()
    urls = request.json.get("urls", [])
    try:
        statuses = list(process_urls(urls))
        return jsonify({"status": statuses[-1]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/answer", methods=["POST", "OPTIONS"])
def answer():
    if request.method == "OPTIONS":
        return _cors_preflight()
    query = request.json.get("question", "")
    try:
        ans, sources = generate_answer(query)
        return jsonify({"answer": ans, "sources": sources})
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def _cors_preflight():
    response = jsonify({})
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response, 200

if __name__ == "__main__":
    app.run(debug=False, port=5000)