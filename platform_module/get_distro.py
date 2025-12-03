import platform


def get_like_distro():
    """
    Get Linux distribution information.
    Only works on Linux systems with /etc/os-release file.
    
    Returns:
        list: Distribution IDs (e.g., ['ubuntu', 'debian'])
        None: If not running on Linux or file not found
    """
    try:
        info = platform.freedesktop_os_release()
        ids = [info["ID"]]
        if "ID_LIKE" in info:
            # ids are space separated and ordered by precedence
            ids.extend(info["ID_LIKE"].split())
        return ids
    except OSError as e:
        # This function only works on Linux systems
        print(f"Error: {e}")
        print(f"Current OS: {platform.system()}")
        print("Note: freedesktop_os_release() only works on Linux systems with /etc/os-release")
        return None


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
    }
    return info


if __name__ == "__main__":
    print("=== Platform Information ===")
    platform_info = get_platform_info()
    for key, value in platform_info.items():
        print(f"{key.capitalize()}: {value.capitalize()}")
    
    print("\n=== Linux Distribution Info ===")
    distro = get_like_distro()
    if distro:
        print(f"Distribution IDs: {distro}")
    
# Example output on Linux: ['ubuntu', 'debian']
# Example output on Windows: Shows Windows platform info