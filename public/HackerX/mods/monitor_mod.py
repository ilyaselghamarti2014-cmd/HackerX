import subprocess
import sys

def start_monitor_mode():
    subprocess.Popen(
        [sys.executable, "sudo", "airmon-ng", "start", "wlan0"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        
    )
    print("Monitor mode started.")