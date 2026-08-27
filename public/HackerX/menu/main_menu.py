from animation import *
from colorama import *
from attacks.packet_sniffer import *
from mods.monitor_mod import *
from mods.managed_mod import *
from attacks.deauth_attack import *
import subprocess

def main_menu() :
    start_tool_animation3("================================================================================")
    start_tool_animation3("                         Welcome to HackX Tool")
    start_tool_animation3("================================================================================")
    while True:
        print(Style.BRIGHT + Fore.GREEN + "1. Start monitor mode" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + "2. Start managed mode" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.BLUE + "3. Start deauth attack" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.MAGENTA + "4. WPS attack" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.YELLOW + "5. Start DOS attack" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.CYAN + "6. start ARP spoofing attack" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.WHITE + "7. Start packet sniffing" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + "8. Exit" + Style.RESET_ALL)
        choice = input("Enter your choice: ")
        if choice == "1":
            start_monitor_mode()
        elif choice == "2":
            start_managed_mode()
        elif choice == "3":
            start_deauth_attack()
        elif choice==4 :
            pass
        elif choice==5 :
            pass
        elif choice==6 :
            subprocess.Popen(
                ["cmd.exe", "/k", "python  attacks/arp_spoofer.py"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        elif choice==7 :
            subprocess.Popen(
                ["cmd.exe", "/k", "python  attacks/packet_sniffer.py"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        elif choice==8 :
            print("Bye")


        