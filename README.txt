# DCDB.py
SHOW COMMANDS ONLY

Data Center Text Based Data Based DB
Three files are required. A target file, a command file, and an output file.
The traget file is a list of network devices. One device per line.
The command file is a list of SHOW commands you want to issue to each one of the the devices in the target file. One command per line.
The output file is a file that you want to output the text DB to. This is file does not need to exist prior to running the script.k


DCDB logs in via SSH and issues the commands placed in the command file. Additionally, DCDB tags the output flowing to output file with the target name as well as the command issued. I suggest placing every device in your data center in the target file.


Suggested Command File:
show version
show running-config
show running-config section bgp
show interface status
show vlan
show ip int brief
show running-config section ospf
show lldp neighbor
Any other command that is relevant to your specific data center


Find all unused ports on all tors
Verify the consistent mlag configs on all devices
Display all VLANS defined on all TORS and Spines.
Display serial number of all devices
Display all unique version of code running on the DC and then identify devices that are not running the standard
Query a line of standard config across all devices and identify any anomolies

