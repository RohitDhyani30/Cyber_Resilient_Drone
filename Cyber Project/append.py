from scapy.all import *


packets = rdpcap('/home/kali/Desktop/WIRESHARK/Pocox51.pcapng')


with open('hash_value.txt', 'r') as f:
    hash_data = f.read().strip()


packet = (
    RadioTap() /
    Dot11(type=2, subtype=0, addr1="ff:ff:ff:ff:ff:ff", addr2="00:11:22:33:44:55", addr3="00:11:22:33:44:55") /
    LLC() /
    SNAP() /
    Raw(load=hash_data)
)

packets.append(packet)


wrpcap("merged_packet.pcapng", packets)

