# Import required modules into the program
import socket
import sys
from datetime import datetime

# Insert header for display
banner = ("Door Knocker \n By R. Lee")
print(banner)

# Prompt for user input
#target = input("Please enter IP to Scan:") Hard input of IP address
hostname = input("Please enter address to scan: ")  # Uses gethostname from socket 
target = socket.gethostbyname(hostname)             # module to pull IPv4 from friendly name

time1 = (datetime.now())

# Add banner info
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning began at: " + str(time1))
print("-" * 50)

# Add exception / error handling
try:
    #Scan ports 1 - 500
    for port in range(1,500):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Error indicator
        result = sock.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("n Exiting Program per User Command!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname unable to be Resolved, Exiting!!")
    sys.exit()
except socket.error:
    print("Server Unresponsive!!")
    sys.exit()

# check current time to calculate run time
time2 = (datetime.now())

total = (time2 - time1)

# Calculate run time
print("-" * 50)
print("Scanned Target: " + target)
print("Total Run time: " + str(total))
print("-" * 50)
