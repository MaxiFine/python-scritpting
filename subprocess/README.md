# Subprocess Module in Python - Complete Guide

The `subprocess` module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It's a powerful tool for running external commands and programs from within Python.

## QUICK LINK

- https://www.geeksforgeeks.org/python/python-subprocess-module/


## 📚 Table of Contents
- [Overview](#overview)
- [Key Functions](#key-functions)
- [File Examples](#file-examples)
- [Common Use Cases](#common-use-cases)
- [Best Practices](#best-practices)

## 🎯 Overview

The subprocess module enables you to:
- Run system commands or external programs from your Python script
- Capture output (stdout) and error messages (stderr)
- Send input (stdin) to running processes
- Wait for processes to complete and check return codes
- Chain multiple commands together using pipes

**Import:** `import subprocess`

---

## 🔑 Key Functions

### `subprocess.run()` - Run a Command
The recommended way to run subprocesses. Returns a `CompletedProcess` instance.

```python
import subprocess

# Basic usage
result = subprocess.run(["python", "--version"])
# Runs command and waits for completion

# Capture output
result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)
print(result.stdout)  # Python 3.13.9
print(result.returncode)  # 0 (success)
```

**Parameters:**
- `args`: Command and arguments as list
- `capture_output`: Capture stdout and stderr (bool)
- `text`: Return output as string instead of bytes (bool)
- `check`: Raise exception if command fails (bool)
- `timeout`: Maximum seconds to wait (int/float)

---

### `subprocess.check_output()` - Run and Get Output
Runs a command and returns its output. Raises exception if command fails.

```python
import subprocess

# Get command output directly
output = subprocess.check_output(["python", "--version"], text=True)
print(output)  # Python 3.13.9

# Handle errors
try:
    result = subprocess.check_output(
        ["invalid_command"],
        text=True,
        stderr=subprocess.STDOUT
    )
except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
    print(f"Output: {e.output}")
```

**When to use:**
- You only need the output, not the return code
- You want automatic error handling
- Simple, one-line command execution

**📁 Example File:** `check_output.py`

---

### `subprocess.PIPE` - Connect Process Pipes
Special value that can be used for stdin, stdout, or stderr to indicate that a pipe should be opened.

```python
import subprocess

# Pipe output between commands
p1 = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "hello"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Allow p1 to receive SIGPIPE if p2 exits
output = p2.communicate()[0]
print(output.decode())  # hello world
```

**Common uses:**
- Chain commands together (like Unix pipes)
- Capture command output for processing
- Send data to command input

**📁 Example File:** `pipe_func.py`

---

### `subprocess.Popen()` - Advanced Process Control
Lower-level interface for more control over process execution.

```python
import subprocess

# Start process without waiting
process = subprocess.Popen(
    ["python", "script.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Do other work while process runs...

# Wait for completion and get output
stdout, stderr = process.communicate()
return_code = process.returncode

print(f"Output: {stdout}")
print(f"Errors: {stderr}")
print(f"Return code: {return_code}")
```

**When to use:**
- Need to interact with process while it runs
- Want to start process and continue without waiting
- Need fine-grained control over stdin/stdout/stderr

---

## 📂 File Examples in This Directory

### 1. **check_output.py** - Cross-Platform Command Execution

This example demonstrates how to run commands in a cross-platform way, handling differences between Windows and Unix systems.

```python
import subprocess
import platform

try:
    # Check Python version - works on all platforms
    ans = subprocess.check_output(["python", "--version"], text=True)
    print(f"check_output: \nresult: {ans}")
    
    # Get current working directory - platform-specific
    if platform.system() == "Windows":
        # On Windows, use PowerShell command
        paths = subprocess.check_output(
            ["powershell", "-Command", "(Get-Location).Path"], 
            text=True
        )
    else:
        # On Unix/Linux/macOS, use 'pwd'
        paths = subprocess.check_output(["pwd"], text=True)
    
    print(f"Current Working Directory: {paths.strip()}")

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
except FileNotFoundError as e:
    print(f"Command not found: {e}")
```

**Key Concepts:**
1. **`subprocess.check_output()`** - Runs command and returns output as string
2. **`text=True`** - Returns string instead of bytes (easier to work with)
3. **Platform detection** - Uses `platform.system()` to run appropriate commands
4. **Error handling** - Catches both command failures and missing commands
5. **`.strip()`** - Removes trailing newlines from output

**What happens:**
- Checks Python version (works everywhere)
- Gets current directory using OS-specific command:
  - Windows: PowerShell's `(Get-Location).Path`
  - Linux/macOS: `pwd` command
- Prints results cleanly

**Output on Windows:**
```
check_output: 
result: Python 3.13.9

Current Working Directory: C:\Users\MaxwellAdomako\amalitech\lprojects\python-scripting\subprocess
```

**Common Issues Fixed:**
- ❌ `pwd` doesn't exist on Windows → ✅ Use PowerShell command
- ❌ Command not found errors → ✅ Added FileNotFoundError handling
- ❌ Extra whitespace in output → ✅ Use `.strip()` to clean

---

### 2. **pipe_func.py** - Process Communication with Pipes

This file will demonstrate piping data between processes (to be implemented).

**Example concepts to cover:**
```python
import subprocess

# Example 1: Simple pipe
# Unix: echo "hello" | grep "h"
p1 = subprocess.Popen(["echo", "hello"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "h"], stdin=p1.stdout, stdout=subprocess.PIPE)
output, _ = p2.communicate()
print(output.decode())

# Example 2: Capture and process output
process = subprocess.Popen(
    ["python", "--version"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
stdout, stderr = process.communicate()
print(f"Standard output: {stdout}")
print(f"Standard error: {stderr}")

# Example 3: Send input to process
process = subprocess.Popen(
    ["python"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)
stdout, _ = process.communicate(input="print('Hello from subprocess')")
print(stdout)
```

**What it teaches:**
- Using `subprocess.PIPE` to connect processes
- `communicate()` for sending/receiving data
- Chaining commands like Unix pipes
- stdin/stdout/stderr redirection

---

## 💡 Common Use Cases

### 1. Running Git Commands
```python
import subprocess

def run_git_command(command):
    """Run a git command and return output"""
    try:
        result = subprocess.check_output(
            ["git"] + command.split(),
            text=True,
            stderr=subprocess.STDOUT
        )
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

# Usage
status = run_git_command("status --short")
print(status)
```

### 2. Running Tests and Capturing Results
```python
import subprocess

def run_tests(test_file):
    """Run pytest and capture results"""
    result = subprocess.run(
        ["pytest", test_file, "-v"],
        capture_output=True,
        text=True
    )
    
    print(f"Exit code: {result.returncode}")
    print(f"Output:\n{result.stdout}")
    
    if result.returncode == 0:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed")
        print(f"Errors:\n{result.stderr}")
    
    return result.returncode == 0

run_tests("test_app.py")
```

### 3. Installing Python Packages Programmatically
```python
import subprocess
import sys

def install_package(package_name):
    """Install a Python package using pip"""
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package_name]
        )
        print(f"✅ Successfully installed {package_name}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package_name}")
        return False

# Install multiple packages
packages = ["requests", "pandas", "numpy"]
for pkg in packages:
    install_package(pkg)
```

### 4. Running System Commands with Timeout
```python
import subprocess

def run_with_timeout(command, timeout_seconds=5):
    """Run command with timeout to prevent hanging"""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=True
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        print(f"⏱️ Command timed out after {timeout_seconds} seconds")
        return None
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {e}")
        return None

# Run a potentially slow command
output = run_with_timeout(["python", "slow_script.py"], timeout_seconds=10)
```

### 5. Cross-Platform File Listing
```python
import subprocess
import platform

def list_files(directory="."):
    """List files in directory (cross-platform)"""
    if platform.system() == "Windows":
        command = ["powershell", "-Command", f"Get-ChildItem '{directory}'"]
    else:
        command = ["ls", "-la", directory]
    
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    
    return result.stdout

print(list_files())
```

---

## ⚙️ Best Practices

### 1. Use Lists for Commands
```python
# ✅ Good - prevents shell injection
subprocess.run(["ls", "-la", "/tmp"])

# ❌ Bad - vulnerable to injection if using user input
subprocess.run("ls -la /tmp", shell=True)
```

### 2. Always Handle Errors
```python
try:
    result = subprocess.check_output(["command"], text=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed: {e}")
except FileNotFoundError:
    print("Command not found")
```

### 3. Use `text=True` for String Output
```python
# ✅ Good - returns string
output = subprocess.check_output(["python", "--version"], text=True)

# ❌ Older style - returns bytes
output = subprocess.check_output(["python", "--version"])
output = output.decode('utf-8')
```

### 4. Specify Timeout for Long-Running Commands
```python
try:
    result = subprocess.run(
        ["long_running_command"],
        timeout=30,  # Prevent hanging
        capture_output=True
    )
except subprocess.TimeoutExpired:
    print("Command took too long!")
```

### 5. Use `check=True` for Critical Commands
```python
# Automatically raises exception if command fails
subprocess.run(
    ["critical_command"],
    check=True,  # Raises CalledProcessError if fails
    capture_output=True
)
```

---

## 🔒 Security Considerations

1. **Avoid `shell=True`** - Can lead to shell injection attacks
2. **Validate user input** - Never pass unsanitized user input to commands
3. **Use absolute paths** - When possible, use full paths to executables
4. **Set timeouts** - Prevent resource exhaustion from hanging processes
5. **Handle sensitive data** - Be careful with passwords in command arguments

---

## 📊 Comparison: run() vs check_output() vs Popen()

| Feature | `run()` | `check_output()` | `Popen()` |
|---------|---------|------------------|-----------|
| Returns | CompletedProcess | Output string | Popen object |
| Error handling | Manual (check=True) | Automatic | Manual |
| Complexity | Medium | Simple | Advanced |
| Use case | General purpose | Get output quickly | Fine control |
| Python version | 3.5+ | All | All |

---

## ⚠️ Common Errors and Solutions

### Error: `FileNotFoundError`
**Cause:** Command doesn't exist or not in PATH
```python
# Solution: Check if command exists first
import shutil
if shutil.which("command_name"):
    subprocess.run(["command_name"])
else:
    print("Command not found")
```

### Error: `CalledProcessError`
**Cause:** Command returned non-zero exit code
```python
# Solution: Handle the error
try:
    subprocess.check_output(["command"])
except subprocess.CalledProcessError as e:
    print(f"Failed with code {e.returncode}")
```

### Error: Command works in terminal but not in Python
**Cause:** Different environment or shell
```python
# Solution: Use absolute paths or set environment
subprocess.run(
    ["/usr/bin/python3", "script.py"],
    env={"PATH": "/usr/bin:/usr/local/bin"}
)
```

---

## 🔗 Related Modules

- **`os.system()`** - Older, simpler way to run commands (use subprocess instead)
- **`shlex`** - Parse shell-like syntax safely
- **`asyncio.subprocess`** - Async subprocess operations

---

## 📖 Additional Resources

- [Official subprocess documentation](https://docs.python.org/3/library/subprocess.html)
- [subprocess.run() documentation](https://docs.python.org/3/library/subprocess.html#subprocess.run)
- [Security considerations](https://docs.python.org/3/library/subprocess.html#security-considerations)


