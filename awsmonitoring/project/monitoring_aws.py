import boto3
import datetime

# Create a CloudWatch Logs client
client = boto3.client('logs')

# Function to get logs from CloudWatch
def get_logs(log_group_name, start_time, end_time):
    response = client.filter_log_events(
        logGroupName=log_group_name,
        startTime=start_time,
        endTime=end_time,
        limit=100  # Adjust as needed
    )
    return response['events']

# Define log group name and time range
log_group_name = '/aws/lambda/your_lambda_function'  # Change as needed
start_time = int((datetime.datetime.now() - datetime.timedelta(hours=1)).timestamp() * 1000)  # 1 hour ago
end_time = int(datetime.datetime.now().timestamp() * 1000)  # Now

# Fetch logs
logs = get_logs(log_group_name, start_time, end_time)

# Print logs
for log in logs:
    print(log['message'])
