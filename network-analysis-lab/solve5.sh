tshark -r q5.pcap -Q -Y "tcp and not icmp" -z endpoints,tcp | head -n 9
