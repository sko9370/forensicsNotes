tshark -r q7.pcap -Y "smb.create.action==2" -T fields -e ip.src -e ip.dst -e smb.file 2>/dev/null
