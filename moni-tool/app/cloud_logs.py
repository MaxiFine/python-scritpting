import boto3
import datetime

def get_logs(log_group_name, log_stream_name, start_time=None, end_time=None):
    """
    Fetch logs from a specific log stream in CloudWatch Logs.

    Args:
        log_group_name (str): Name of the CloudWatch Logs group.
        log_stream_name (str): Name of the log stream.
        start_time (datetime, optional): Start time for fetching logs.
        end_time (datetime, optional): End time for fetching logs.

    Returns:
        list: List of log events.
    """
    client = boto3.client('logs')

    # Convert times to milliseconds since epoch
    start_time_ms = int(start_time.timestamp() * 1000) if start_time else None
    end_time_ms = int(end_time.timestamp() * 1000) if end_time else None

    try:
        response = client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            startTime=start_time_ms,
            endTime=end_time_ms,
            startFromHead=True  # Fetch from the beginning
        )

        events = response['events']
        return events
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace these with your log group and stream names
    LOG_GROUP_NAME = "/aws/ec2/instance-logs"
    LOG_STREAM_NAME = "instance-id/var/log/messages"

    # Optional time filter (last hour)
    now = datetime.datetime.utcnow()
    one_hour_ago = now - datetime.timedelta(hours=1)

    logs = get_logs(LOG_GROUP_NAME, LOG_STREAM_NAME, start_time=one_hour_ago, end_time=now)

    print(f"Fetched {len(logs)} log events.")
    for log in logs:
        print(log['message'])
