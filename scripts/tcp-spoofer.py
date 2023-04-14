#!/usr/bin/env python3

from scapy.all import *

# Adding IPv6 route
#conf.route6.add(dst="64:ff9b::/96", gw="2001:db8:6::1")

# This scritp sniffes the communication channel on Interface ens34, looks for TCP packet.
# Then, it spoofes the source IP address of the found packet and sends identical packet to the same recipient.

# function to process the packet
def process_packet(packet):
    # check if the packet is a TCP packet
    elif packet.haslayer(TCP) and packet[IPv6].src == "2001:db8:ce:11b:0:cb00:7108:1b":
        # extract the source port
        src_port = packet[TCP].sport
        print("[+] Found TCP packet with source port: ", src_port)
        # craft a new UDP packet
        ip = IPv6(dst="64:ff9b::c000:202",src="2001:db8:ce:11b:0:cb00:7108:1b")
        eth= Ether(src="00:0c:29:b3:80:01")
        tcp = TCP(sport=src_port, dport=80)
        data = "From Ameen with Love!"
        packet = eth/ip/tcp/data
        sendp(packet, iface='ens34',return_packets=True)

# start sniffing on ens34
sniff(iface='ens34', filter="tcp", prn=process_packet)
