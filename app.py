
from gradio_client import Client
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
client = Client("sahilawatramani/crime-analytics-backend")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/gr_query", methods=["POST"])
def gr_query():
    query = request.json.get("query")
    response = client.predict(query, api_name="/gr_query")
    return jsonify(response)

@app.route("/api/gr_quick_stats", methods=["GET"])
def gr_quick_stats():
    response = client.predict(api_name="/gr_quick_stats")
    return jsonify(response)

@app.route("/api/gr_filter_options", methods=["GET"])
def gr_filter_options():
    response = client.predict(api_name="/gr_filter_options")
    return jsonify(response)

@app.route("/api/gr_sample_queries", methods=["GET"])
def gr_sample_queries():
    response = client.predict(api_name="/gr_sample_queries")
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
