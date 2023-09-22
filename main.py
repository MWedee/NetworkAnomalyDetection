from scapy.all import *


def packet_callback(packet):
    print(packet.summary())


# Capture packets on a specific wireless network interface (e.g., 'Wi-Fi' on Windows)
sniff(iface='Ethernet 4', prn=packet_callback)
