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
        "edition": platform.win32_edition() if platform.system() == "Windows" else "N/A",  # Windows edition
        "system_alias": platform.system_alias(
            platform.system(),
            platform.release(),
            platform.version()
        )  # Tuple with (system, release, version)
    }
    return info


if __name__ == "__main__":
    print("=== Platform Information ===")
    platform_info = get_platform_info()
    for key, value in platform_info.items():
        print(f"{key.capitalize()}: {value.capitalize()}")
    
# Example output on Linux: ['ubuntu', 'debian']
# Example output on Windows: Shows Windows platform info