# Python Scripting - Learning Repository

A comprehensive Python learning repository featuring practical examples of OS module operations, system monitoring, and AWS CloudWatch integration.

## 📚 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [OS Module](#os-module)
  - [System Monitoring](#system-monitoring)
  - [AWS Monitoring](#aws-monitoring)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Learning Objectives](#learning-objectives)
- [Contributing](#contributing)

## 🎯 Overview

This repository serves as a hands-on learning resource for Python developers looking to master:
- File system operations using the `os` module
- System resource monitoring with `psutil`
- AWS CloudWatch integration with `boto3`
- Log parsing and analysis
- Real-time data collection and processing

## 📁 Projects

### OS Module

Located in `os_module/`, this section demonstrates essential file system operations:

#### **Directory Operations**
- **`os_change_cwd.py`** - Change current working directory and navigate the file system
- **`os_create_dirs.py`** - Create single directories with `os.mkdir()`
- **`os_mkdirs_func.py`** - Create nested directory structures with `os.makedirs()`
- **`os_remove_dir.py`** - Remove empty directories using `os.rmdir()`
- **`os_chng_path.py`** - Navigate directory paths and change to parent directories

#### **File Operations**
- **`os_listing_files.py`** - List files and directories in a specified path
- **`os_remove_files.py`** - Delete files using `os.remove()`

#### **Key Concepts Covered**
```python
# Get current working directory
os.getcwd()

# Create directory with permissions
os.mkdir(path, mode=0o666)

# Create nested directories
os.makedirs(path, exist_ok=True)

# List directory contents
os.listdir(path)

# Join paths safely
os.path.join(parent, child)

# Remove files and directories
os.remove(file_path)
os.rmdir(directory_path)
```

### System Monitoring

Located in `pymonitoring/project/`, this section includes a robust system monitoring application:

#### **`my-system.py`** - Real-time System Monitor

**Features:**
- 📊 Real-time CPU usage monitoring
- 📝 Log file parsing and analysis
- 🔍 Pattern-based log filtering (ERROR, WARNING, INFO)
- 📈 Statistical analysis (averages)
- 💾 Data persistence to text files

**Functionality:**
```python
# Monitor CPU usage
def monitor_cpu():
    return psutil.cpu_percent(interval=1)

# Query and filter logs
def query_logs(log_file, pattern):
    # Returns logs matching pattern

# Calculate averages
def calculate_average(logs):
    # Computes mean values from log entries
```

**Output Files:**
- `cpu_usage.txt` - Historical CPU usage data
- `error_values.txt` - Average values from ERROR logs
- `warning_values.txt` - Average values from WARNING logs
- `info_values.txt` - Average values from INFO logs

**Usage:**
```bash
python my-system.py
# Press Ctrl+C to stop monitoring and save data
```

### AWS Monitoring

Located in `awsmonitoring/project/`, this section demonstrates AWS integration:

#### **`moni-aws.py`** - AWS CloudWatch Integration

**Features:**
- ☁️ AWS CloudWatch metrics retrieval
- 📊 EC2 instance monitoring
- 🔐 Secure credential management
- 📈 Time-series data collection

**Setup:**
```python
# Configure AWS credentials
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='YOUR_REGION'
)

# Get CloudWatch metrics
metrics = get_metrics(
    namespace='AWS/EC2',
    metric_name='CPUUtilization',
    dimensions=[{'Name': 'InstanceId', 'Value': 'YOUR_INSTANCE_ID'}]
)
```

## 🔧 Prerequisites

- Python 3.7 or higher
- pip package manager

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/MaxiFine/project-monitoring.git
cd python-scripting
```

2. **Install required packages:**
```bash
# For system monitoring
pip install psutil

# For AWS monitoring
pip install boto3
```

## 🚀 Usage

### Running OS Module Examples

```bash
cd os_module

# List files in a directory
python os_listing_files.py

# Create a new directory
python os_create_dirs.py

# Navigate directories
python os_chng_path.py
```

### Running System Monitor

```bash
cd pymonitoring/project

# Start real-time monitoring
python my-system.py

# Monitor runs continuously
# Press Ctrl+C to stop and save results
```

### Running AWS Monitor

```bash
cd awsmonitoring/project

# Edit moni-aws.py with your AWS credentials first
python moni-aws.py
```

## 🎓 Learning Objectives

By exploring this repository, you will learn:

1. **File System Management**
   - Navigate and manipulate directories
   - Create, read, and delete files
   - Understand path operations
   - Handle permissions and modes

2. **System Monitoring**
   - Monitor system resources in real-time
   - Parse and filter log files
   - Implement pattern matching with regex
   - Calculate statistics from data streams
   - Handle user interrupts gracefully

3. **Cloud Integration**
   - Connect to AWS services programmatically
   - Retrieve CloudWatch metrics
   - Work with time-series data
   - Manage AWS credentials securely

4. **Best Practices**
   - Exception handling
   - File I/O operations
   - Code organization and modularity
   - Function decomposition
   - Data persistence

## 📖 Code Examples

### Example 1: Directory Management
```python
import os

# Get current directory
cwd = os.getcwd()
print(f"Current Directory: {cwd}")

# Create nested directories
os.makedirs("parent/child/grandchild", exist_ok=True)

# List all files
files = os.listdir(cwd)
print(f"Files: {files}")
```

### Example 2: System Monitoring
```python
import psutil
import time

# Monitor CPU for 10 seconds
for _ in range(10):
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU: {cpu}%")
    time.sleep(1)
```

### Example 3: Log Analysis
```python
import re

def query_logs(log_file, pattern):
    with open(log_file, 'r') as f:
        logs = f.readlines()
    return [log for log in logs if re.search(pattern, log)]

# Find all ERROR entries
errors = query_logs('system.log', 'ERROR')
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 Notes

- Ensure you have proper permissions when running file system operations
- Replace AWS credentials with your own before running AWS examples
- The system monitor requires a `system.log` file to analyze
- Use virtual environments for package management

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Happy Learning! 🚀**
