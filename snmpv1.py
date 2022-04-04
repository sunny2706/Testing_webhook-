#!/usr/bin/env python3 
#Objective 2
import os

os.system("snmpget -v1 -c public 198.51.100.3 .1.3.6.1.2.1.1.4.0")
os.system("snmpget -v1 -c public 198.51.100.3 .1.3.6.1.2.1.1.5.0")
os.system("snmpget -v1 -c public 198.51.100.3 .1.3.6.1.2.1.1.6.0")
os.system("snmpget -v1 -c public 198.51.100.3 .1.3.6.1.2.1.2.1.0")
os.system("snmpget -v1 -c public 198.51.100.3 .1.3.6.1.2.1.1.3.0")

