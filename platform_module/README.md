# Platform Module in Python - Complete Guide

The `platform` module provides access to underlying platform's identifying data - system information, OS details, hardware architecture, and Python implementation details. It's essential for writing cross-platform code.

## 📚 Table of Contents
- [Overview](#overview)
- [Key Functions](#key-functions)
- [File Examples](#file-examples)
- [Common Use Cases](#common-use-cases)
- [Cross-Platform Development](#cross-platform-development)

## 🎯 Overview

The platform module enables you to:
- Detect the operating system (Windows, Linux, macOS)
- Get system architecture and processor information
- Retrieve Python version and implementation details
- Access Linux distribution information
- Write portable, cross-platform code

**Import:** `import platform`

---

## 🔑 Key Functions

### Basic System Information

#### `platform.system()` - Get OS Name
Returns the system/OS name: `'Windows'`, `'Linux'`, `'Darwin'` (macOS), `'Java'`.

```python
import platform

os_name = platform.system()
print(os_name)
# Windows: 'Windows'
# Linux: 'Linux'
# macOS: 'Darwin'
```

**Use case:** Conditional logic for different operating systems

---

#### `platform.platform(aliased=False, terse=False)` - Complete Platform String
Returns a comprehensive string identifying the platform.

```python
print(platform.platform())
# Windows: 'Windows-10-10.0.19045-SP0'
# Linux: 'Linux-5.15.0-56-generic-x86_64-with-glibc2.35'
# macOS: 'macOS-13.0.1-arm64-arm-64bit'
```

**Parameters:**
- `aliased`: If True, uses common names instead of technical ones
- `terse`: If True, returns minimal information

---

#### `platform.machine()` - Machine Type
Returns the machine type/architecture: `'AMD64'`, `'x86_64'`, `'arm64'`, `'i386'`.

```python
print(platform.machine())
# Windows 64-bit: 'AMD64'
# Linux 64-bit: 'x86_64'
# Mac M1/M2: 'arm64'
```

**Use case:** Determine if system is 32-bit or 64-bit

---

#### `platform.processor()` - Processor Name
Returns the processor name/identifier.

```python
print(platform.processor())
# 'Intel64 Family 6 Model 142 Stepping 10, GenuineIntel'
# 'x86_64'
# 'arm'
```

**Note:** Returns empty string on some systems; not always reliable

---

### Operating System Details

#### `platform.release()` - OS Release Version
Returns the system's release version.

```python
print(platform.release())
# Windows: '10'
# Linux: '5.15.0-56-generic'
# macOS: '22.1.0'
```

---

#### `platform.version()` - OS Version Details
Returns detailed version information.

```python
print(platform.version())
# Windows: '10.0.19045'
# Linux: '#58-Ubuntu SMP Thu Oct 13 08:03:55 UTC 2022'
# macOS: 'Darwin Kernel Version 22.1.0'
```

---

#### `platform.node()` - Network/Computer Name
Returns the computer's network name (hostname).

```python
print(platform.node())
# 'DESKTOP-ABC123'
# 'ubuntu-server'
# 'MacBook-Pro.local'
```

**Use case:** Identify which machine code is running on

---

### Windows-Specific Functions

#### `platform.win32_ver()` - Windows Version Details
Returns tuple: (release, version, csd, ptype)

```python
print(platform.win32_ver())
# ('10', '10.0.19045', 'SP0', 'Multiprocessor Free')
```

**Only works on Windows!**

---

#### `platform.win32_edition()` - Windows Edition
Returns the Windows edition: `'Professional'`, `'Home'`, `'Enterprise'`.

```python
if platform.system() == "Windows":
    print(platform.win32_edition())
    # 'Core'  # Windows Home
    # 'Professional'
```

---

### Linux-Specific Functions

#### `platform.freedesktop_os_release()` - Linux Distribution Info
Returns dictionary with OS information from `/etc/os-release`.

```python
try:
    info = platform.freedesktop_os_release()
    print(f"Name: {info['NAME']}")
    print(f"Version: {info['VERSION']}")
    print(f"ID: {info['ID']}")
except OSError:
    print("Not running on Linux or file not found")

# Ubuntu example:
# Name: Ubuntu
# Version: 22.04.1 LTS (Jammy Jellyfish)
# ID: ubuntu
```

**Important:** Only works on Linux systems with `/etc/os-release` file!

**Common keys in dictionary:**
- `NAME` - OS name
- `VERSION` - Version string
- `ID` - OS identifier (ubuntu, debian, fedora, etc.)
- `ID_LIKE` - Related OS families
- `VERSION_ID` - Version number

---

### Python Information

#### `platform.python_version()` - Python Version String
Returns Python version as string: `'3.13.9'`

```python
print(platform.python_version())
# '3.13.9'
# '3.11.0'
```

---

#### `platform.python_implementation()` - Python Implementation
Returns the Python implementation: `'CPython'`, `'PyPy'`, `'Jython'`, `'IronPython'`.

```python
print(platform.python_implementation())
# 'CPython'  # Standard Python
# 'PyPy'     # PyPy implementation
```

---

### Advanced Functions

#### `platform.uname()` - All System Information
Returns named tuple with comprehensive system info.

```python
info = platform.uname()
print(f"System: {info.system}")
print(f"Node: {info.node}")
print(f"Release: {info.release}")
print(f"Version: {info.version}")
print(f"Machine: {info.machine}")
print(f"Processor: {info.processor}")
```

**Returns namedtuple with:**
- `system` - OS name
- `node` - Network name
- `release` - OS release
- `version` - OS version
- `machine` - Hardware type
- `processor` - Processor name

---

## 📂 File Examples in This Directory

### **get_distro.py** - Cross-Platform System Information

This comprehensive example demonstrates platform detection and handles OS-specific functions gracefully.

```python
import platform

def get_platform_info():
    """
    Get cross-platform system information.
    Works on Windows, Linux, and macOS.
    """
    info = {
        "system": platform.system(),           # 'Windows', 'Linux', 'Darwin'
        "release": platform.release(),         # OS version
        "version": platform.version(),         # Detailed version
        "machine": platform.machine(),         # Machine type (e.g., 'x86_64', 'AMD64')
        "processor": platform.processor(),     # Processor name
        "platform": platform.platform(),       # Complete platform string
        "edition": platform.win32_edition() if platform.system() == "Windows" else "N/A",
        "system_alias": platform.system_alias(
            platform.system(),
            platform.release(),
            platform.version()
        ),
        "uname": platform.uname(),            # Named tuple with system info
        "machineNode": platform.node(),       # Network name (hostname)
    }
    return info


if __name__ == "__main__":
    print("=== Platform Information ===")
    platform_info = get_platform_info()
    for key, value in platform_info.items():
        print(f"{key.capitalize()}: {value}")
```

**Key Concepts:**

1. **Cross-Platform Detection:**
   - Uses `platform.system()` to detect OS
   - Conditional execution of Windows-specific functions
   - Gracefully handles unavailable functions

2. **Comprehensive Information Gathering:**
   - Collects all available system details
   - Returns structured dictionary
   - Easy to extend or filter

3. **Safe Windows Edition Check:**
   ```python
   "edition": platform.win32_edition() if platform.system() == "Windows" else "N/A"
   ```
   - Only calls Windows functions on Windows
   - Prevents errors on other systems

4. **Using `platform.uname()`:**
   - Named tuple with all system info
   - Single function call for complete data
   - Similar to Unix `uname` command

**Example Output on Windows:**
```
=== Platform Information ===
System: Windows
Release: 10
Version: 10.0.19045
Machine: AMD64
Processor: Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
Platform: Windows-10-10.0.19045-SP0
Edition: Core
System_alias: ('Windows', '10', '10.0.19045')
Uname: uname_result(system='Windows', node='DESKTOP-ABC', release='10', version='10.0.19045', machine='AMD64', processor='Intel64...')
Machinenode: DESKTOP-ABC
```

**Example Output on Linux:**
```
=== Platform Information ===
System: Linux
Release: 5.15.0-56-generic
Version: #62-Ubuntu SMP Tue Nov 22 19:54:14 UTC 2022
Machine: x86_64
Processor: x86_64
Platform: Linux-5.15.0-56-generic-x86_64-with-glibc2.35
Edition: N/A
System_alias: ('Linux', '5.15.0-56-generic', '#62-Ubuntu SMP Tue Nov 22 19:54:14 UTC 2022')
Uname: uname_result(system='Linux', node='ubuntu-server', release='5.15.0-56-generic', version='#62-Ubuntu SMP...', machine='x86_64', processor='x86_64')
Machinenode: ubuntu-server
```

**What It Teaches:**
- How to write cross-platform detection code
- Safe handling of OS-specific functions
- Collecting comprehensive system information
- Using named tuples for structured data
- Conditional execution based on OS

---

## 💡 Common Use Cases

### 1. Cross-Platform File Paths
```python
import platform
import os

def get_config_path():
    """Get configuration file path based on OS"""
    if platform.system() == "Windows":
        return os.path.join(os.environ['APPDATA'], 'myapp', 'config.ini')
    elif platform.system() == "Darwin":  # macOS
        return os.path.expanduser('~/Library/Application Support/myapp/config.ini')
    else:  # Linux
        return os.path.expanduser('~/.config/myapp/config.ini')

config_path = get_config_path()
print(f"Config location: {config_path}")
```

### 2. Conditional Package Installation
```python
import platform
import subprocess

def install_os_specific_package():
    """Install packages based on operating system"""
    system = platform.system()
    
    if system == "Windows":
        subprocess.run(["pip", "install", "pywin32"])
    elif system == "Linux":
        subprocess.run(["pip", "install", "python-xlib"])
    elif system == "Darwin":
        subprocess.run(["pip", "install", "pyobjc"])
    
    print(f"Installed packages for {system}")
```

### 3. System Requirements Check
```python
import platform
import sys

def check_system_requirements():
    """Verify system meets minimum requirements"""
    errors = []
    
    # Check Python version
    py_version = tuple(map(int, platform.python_version_tuple()))
    if py_version < (3, 8):
        errors.append(f"Python 3.8+ required, found {platform.python_version()}")
    
    # Check architecture
    if platform.machine() not in ['AMD64', 'x86_64', 'arm64']:
        errors.append(f"Unsupported architecture: {platform.machine()}")
    
    # Check OS
    if platform.system() not in ['Windows', 'Linux', 'Darwin']:
        errors.append(f"Unsupported OS: {platform.system()}")
    
    if errors:
        print("❌ System Requirements Not Met:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("✅ System requirements satisfied")

check_system_requirements()
```

### 4. Logging System Information
```python
import platform
import logging

def log_system_info():
    """Log system information for debugging"""
    logging.info("="*50)
    logging.info("SYSTEM INFORMATION")
    logging.info("="*50)
    logging.info(f"OS: {platform.system()} {platform.release()}")
    logging.info(f"Platform: {platform.platform()}")
    logging.info(f"Processor: {platform.processor()}")
    logging.info(f"Machine: {platform.machine()}")
    logging.info(f"Python: {platform.python_version()}")
    logging.info(f"Hostname: {platform.node()}")
    logging.info("="*50)

# Call at application startup
logging.basicConfig(level=logging.INFO)
log_system_info()
```

### 5. Feature Detection
```python
import platform

def get_available_features():
    """Determine available features based on system"""
    features = {
        'gui': True,
        'audio': True,
        'notifications': False,
    }
    
    system = platform.system()
    
    if system == "Linux":
        # Check for display server
        import os
        features['gui'] = 'DISPLAY' in os.environ
        features['notifications'] = True  # Most Linux has notification systems
    
    elif system == "Windows":
        features['notifications'] = int(platform.release()) >= 10
    
    elif system == "Darwin":
        features['notifications'] = True
    
    return features

features = get_available_features()
print(f"Available features: {features}")
```

---

## 🔄 Cross-Platform Development Tips

### 1. Always Check OS Before Using OS-Specific Functions
```python
import platform

# ✅ Good
if platform.system() == "Windows":
    edition = platform.win32_edition()

# ❌ Bad - Will crash on Linux
edition = platform.win32_edition()
```

### 2. Use Platform Detection for Paths
```python
# ✅ Good - Cross-platform
import os
path = os.path.join("folder", "file.txt")  # Works everywhere

# ❌ Bad - Windows-only
path = "folder\\file.txt"
```

### 3. Test on Multiple Platforms
- Develop on one platform
- Test on Windows, Linux, and macOS if possible
- Use CI/CD to test on multiple platforms automatically

### 4. Document Platform Requirements
```python
"""
This module requires:
- Python 3.8+
- Windows 10+ or Linux with X11
- 64-bit architecture
"""
```

---

## 📊 Platform Detection Patterns

### Pattern 1: Simple OS Switch
```python
import platform

os_name = platform.system()

if os_name == "Windows":
    # Windows-specific code
    print("Running on Windows")
elif os_name == "Linux":
    # Linux-specific code
    print("Running on Linux")
elif os_name == "Darwin":
    # macOS-specific code
    print("Running on macOS")
else:
    print(f"Unknown OS: {os_name}")
```

### Pattern 2: Feature-Based Detection
```python
import platform

class SystemInfo:
    def __init__(self):
        self.is_windows = platform.system() == "Windows"
        self.is_linux = platform.system() == "Linux"
        self.is_mac = platform.system() == "Darwin"
        self.is_64bit = platform.machine() in ['AMD64', 'x86_64']
    
    def __repr__(self):
        os_names = []
        if self.is_windows: os_names.append("Windows")
        if self.is_linux: os_names.append("Linux")
        if self.is_mac: os_names.append("macOS")
        
        bits = "64-bit" if self.is_64bit else "32-bit"
        return f"<SystemInfo: {', '.join(os_names)} ({bits})>"

sys_info = SystemInfo()
print(sys_info)
```

### Pattern 3: Dictionary-Based Dispatch
```python
import platform

def windows_specific():
    return "Windows implementation"

def linux_specific():
    return "Linux implementation"

def mac_specific():
    return "macOS implementation"

OS_HANDLERS = {
    "Windows": windows_specific,
    "Linux": linux_specific,
    "Darwin": mac_specific,
}

# Execute OS-specific function
handler = OS_HANDLERS.get(platform.system())
if handler:
    result = handler()
    print(result)
else:
    print("Unsupported OS")
```

---

## ⚠️ Common Pitfalls

### 1. Assuming Linux Distribution Info is Always Available
```python
# ❌ Bad - Crashes on Windows
info = platform.freedesktop_os_release()

# ✅ Good - Handle gracefully
try:
    info = platform.freedesktop_os_release()
    print(f"Linux distro: {info['ID']}")
except OSError:
    print("Not a Linux system with /etc/os-release")
```

### 2. Relying on `processor()` Always Returning Value
```python
# ❌ Bad - May return empty string
print(f"Processor: {platform.processor()}")

# ✅ Good - Provide fallback
proc = platform.processor() or platform.machine() or "Unknown"
print(f"Processor: {proc}")
```

### 3. Hardcoding Architecture Assumptions
```python
# ❌ Bad - Assumes x86_64
if platform.machine() == "x86_64":
    # Use 64-bit libraries

# ✅ Good - Check multiple possibilities
if platform.machine() in ["x86_64", "AMD64", "arm64"]:
    # Use 64-bit libraries
```

---

## 🔗 Related Modules

- **`sys`** - System-specific parameters and functions
- **`os`** - Operating system interfaces
- **`subprocess`** - Run system commands
- **`distro`** - Third-party module for detailed Linux distribution info

---

## 📖 Additional Resources

- [Official platform documentation](https://docs.python.org/3/library/platform.html)
- [Cross-platform Python development guide](https://docs.python.org/3/howto/index.html)
- [PEP 11 - Removing support for little used platforms](https://peps.python.org/pep-0011/)
