from scapy.all import sniff
from scapy.layers.inet import IP

def process_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto

        print(f"Source: {src}")
        print(f"Destination: {dst}")
        print(f"Protocol: {proto}")
        print("-" * 40)

print("Packet Sniffer V2 Started...")
print("Press Ctrl+C to stop.\n")

sniff(prn=process_packet, store=False)
