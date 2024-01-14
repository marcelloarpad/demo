from scapy.all import *
eth = Ether()
eth.dst = "ff:ff:ff:ff:ff:ff"
dot = Dot1Q()
dot1 = Dot1Q()
arp = ARP()
arp.pdst = "11.11.11.11"
dot.vlan = 1
dot1.vlan = 2
packet = eth/dot/dot1/arp
packet.show()
sendp(packet)