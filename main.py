import subprocess
import sys

def run_command(command):
    """Run a command in the shell."""
    try:
        subprocess.check_call(command, shell=True)
        print("Successfully ran: {}".format(command))
    except subprocess.CalledProcessError as e:
        print("Failed to run: {}\nError: {}".format(command, e))
        sys.exit(1)

def install_stress():
    """Install the stress package."""
    print("Installing stress package...")
    run_command('sudo apt-get update --fix-missing')
    run_command('sudo apt-get install -y stress')

def install_s_tui():
    # Install s-tui
    print("Installing s-tui...")
    run_command('sudo apt install s-tui')

def run_s_tui():
    try:
        # Run s-tui
        print("Running s-tui...")
        subprocess.run(['sudo', 's-tui'], check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to run s-tui: {}".format(e))

if __name__ == "__main__":
    install_s_tui()
    install_stress()
    run_s_tui()

