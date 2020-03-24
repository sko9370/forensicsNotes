tshark -r q2.pcap -Y 'tcp and ip.src==10.1.60.68 and http.request.method==GET or http.request.method==POST' | wc -l
