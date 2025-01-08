from flask import Flask, request, jsonify
from app.log_aggregator import fetch_local_logs, parse_logs_to_dataframe, query_logs

app = Flask(__name__)

# Load and parse logs on startup
logs = fetch_local_logs("./logs")
log_df = parse_logs_to_dataframe(logs)

@app.route("/logs/query", methods=["GET"])
def query_logs_endpoint():
    level = request.args.get("level")
    keyword = request.args.get("keyword")
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")

    results = query_logs(log_df, level=level, keyword=keyword, start_time=start_time, end_time=end_time)
    return jsonify(results.to_dict(orient="records"))

@app.route("/logs/summary", methods=["GET"])
def logs_summary_endpoint():
    summary = aggregate_logs_by_level(log_df)
    return jsonify(summary.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
