import subprocess
import sys

def start_managed_mode():
    subprocess.Popen(
        [sys.executable, "sudo", "airmon-ng", "stop", "wlan0mon"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        
    )
    print("Managed mode started.")