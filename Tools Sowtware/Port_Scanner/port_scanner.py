import socket
import csv

target = input('Enter the IP address to scan (default: 192.168.100.110): ')
portrange = input('Enter the port range to scan (default: 1-1024): ')

if target == "":
    target = "192.168.100.110"

if portrange == "":
    portrange = "1-1024"

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

tcp_port_aray = []
with open("tcp.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        tcp_port_aray.append(row)
    csvfile.close()

print('Scanning host ', target, ' from port ', lowport, ' to port ', highport)

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        for i in range(len(tcp_port_aray)):
            if tcp_port_aray[i][1] == port:
                print('>>> Port ', port, tcp_port_aray[i][2], ' - OPEN')
                break
    #selse:
        #print('Port ', port, ' - CLOSED')
    s.close()
