from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = "Other"

        print("="*60)
        print(f"📅 Time          : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🌐 Source IP     : {src_ip}")
        print(f"🎯 Destination IP: {dst_ip}")
        print(f"📦 Protocol      : {protocol}")
        print(f"🧩 Packet Length : {len(packet)} bytes")

        if packet.haslayer(Raw):
            print(f"📝 Payload (raw) : {packet[Raw].load[:50]}")
        print("="*60)

print("📡 Sniffing started... Press Ctrl+C to stop.\n")
sniff(filter="ip", prn=process_packet, store=False)
