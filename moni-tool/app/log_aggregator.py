import os
import pandas as pd

def fetch_local_logs(directory, log_format="txt"):
    logs = []
    for file_name in os.listdir(directory):
        if file_name.endswith(f".{log_format}"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r') as file:
                for line in file:
                    logs.append(line.strip())
    return logs

def parse_logs_to_dataframe(logs):
    """Parse logs into a DataFrame for easy querying and filtering."""
    log_entries = []
    for log in logs:
        # Assuming a sample log format: "[2024-12-28 10:00:00] INFO: User logged in"
        parts = log.split("] ")
        timestamp = parts[0][1:]  # Extract timestamp
        level, message = parts[1].split(": ", 1)
        log_entries.append({"timestamp": timestamp, "level": level, "message": message})
    return pd.DataFrame(log_entries)

# Example usage
logs = fetch_local_logs("./logs")
df = parse_logs_to_dataframe(logs)
print(df.head())


def aggregate_logs_by_level(log_df):
    """Calculate log level averages and counts."""
    summary = log_df['level'].value_counts().reset_index()
    summary.columns = ['level', 'count']
    return summary

# Example
summary = aggregate_logs_by_level(df)
print(summary)
