import sys
import subprocess

# List of required libraries
libraries = [
    ("python-barcode", "barcode"),
    ("jinja2", "jinja2"),
    ("re", "re"),
    ("Pillow", "pillow")
]

# Check if each library is already installed
for lib, mod_name in libraries:
    try:
        __import__(mod_name)
        print(f"{lib} is already installed.")
    except ImportError:
        print(f"{lib} is not installed. Installing...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(f"{lib} installed successfully.")
        except Exception as e:
            print(f"Error occurred while installing {lib}: {str(e)}")
