#!/usr/bin/env python3
"""
Installation script for College Assistant Chatbot dependencies
Run this script to install all required packages
"""

import subprocess
import sys

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

def main():
    """Install all required packages"""
    packages = [
        "Flask",
        "transformers", 
        "torch",
        "pandas",
        "rapidfuzz",
        "numpy"
    ]
    
    print("🚀 Starting installation of College Assistant Chatbot dependencies...")
    print("=" * 60)
    
    failed_packages = []
    
    for package in packages:
        print(f"\n📦 Installing {package}...")
        if not install_package(package):
            failed_packages.append(package)
    
    print("\n" + "=" * 60)
    print("📋 Installation Summary:")
    
    if failed_packages:
        print(f"❌ Failed packages: {', '.join(failed_packages)}")
        print("\n🔧 Try installing failed packages manually:")
        for package in failed_packages:
            print(f"   pip install {package}")
    else:
        print("✅ All packages installed successfully!")
        print("\n🎉 You can now run the chatbot with:")
        print("   python app.py")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
