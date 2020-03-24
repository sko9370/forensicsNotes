tcpdump -A -r q4.pcap 'tcp' | grep -o "<title.*<" | sort -u | cut -c 8- | cut -d'<' -f1
