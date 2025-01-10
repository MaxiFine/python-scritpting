# import os
# import pandas as pd

# # TODO
# # IDENTIFY THE PATH AND RUN THE APP
# # NOW MOVING UNTO CLOUD TO MONITOR EC2 INSTANCE

# # directory = r"/mnt/c/Users/MaxwellAdomako/aws-projects/paul-assign/moni-tool/app"
# directory = r"/var/log"

# def fetch_local_logs(directory, log_format="txt"):
#     logs = []
#     for file_name in os.listdir(directory):
#         if file_name.endswith(f".{log_format}"):
#             file_path = os.path.join(directory, file_name)
#             with open(file_path, 'r') as file:
#                 for line in file:
#                     logs.append(line.strip())
#     return logs

# def parse_logs_to_dataframe(logs):
#     """Parse logs into a DataFrame for easy querying and filtering."""
#     log_entries = []
#     for log in logs:
#         # Assuming a sample log format: "[2024-12-28 10:00:00] INFO: User logged in"
#         parts = log.split("] ")
#         timestamp = parts[0][1:]  # Extract timestamp
#         level, message = parts[1].split(": ", 1)
#         log_entries.append({"timestamp": timestamp, "level": level, "message": message})
#     return pd.DataFrame(log_entries)

# # Example usage
# logs = fetch_local_logs(directory)
# df = parse_logs_to_dataframe(logs)
# print(df.head())


# def aggregate_logs_by_level(log_df):
#     """Calculate log level averages and counts."""
#     summary = log_df['level'].value_counts().reset_index()
#     summary.columns = ['level', 'count']
#     return summary

# # # Example
# # summary = aggregate_logs_by_level(df)
# # print(summary)

# change of plans
# NOW GOING TO USE THE WLS ENVIRONMENT ONLY FOR THE WORK

import os
import pandas as pd

# directory = r"/mnt/c/Users/MaxwellAdomako/aws-projects/paul-assign/moni-tool/app"
directory = r"/var/log"

def fetch_local_logs(directory, log_format="txt"):
    logs = []
    try:
        for file_name in os.listdir(directory):
            if file_name.endswith(f".{log_format}"):
                file_path = os.path.join(directory, file_name)
                with open(file_path, 'r') as file:
                    for line in file:
                        logs.append(line.strip())
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")
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
logs = fetch_local_logs(directory)
if logs:
    df = parse_logs_to_dataframe(logs)
    print(df.head())
else:
    print("No logs found or unable to access the directory.")

def aggregate_logs_by_level(log_df):
    """Calculate log level averages and counts."""
    summary = log_df['level'].value_counts().reset_index()
    summary.columns = ['level', 'count']
    return summary

# # Example
# summary = aggregate_logs_by_level(df)
# print(summary)


    """
            import os

def list_files_in_directory(directory):
    '
    List all files and directories in the given path.

    Args:
        directory (str): Path to the directory.

    Returns:
        list: A list of files and directories in the specified path.
    '
    try:
        # Ensure the directory exists
        if not os.path.exists(directory):
            print(f"Error: Directory '{directory}' does not exist.")
            return []
        
        # Ensure the path is a directory
        if not os.path.isdir(directory):
            print(f"Error: Path '{directory}' is not a directory.")
            return []
        
        # List all items in the directory
        items = os.listdir(directory)
        return items
    except PermissionError as e:
        print(f"Permission Error: {e}")
        return []
    except FileNotFoundError as e:
        print(f"File Not Found Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return []

    """