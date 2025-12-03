# Python Scripting - Learning Repository

A comprehensive Python learning repository featuring practical examples of OS module operations, platform detection, subprocess management, system monitoring, and AWS CloudWatch integration.

## 📚 Table of Contents

- [Overview](#overview)
- [Modules & Projects](#modules--projects)
  - [OS Module](#os-module)
  - [Platform Module](#platform-module)
  - [Subprocess Module](#subprocess-module)
  - [System Monitoring](#system-monitoring)
  - [AWS Monitoring](#aws-monitoring)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Learning Path](#learning-path)
- [Contributing](#contributing)

## 🎯 Overview

This repository serves as a hands-on learning resource for Python developers looking to master:
- **File system operations** using the `os` module
- **Platform detection** and cross-platform development with `platform` module
- **Process management** and command execution with `subprocess` module
- **System resource monitoring** with `psutil`
- **AWS CloudWatch integration** with `boto3`
- Log parsing and real-time data analysis

## 📁 Modules & Projects

### OS Module

📂 **Location:** `os_module/`
📖 **[Full Documentation](os_module/README.md)**

Master file system operations and directory management with Python's built-in `os` module.

#### **What You'll Learn**
- Navigate and manipulate the file system
- Create single and nested directories
- List, rename, and delete files/folders
- Handle file permissions
- Build cross-platform path handling

#### **Example Files**
| File | Description | Key Functions |
|------|-------------|---------------|
| `os_change_cwd.py` | Change working directory | `os.getcwd()`, `os.mkdir()` |
| `os_create_dirs.py` | Create directories with permissions | `os.mkdir()` with mode |
| `os_mkdirs_func.py` | Create nested directory structures | `os.makedirs()` |
| `os_listing_files.py` | List directory contents | `os.listdir()` |
| `os_remove_files.py` | Delete files safely | `os.remove()` |
| `os_remove_dir.py` | Remove empty directories | `os.rmdir()` |
| `os_chng_path.py` | Navigate directory tree | `os.chdir()` |

#### **Quick Example**
```python
import os

# Get current directory and create nested structure
cwd = os.getcwd()
new_path = os.path.join(cwd, "parent", "child")
os.makedirs(new_path, exist_ok=True)

# List all files
files = os.listdir(cwd)
print(f"Files: {files}")
```

**[→ Read Complete OS Module Guide](os_module/README.md)**

---

### Platform Module

📂 **Location:** `platform_module/`
📖 **[Full Documentation](platform_module/README.md)**

Detect operating systems, hardware architecture, and write portable cross-platform code.

#### **What You'll Learn**
- Identify the operating system (Windows, Linux, macOS)
- Get hardware and processor information
- Detect system architecture (32-bit vs 64-bit)
- Access Linux distribution details
- Write code that adapts to different platforms

#### **Example Files**
| File | Description | Key Functions |
|------|-------------|---------------|
| `get_distro.py` | Cross-platform system detection | `platform.system()`, `platform.uname()`, `platform.win32_edition()` |

#### **Quick Example**
```python
import platform

# Detect operating system
os_name = platform.system()  # 'Windows', 'Linux', 'Darwin'

# Get architecture
arch = platform.machine()  # 'AMD64', 'x86_64', 'arm64'

# Platform-specific code
if os_name == "Windows":
    print(f"Windows {platform.release()}")
    print(f"Edition: {platform.win32_edition()}")
elif os_name == "Linux":
    print(f"Linux {platform.release()}")
else:
    print(f"macOS {platform.mac_ver()[0]}")
```

#### **Key Functions Covered**
- `platform.system()` - OS name
- `platform.machine()` - Architecture
- `platform.processor()` - CPU info
- `platform.platform()` - Complete platform string
- `platform.win32_edition()` - Windows edition (Windows only)
- `platform.freedesktop_os_release()` - Linux distribution (Linux only)
- `platform.uname()` - Comprehensive system info

**[→ Read Complete Platform Module Guide](platform_module/README.md)**

---

### Subprocess Module

📂 **Location:** `subprocess/`
📖 **[Full Documentation](subprocess/README.md)**

Execute external commands, run system programs, and manage child processes from Python.

#### **What You'll Learn**
- Run system commands programmatically
- Capture command output (stdout/stderr)
- Send input to running processes
- Chain commands using pipes
- Handle command errors and timeouts
- Write cross-platform command execution

#### **Example Files**
| File | Description | Key Functions |
|------|-------------|---------------|
| `check_output.py` | Cross-platform command execution | `subprocess.check_output()` with platform detection |
| `pipe_func.py` | Process piping and communication | `subprocess.PIPE`, `Popen()` |

#### **Quick Example**
```python
import subprocess
import platform

# Run command and capture output
output = subprocess.check_output(
    ["python", "--version"], 
    text=True
)
print(output)  # Python 3.13.9

# Cross-platform directory listing
if platform.system() == "Windows":
    result = subprocess.run(
        ["powershell", "-Command", "Get-ChildItem"],
        capture_output=True,
        text=True
    )
else:
    result = subprocess.run(
        ["ls", "-la"],
        capture_output=True,
        text=True
    )

print(result.stdout)
```

#### **Key Functions Covered**
- `subprocess.run()` - Execute command and wait
- `subprocess.check_output()` - Run and get output
- `subprocess.Popen()` - Advanced process control
- `subprocess.PIPE` - Connect process pipes
- Error handling with `CalledProcessError`

**[→ Read Complete Subprocess Module Guide](subprocess/README.md)**

---

### System Monitoring

📂 **Location:** `pymonitoring/project/`

Build real-time system monitoring applications with log analysis and data persistence.

#### **`my-system.py`** - Real-time System Monitor

**Features:**
- 📊 Real-time CPU usage monitoring
- 📝 Log file parsing and analysis
- 🔍 Pattern-based log filtering (ERROR, WARNING, INFO)
- 📈 Statistical analysis (averages)
- 💾 Data persistence to text files

**Functionality:**
```python
import psutil
import re
import time

# Monitor CPU usage
def monitor_cpu():
    return psutil.cpu_percent(interval=1)

# Query and filter logs
def query_logs(log_file, pattern):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    return [log for log in logs if re.search(pattern, log)]

# Calculate averages
def calculate_average(logs):
    try:
        values = [float(log.split()[-1]) for log in logs]
        return sum(values) / len(values)
    except ZeroDivisionError:
        return 0
```

**Output Files Generated:**
- `cpu_usage.txt` - Historical CPU usage data
- `error_values.txt` - Average values from ERROR logs
- `warning_values.txt` - Average values from WARNING logs
- `info_values.txt` - Average values from INFO logs

**Usage:**
```bash
cd pymonitoring/project
python my-system.py
# Press Ctrl+C to stop monitoring and save data
```

---

### AWS Monitoring

📂 **Location:** `awsmonitoring/project/`

Integrate with AWS CloudWatch to monitor cloud resources.

#### **`moni-aws.py`** - AWS CloudWatch Integration

**Features:**
- ☁️ AWS CloudWatch metrics retrieval
- 📊 EC2 instance monitoring
- 🔐 Secure credential management
- 📈 Time-series data collection

**Setup:**
```python
import boto3
from datetime import datetime, timedelta

# Configure AWS credentials
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='YOUR_REGION'
)

cloudwatch = session.client('cloudwatch')

# Get CloudWatch metrics
def get_metrics(namespace, metric_name, dimensions):
    response = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        Dimensions=dimensions,
        StartTime=datetime.utcnow() - timedelta(minutes=10),
        EndTime=datetime.utcnow(),
        Period=60,
        Statistics=['Average']
    )
    return response['Datapoints']

# Monitor EC2 instance
metrics = get_metrics(
    namespace='AWS/EC2',
    metric_name='CPUUtilization',
    dimensions=[{'Name': 'InstanceId', 'Value': 'YOUR_INSTANCE_ID'}]
)
```

---

## 🔧 Prerequisites

- **Python 3.7+** (recommended: Python 3.10 or higher)
- **pip** package manager
- **Git** for cloning the repository

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MaxiFine/project-monitoring.git
cd python-scripting
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
# For system monitoring
pip install psutil

# For AWS monitoring
pip install boto3

# Or install all at once
pip install psutil boto3
```

## 🚀 Usage

### OS Module Examples
```bash
cd os_module

# List files in a directory
python os_listing_files.py

# Create nested directories
python os_mkdirs_func.py

# Navigate and change directories
python os_chng_path.py

# Remove files and directories
python os_remove_files.py
```

### Platform Module Examples
```bash
cd platform_module

# Get comprehensive system information
python get_distro.py

# Output shows OS, architecture, processor, etc.
```

### Subprocess Module Examples
```bash
cd subprocess

# Execute cross-platform commands
python check_output.py

# Work with process pipes
python pipe_func.py
```

### System Monitoring
```bash
cd pymonitoring/project

# Start real-time monitoring (Ctrl+C to stop)
python my-system.py
```

### AWS Monitoring
```bash
cd awsmonitoring/project

# Configure your AWS credentials in moni-aws.py first!
python moni-aws.py
```

---

## 🎓 Learning Path

Follow this recommended order to build your Python skills progressively:

### 1️⃣ **Beginner: OS Module** (Start Here)
- Learn file system basics
- Understand path operations
- Practice directory management
- **Time:** 2-3 hours
- **[Start with OS Module →](os_module/README.md)**

### 2️⃣ **Beginner-Intermediate: Platform Module**
- Detect operating systems
- Write cross-platform code
- Understand system architecture
- **Time:** 1-2 hours
- **[Continue with Platform Module →](platform_module/README.md)**

### 3️⃣ **Intermediate: Subprocess Module**
- Execute external commands
- Capture and process output
- Handle errors gracefully
- **Time:** 2-3 hours
- **[Learn Subprocess Module →](subprocess/README.md)**

### 4️⃣ **Intermediate-Advanced: System Monitoring**
- Monitor system resources
- Parse and analyze logs
- Implement real-time data collection
- **Time:** 3-4 hours

### 5️⃣ **Advanced: AWS Integration**
- Connect to cloud services
- Retrieve metrics
- Manage credentials
- **Time:** 2-3 hours

---

## 💡 Key Concepts & Best Practices

### Cross-Platform Development
```python
import os
import platform

# ✅ Good - Works everywhere
path = os.path.join("folder", "subfolder", "file.txt")

# ❌ Bad - Windows only
path = "folder\\subfolder\\file.txt"

# ✅ Good - OS-specific code
if platform.system() == "Windows":
    # Windows-specific implementation
    pass
elif platform.system() == "Linux":
    # Linux-specific implementation
    pass
```

### Error Handling
```python
import os
import subprocess

# ✅ Always wrap file operations in try-except
try:
    os.remove("file.txt")
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("Permission denied")

# ✅ Handle subprocess errors
try:
    result = subprocess.check_output(["command"], text=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed: {e}")
except FileNotFoundError:
    print("Command not found")
```

### Resource Management
```python
# ✅ Good - Use context managers
with open("file.txt", "r") as f:
    data = f.read()

# ✅ Good - Clean up processes
process = subprocess.Popen(["command"])
try:
    process.wait(timeout=5)
finally:
    process.kill()  # Ensure cleanup
```

---

## 📊 Module Comparison

| Module | Purpose | Difficulty | Use Case |
|--------|---------|------------|----------|
| `os` | File system operations | ⭐ Beginner | Creating files, navigating directories |
| `platform` | System detection | ⭐ Beginner | Cross-platform compatibility |
| `subprocess` | Running commands | ⭐⭐ Intermediate | Executing external programs |
| `psutil` | System monitoring | ⭐⭐ Intermediate | CPU, memory, disk monitoring |
| `boto3` | AWS integration | ⭐⭐⭐ Advanced | Cloud resource management |

---

## 🤝 Contributing

Contributions are welcome! Ways to contribute:

- 🐛 **Report bugs** - Open an issue
- 💡 **Suggest features** - Share your ideas
- 📝 **Improve documentation** - Fix typos, add examples
- 🔧 **Submit code** - Create pull requests
- ⭐ **Star the repo** - Show your support

### How to Contribute
```bash
# Fork the repository
git clone https://github.com/YOUR_USERNAME/project-monitoring.git

# Create a feature branch
git checkout -b feature/your-feature-name

# Make changes and commit
git add .
git commit -m "Add: your feature description"

# Push and create PR
git push origin feature/your-feature-name
```

---

## 📝 Notes & Tips

### General Tips
- ✅ Use **virtual environments** to isolate dependencies
- ✅ Always **handle exceptions** for file and process operations
- ✅ Test code on **multiple platforms** when possible
- ✅ Use `os.path.join()` for **cross-platform paths**
- ✅ Check **permissions** before file operations

### Security Tips
- 🔐 Never commit **AWS credentials** or sensitive data
- 🔐 Use **environment variables** for secrets
- 🔐 Avoid `shell=True` in subprocess (security risk)
- 🔐 Validate **user input** before using in commands

### Performance Tips
- ⚡ Use `pathlib` for modern path operations (Python 3.4+)
- ⚡ Cache platform detection results if called frequently
- ⚡ Use `subprocess.run()` instead of older functions
- ⚡ Close file handles and processes properly

---

## 🔗 Additional Resources

### Official Documentation
- [Python os module](https://docs.python.org/3/library/os.html)
- [Python platform module](https://docs.python.org/3/library/platform.html)
- [Python subprocess module](https://docs.python.org/3/library/subprocess.html)
- [psutil documentation](https://psutil.readthedocs.io/)
- [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

### Related Topics
- [pathlib - Object-oriented paths](https://docs.python.org/3/library/pathlib.html)
- [shutil - High-level file operations](https://docs.python.org/3/library/shutil.html)
- [logging - Python logging facility](https://docs.python.org/3/library/logging.html)

---

## 📧 Contact & Support

- **Issues:** [GitHub Issues](https://github.com/MaxiFine/project-monitoring/issues)
- **Discussions:** [GitHub Discussions](https://github.com/MaxiFine/project-monitoring/discussions)
- **Repository:** [project-monitoring](https://github.com/MaxiFine/project-monitoring)

---

## 📄 License

This project is created for educational purposes. Feel free to use and modify for learning.

---

<div align="center">

**⭐ If you found this repository helpful, please consider giving it a star! ⭐**

**Happy Learning! 🚀 Keep Coding! 💻**

</div>

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
