import threading
from scapy.all import *

# our packet callback
def packet_callback(packet):
    print packet[TCP].payload

# fire up our sniffer
sniff(filter="tcp port 3333",prn=packet_callback,store=0)
