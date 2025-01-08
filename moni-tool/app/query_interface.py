def query_logs(log_df, level=None, keyword=None, start_time=None, end_time=None):
    """Filter logs based on conditions."""
    filtered_logs = log_df

    if level:
        filtered_logs = filtered_logs[filtered_logs['level'] == level]
    if keyword:
        filtered_logs = filtered_logs[filtered_logs['message'].str.contains(keyword, case=False)]
    if start_time and end_time:
        filtered_logs = filtered_logs[
            (filtered_logs['timestamp'] >= start_time) & (filtered_logs['timestamp'] <= end_time)
        ]

    return filtered_logs

# Example query
results = query_logs(df, level="INFO", keyword="login")
print(results)
