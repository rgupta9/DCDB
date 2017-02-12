#! /usr/bin/python

import os, sys, getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException

platform = 'arista_eos'
username = raw_input('Username? ')
passy = getpass.getpass()

commandfile = raw_input('command file? ')
f = open(commandfile, 'r')
show_commands = f.read()
show_commands = show_commands.strip()
show_commands = show_commands.split('\n')

targetfile = raw_input('target file? ')
x = open(targetfile, 'r')
hostlist =  x.read()
hostlist = hostlist.strip()
hostlist = hostlist.split()

outfile = raw_input('output filename? ')

for host in hostlist:
	try:
		device = ConnectHandler(device_type=platform, ip=host, username=username, password=passy)
	except Exception:
		continue
	try:
		device.find_prompt()
	except Exception:
		continue
	sys.stdout=open(outfile,"a")
	for item in show_commands:
		try:
			output = device.send_command(item)
		except:
			continue
		output = output.split('\n')
		for line in output:
			print host + " " + "|" + item + "|" + " " + line
	device.disconnect()
	sys.stdout.close()
