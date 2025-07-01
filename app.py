from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
GRADIO_BACKEND_URL = "https://sahilawatramani-crime-analytics-backend.hf.space"

@app.route("/api/gr_query", methods=["POST"])
def gr_query():
    user_query = request.json.get("query")
    response = requests.post(
        f"{GRADIO_BACKEND_URL}/gr_query",
        json={"query": user_query}
    )
    return jsonify(response.json()), response.status_code

@app.route("/api/gr_quick_stats", methods=["GET"])
def gr_quick_stats():
    response = requests.get(f"{GRADIO_BACKEND_URL}/gr_quick_stats")
    return jsonify(response.json()), response.status_code

@app.route("/api/gr_filter_options", methods=["GET"])
def gr_filter_options():
    response = requests.get(f"{GRADIO_BACKEND_URL}/gr_filter_options")
    return jsonify(response.json()), response.status_code

@app.route("/api/gr_sample_queries", methods=["GET"])
def gr_sample_queries():
    response = requests.get(f"{GRADIO_BACKEND_URL}/gr_sample_queries")
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=True) 