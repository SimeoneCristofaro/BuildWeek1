import socket
import csv

target = input('Enter the IP address to scan (default: 192.168.100.110): ')
portrange = input('Enter the port range to scan (default: 1-1024): ')

if target == "":
    target = "192.168.100.110"

if portrange == "":
    portrange = "1-1024"

# Inizializzo l'array vuoto.
tcp_port_aray = []

# csvfile è un puntatore al file
# tcp.csv che contine una lista in cui ogni riga è così formata
# 'TCP', numero_porta, 'nome_servizio'
with open("tcp.csv") as csvfile:
    # csv.QUOTE_NONNUMERIC serve per convertire in float i caratteri che non sono inclusi tra le '. 
    # La funzione non lo fa in automatico
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
    # Ogni riga è una lista con indice che va da 0 a 3
    for row in reader: 
        # aggiungo la lista all'array.
        # tcp_port_array diventa una matrice
        tcp_port_aray.append(row)
        
    # libera la risorsa
    csvfile.close()

# estraggo i due numeri dalla stringa inserita utilizzando come separatore
# il carattere '-'
lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print('Scansiono host ', target, ' dalla porta ', lowport, ' alla porta ', highport)


for port in range(lowport, highport):
    # cerco di stabilire la connessione sulla porta port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))

    # se  s.connect_ex((target, port)) restituisce 0 la connessione è avvenuta
    if(status == 0):
        # cerco la porta nella matrice per estrarre
        # il nome_servizio
        for i in range(len(tcp_port_aray)):
            if tcp_port_aray[i][1] == port:
                print('>>> Port ', port, tcp_port_aray[i][2], ' - OPEN')
                break
    s.close()
