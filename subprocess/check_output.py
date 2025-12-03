import subprocess
import platform

try:
    # Check Python version - works on all platforms
    ans = subprocess.check_output(["python", "--version"], text=True)
    print(f"check_output: \nresult: {ans}")
    
    # Get current working directory - platform-specific
    if platform.system() == "Windows":
        # On Windows, use 'cd' or PowerShell command
        paths = subprocess.check_output(["powershell", "-Command", "Get-Location"], text=True)
    else:
        # On Unix/Linux/macOS, use 'pwd'
        paths = subprocess.check_output(["pwd"], text=True)
    
    print(f"Current Working Directory: {paths.strip()}")

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
except FileNotFoundError as e:
    print(f"Command not found: {e}")