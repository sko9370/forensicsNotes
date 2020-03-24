tcpdump -r q1.pcap 'tcp[tcpflags] & (tcp-syn) != 0 and src 10.1.60.66' | wc -l
