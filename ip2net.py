#################################################################################
#	ip2net.py -- Looks up network information given a file containing IPs   #
#       Heavily commented for educational purposes                              #
#       Requires Cymruwhois pacakage: https://pypi.python.org/pypi/cymruwhois   #
#	Copyrighted:  Primal Security Podcast - www.primalsecurity.net         	#
#									       	#
#    	This program is free software: you can redistribute it and/or modify	#
#    	it under the terms of the GNU General Public License as published by	#
#    	the Free Software Foundation, either version 3 of the License, or	#
#    	(at your option) any later version.					#
#										#
#    	This program is distributed in the hope that it will be useful,		#
#    	but WITHOUT ANY WARRANTY; without even the implied warranty of		#
#    	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the		#
#    	GNU General Public License for more details.				#
#										#
#    	You should have received a copy of the GNU General Public License	#
#    	along with this program.  If not, see <http://www.gnu.org/licenses/>.	#
#################################################################################
#!/usr/bin/env python
import sys, os, optparse
from cymruwhois import Client
import time
 
def look(iplist):
    time.sleep(2) # delays for 2 seconds
    c=Client() # creates an instance of the Client class
    try:
#       print 'here before != None'
#       print iplist
#       if ips != None:
        if iplist != None: 
            print 'here after !=None'
            print iplist
            time.sleep(2)
 #          r = c.lookupmany_dict('8.8.8.8')
            r = c.lookupmany_dict(iplist) # leverages the lookupmany_dict() function to pass in a list of IPs
            for ip in iplist: # Iterates over the ips in the list to use a key value in the dictionary from lookupman_dict()
                time.sleep(2) # delays for 2 seconds
                print " ip here " + ip
                net = r[ip].prefix; owner = r[ip].owner; cc = r[ip].cc # gets the networking information from the dictionary
 #              print net
                line = '%-20s # - %15s (%s) - %s' % (net,ip,cc,owner) # formats the line to print cleanly
                print line
    except:pass
 
def checkFile(ips): # Checks to ensure the file can be read
        if not os.path.isfile(ips):
                print '[-] ' + ips + ' does not exist.'
                sys.exit(0)
        if not os.access(ips, os.R_OK):
                print '[-] ' + ips + ' access denied.'
                sys.exit(0)
        print '[+] Querying from:  ' +ips
 
def main():
    parser = optparse.OptionParser('%prog '+'-r <file_with IPs> || -i <IP>')
    parser.add_option('-r', dest='ips', type='string', help='specify target file with IPs')
    parser.add_option('-i', dest='ip', type='string', help='specify a target IP address')
    (options, args) = parser.parse_args()
    ip = options.ip      # Assigns a -i <IP> to variable 'ip'
    global ips; ips = options.ips # Assigns a -r <fileName> to variable 'ips'
    if (ips == None) and (ip == None): # If proper arguments aren't given print the script usage
        print parser.usage
        sys.exit(0)
    if ips != None:    # Execute if ips has a value
#       print "ips is not empty here " + ips
        checkFile(ips)    # Execute the function to check if the file can be read
        iplist = []    # create the ipslist list object
        for line in open(ips, 'r'): # Parse File to create a list
#           iplist.append(line.strip("'" + "\r\n" + "'"))
            iplist.append(line.strip("\r\n")) # Appends that line in the file to list and removes the new line char
#           iplist.append(line.strip('n'))
            print "line not empty " + line
            print iplist
            look(iplist)    # pass the iplist list object to the look() function
    elif ip != None:
        try:
            print "here ip not empty " + ip
            c=Client()
            r = c.lookup(ip)
            net = r.prefix; owner = r.owner; cc = r.cc
            print net
            line = '%-20s # - %15s (%s) - %s' % (net,ip,cc,owner)
            print line
        except:pass           

#    else:    # Executes lookup() function for a single IP stored in variable 'ip'
#        try:
#            print "here ip not empty " + ip
#            c=Client()
#            r = c.lookup(ip)
#            net = r.prefix; owner = r.owner; cc = r.cc
#            line = '%-20s # - %15s (%s) - %s' % (net,ip,cc,owner)
#            print line
#        except:pass
 
if __name__ == "__main__":
      main()
