tshark -r q6.pcap -Q -Y "ip and not icmp" -z endpoints,ip | head -n 5
