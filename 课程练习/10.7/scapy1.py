from scapy.all import *
while True:
    eth = Ether()
    eth.dst = RandMAC()
    eth.src = RandMAC()
    eth.show()
    sendp(eth)