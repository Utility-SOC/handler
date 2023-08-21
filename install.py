import os
import subprocess

def create_venv():
    """Creates a virtual environment in the current directory."""
    print("Creating virtual environment...")
    subprocess.check_call(['python', '-m', 'venv', 'venv'])
    print("Virtual environment created!")

def install_dependencies():
    """Installs the required dependencies in the virtual environment."""
    print("Installing dependencies...")
    
    pip_cmd = os.path.join('venv', 'Scripts', 'pip') if os.name == 'nt' else os.path.join('venv', 'bin', 'pip')
    
    subprocess.check_call([pip_cmd, 'install', 'tqdm'])
    print("Dependencies installed!")

if __name__ == "__main__":
    create_venv()
    install_dependencies()
