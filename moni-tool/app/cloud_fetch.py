import boto3

def fetch_logs_from_cloudwatch(log_group, start_time, end_time):
    client = boto3.client('logs')
    response = client.filter_log_events(
        logGroupName=log_group,
        startTime=int(start_time.timestamp() * 1000),
        endTime=int(end_time.timestamp() * 1000)
    )
    logs = [event['message'] for event in response['events']]
    return logs


@app.route("/logs/export", methods=["GET"])
def export_logs():
    log_df.to_csv("exported_logs.csv", index=False)
    return jsonify({"message": "Logs exported successfully"})
