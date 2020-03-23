tshark -r q3.pcap -Y "tcp and ip.src==10.1.60.67 or ip.dst==10.1.60.67" | wc -l
