from scapy.all import *

eth = Ether()
eth.dst="01:00:5e:00:00:09"
eth.src="00:e0:fc:36:31:e0"
ip = IP()#IP
ip.src ="192.168.3.2"
ip.dst = "224.0.0.9"
udp = UDP()
udp.sport = 520
udp.dport = 520
rip = RIP()
rip.cmd = 2
rip.version = 2
ripentry1 = RIPEntry()
ripentry1.addr = "192.168.1.0"
ripentry1.mask = "255.255.255.255"

ripentry2 = RIPEntry()
ripentry2.addr = "192.168.2.0"
ripentry2.mask = "255.255.255.255"


ripentry3 = RIPEntry()
ripentry3.addr = "192.168.2.0"
ripentry3.mask = "255.255.255.255"
ripentry3.metric = 16

packet =eth/ip/rip/ripentry1/ripentry2/ripentry3
packet.show()
sendp(packet)