from scapy.all import *
import time
import sys
import os


def arp_scan(interface , ip_addr):
    #Turn off verbose
    conf.verb=0
    #send packets to every Host on the Network , aka , the Broadcast ID
    broadcast = "ff:ff:ff:ff:ff:ff"
    ether_layer= Ether(dst=broadcast)
    arp_layer = ARP(pdst = ip_addr)
    packet = ether_layer/arp_layer
    recv , unrecv= srp(packet , iface=interface , timeout = 2 , inter = 0.1)
    
    #Print sent and received packet info.
    #Here the Sent Packet Data has been ignored
    for snd , rcv in recv:
        respip = rcv[ARP].psrc
        respmac = rcv[Ether].src
        print(f"[+] {respip} ---> {respmac}")
    

try :
    inter = sys.argv[1]
    ip_addr = sys.argv[2]

except IndexError :
    print ("[+] Empty Parameter List")
    name = os.path.basename(__file__)
    print (f"[+] Usage : python3 {name} <interface> <IP Address/Range>")
    sys.exit(0)

print(f"[+] Interface : {inter}")
print(f"[+] IP Address : {ip_addr}")
currtime = time.time()
print("[+] Starting Scan On:" , time.ctime(currtime))
print("")
arp_scan(inter , ip_addr)
print("")
print("[+] Scan Completed In :", time.time()-currtime , "seconds")
