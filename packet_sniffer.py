from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

print("================================")
print("   Packet Sniffer Version 1")
print("================================")
print("Capturing packets...")
print("Press CTRL+C to stop.\n")

sniff(prn=process_packet, store=False)
