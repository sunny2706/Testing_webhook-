#!/usr/bin/env python3
#Objective 4: Port Scan Using NMAP 
import time
import csv
import subprocess as sp

IP_address_scan = "nmap -sP 10.201.23.110/24"
scanning_port = sp.getoutput(IP_address_scan)
print (scanning_port)
with open ('target_file_1','w') as file_1:
    file_1.write(scanning_port)
