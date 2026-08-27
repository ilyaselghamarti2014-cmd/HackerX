
import subprocess
import sys
import time


def install_packages():

    process = subprocess.Popen(
        [sys.executable, "-m", "pip", "install", "scapy"],
        [sys.executable, "-m", "sudo", "apt", "install", "aircrack-ng"],
        [sys.executable, "-m", "pip", "install", "scapy_http"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    frames = [
        "▱▱▱▱▱▱▱▱▱▱",
        "▰▱▱▱▱▱▱▱▱▱",
        "▰▰▱▱▱▱▱▱▱▱",
        "▰▰▰▱▱▱▱▱▱",
        "▰▰▰▰▱▱▱▱▱▱",
        "▰▰▰▰▰▱▱▱▱▱",
        "▰▰▰▰▰▰▱▱▱▱",
        "▰▰▰▰▰▰▰▱▱▱",
        "▰▰▰▰▰▰▰▰▱▱",
        "▰▰▰▰▰▰▰▰▰▱",
        "▰▰▰▰▰▰▰▰▰▰"
    ]

    i = 0

    while process.poll() is None:
        print(
            f"\rDownloading / Installing Scapy [{frames[i % len(frames)]}]",
            end="",
            flush=True
        )

        i += 1
        time.sleep(0.12)

    if process.returncode == 0:
        print("\r[+] Scapy installed successfully!              ")
    else:
        print("\r[-] Failed to install Scapy.                    ")