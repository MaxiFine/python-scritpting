# OS Module in Python - Complete Guide

The `os` module in Python provides functions for interacting with the operating system. It comes under Python's standard utility modules and provides a portable way of using operating system-dependent functionality.

##  QUICK LINK 
- https://www.geeksforgeeks.org/python/os-module-python-examples/

## 📚 Table of Contents
- [Overview](#overview)
- [Key Functions](#key-functions)
- [File Examples](#file-examples)
- [Common Use Cases](#common-use-cases)

## 🎯 Overview

The OS module enables you to:
- Navigate and manipulate the file system
- Get system information
- Execute system commands
- Handle file permissions
- Manage environment variables

**Import:** `import os`

---

## 🔑 Key Functions

### Directory Navigation

#### `os.getcwd()` - Get Current Working Directory
Returns the absolute path of the current working directory.

```python
import os
cwd = os.getcwd()
print(f"Current Directory: {cwd}")
# Output: C:\Users\MaxwellAdomako\amalitech\lprojects\python-scripting
```

#### `os.chdir(path)` - Change Directory
Changes the current working directory to the specified path.

```python
os.chdir('../')  # Move to parent directory
print(os.getcwd())
```

**📁 Example File:** `os_change_cwd.py`, `os_chng_path.py`

---

### Creating Directories

#### `os.mkdir(path, mode=0o777)` - Create Single Directory
Creates a single directory. Raises error if directory already exists or parent doesn't exist.

```python
import os

# Create directory in current location
new_dir = os.path.join(os.getcwd(), 'test_directory')
os.mkdir(new_dir)
print(f"Directory created: {new_dir}")

# Create with specific permissions
os.mkdir("new_dir_by_mkdir", mode=0o666)
```

**📁 Example Files:** `os_change_cwd.py`, `os_create_dirs.py`

#### `os.makedirs(path, mode=0o777, exist_ok=False)` - Create Nested Directories
Creates intermediate directories as needed (like `mkdir -p` in Unix).

```python
import os

# Create nested directory structure
path = os.path.join(os.getcwd(), "parent/child/grandchild")
os.makedirs(path, exist_ok=True)  # Won't raise error if exists
print(f"Nested directories created: {path}")
```

**Parameters:**
- `path`: Directory path to create
- `mode`: Permission bits (default 0o777)
- `exist_ok`: If True, don't raise error if directory exists

**📁 Example File:** `os_mkdirs_func.py`

---

### Listing Files and Directories

#### `os.listdir(path='.')` - List Directory Contents
Returns a list containing names of entries (files and directories) in the given path.

```python
import os

# List current directory
files = os.listdir('.')
print(f"Files in current directory: {files}")

# List specific directory
path = "/path/to/directory"
dir_list = os.listdir(path)
print(f"Contents: {dir_list}")
# Output: ['file1.txt', 'folder1', 'script.py']
```

**Note:** Returns names only, not full paths. Use `os.path.join()` to create full paths.

**📁 Example File:** `os_listing_files.py`

---

### Path Operations

#### `os.path.join(path, *paths)` - Join Path Components
Intelligently joins path components using the correct separator for your OS.

```python
import os

# Cross-platform path joining
parent = os.getcwd()
directory = "new_folder"
path = os.path.join(parent, directory)
# Windows: C:\Users\...\new_folder
# Linux: /home/.../new_folder
```

**Benefits:**
- Handles different OS path separators (\ vs /)
- Prevents double slashes
- Creates clean, valid paths

**📁 Used in:** All example files

---

### Removing Files and Directories

#### `os.remove(path)` - Delete a File
Removes (deletes) the file at the specified path.

```python
import os

# Remove a file
file = 'file1.txt'
location = os.getcwd()
path = os.path.join(location, file)
os.remove(path)
print(f"File '{file}' removed successfully")
```

**Important:**
- Only works on files, not directories
- Raises `OSError` if path is a directory
- Raises `FileNotFoundError` if file doesn't exist

**📁 Example File:** `os_remove_files.py`

#### `os.rmdir(path)` - Remove Empty Directory
Removes an empty directory.

```python
import os

# Remove empty directory
directory = "c"
parent = os.getcwd()
path = os.path.join(parent, directory)
os.rmdir(path)
print(f"Directory '{directory}' removed successfully")
```

**Important:**
- Only works on empty directories
- Raises `OSError` if directory is not empty
- Use `shutil.rmtree()` for non-empty directories

**📁 Example File:** `os_remove_dir.py`

---

## 📂 File Examples in This Directory

### 1. **os_change_cwd.py**
Demonstrates creating a directory and navigating the file system.

```python
import os

# Get current directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Create new directory
new_dir = os.path.join(cwd, 'test_directory')
os.mkdir(new_dir)
print("Directory 'test_directory' created successfully.")
```

**What it teaches:** `os.getcwd()`, `os.mkdir()`, `os.path.join()`

---

### 2. **os_create_dirs.py**
Shows different ways to create directories with various options.

```python
import os

# Create single directory
directory = "new_dir_by_mkdir"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print(f"Directory '{directory}' created at: {path}")

# Create with custom permissions
new_dirs = "GeekBymkdir"
mode = 0o666
path = os.path.join(parent_dir, new_dirs)
os.mkdir(path, mode)
print(f"Directory '{new_dirs}' created with mode {mode}")
```

**What it teaches:** `os.mkdir()` with permissions, directory creation patterns

---

### 3. **os_mkdirs_func.py**
Demonstrates creating nested directory structures.

```python
import os

# Create nested directories
directory = "Nikhil"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print(f"Directory '{directory}' created")

# Create with permissions
directory = "c"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path, mode)
print(f"Directory '{directory}' created")
```

**What it teaches:** `os.makedirs()` for nested structures

---

### 4. **os_listing_files.py**
Lists all files and directories in a specified path.

```python
import os

path = "/mnt/c/Users/MaxwellAdomako/amalitech/lprojects/python-scripting/"
dir_list = os.listdir(path)
print(f"Files and directories in '{path}':")
print("====================================")
print(f"Files and directories: {dir_list}")
```

**What it teaches:** `os.listdir()` for directory exploration

---

### 5. **os_remove_files.py**
Safely removes files from the file system.

```python
import os

# Remove a file
file = 'file1.txt'
location = os.getcwd()
path = os.path.join(location, file)
os.remove(path)
print(f"File '{file}' removed from location: {location}")
os.listdir(location)  # Verify removal
```

**What it teaches:** `os.remove()` for file deletion, error handling

---

### 6. **os_remove_dir.py**
Removes empty directories from the file system.

```python
import os

directory = os.getcwd() + "/c/"
parent = os.getcwd()
path = os.path.join(parent, directory)
print(f"Removing Directory '{directory}':")
os.rmdir(path)
print(f"Directory '{directory}' removed successfully")
print(os.listdir(parent))  # Show remaining items
```

**What it teaches:** `os.rmdir()` for directory removal

---

### 7. **os_chng_path.py**
Navigates between directories by changing the current working directory.

```python
import os

def current_path():
    print("Current Directory Path:", os.getcwd())

current_path()
print("Changing Directory to Root Path...")
os.chdir('../')  # Move to parent directory
print('Path Changed Successfully.')
print("Current Root Directory Path:", os.getcwd())
```

**What it teaches:** `os.chdir()` for navigation, moving up directory tree

---

## 💡 Common Use Cases

### 1. Creating Project Structure
```python
import os

def create_project_structure(project_name):
    """Create a standard project directory structure"""
    base = os.path.join(os.getcwd(), project_name)
    
    # Create nested directories
    os.makedirs(os.path.join(base, "src"), exist_ok=True)
    os.makedirs(os.path.join(base, "tests"), exist_ok=True)
    os.makedirs(os.path.join(base, "docs"), exist_ok=True)
    
    print(f"Project '{project_name}' structure created!")

create_project_structure("my_app")
```

### 2. Finding Files with Specific Extension
```python
import os

def find_files_by_extension(directory, extension):
    """Find all files with specific extension"""
    matching_files = []
    for item in os.listdir(directory):
        if item.endswith(extension):
            matching_files.append(item)
    return matching_files

# Find all Python files
python_files = find_files_by_extension(".", ".py")
print(f"Python files: {python_files}")
```

### 3. Safe Directory Cleanup
```python
import os

def cleanup_empty_dirs(parent):
    """Remove all empty directories in parent"""
    for item in os.listdir(parent):
        path = os.path.join(parent, item)
        if os.path.isdir(path):
            try:
                os.rmdir(path)
                print(f"Removed empty directory: {item}")
            except OSError:
                print(f"Directory not empty: {item}")
```

---

## ⚠️ Important Notes

1. **Path Separators:** Always use `os.path.join()` for cross-platform compatibility
2. **Permissions:** Default mode is 0o777, but actual permissions depend on umask
3. **Error Handling:** Always wrap file operations in try-except blocks
4. **Existence Check:** Use `os.path.exists()` before operations
5. **Current Directory:** File operations use current directory if relative paths given

## 🔗 Related Modules

- **`pathlib`** - Modern, object-oriented path handling (recommended for new projects)
- **`shutil`** - High-level file operations (copy, move, delete trees)
- **`glob`** - Unix-style pathname pattern expansion

---

## 📖 Additional Resources

- [Official Python os documentation](https://docs.python.org/3/library/os.html)
- [os.path documentation](https://docs.python.org/3/library/os.path.html)
