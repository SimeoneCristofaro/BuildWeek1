# importo la libreria http.client
# che contiene i metodi per perfezionare una connessione http
import http.client

# Tupla che contiene i metodi da interrogare
http_methods = ('GET', 'POST', 'DELETE', 'PATCH', 'OPTIONS', 'PUT', 'HEAD', 'CONNECT', 'TRACE')

host = input('Inserire URL completa del sistema target (default:192.168.100.110/phpMyAdmin/index.php):')

if host == "":
    host = "192.168.100.110/phpMyAdmin/index.php"

host = host.split('/')
# host[0] = "192.168.100.110"
# host[1] = "phpMyAdmin"
# host[2] = "index.php"

url_domain = host[0]

url_path = ""
for i in range(1, len(host)):
    url_path = url_path + "/" + host[i]
    # 1 - url_path = "/phpMyAdmin"
    # 2 - url_path = "/phpMyAdmin/index.php"


port = input('Inserire la porta del sistema target (default:80): ')

if(port == ""):
    port = 80

for i in range(len(http_methods)):
    # provo a inviare la richiesta al web Server
    try:
        # connessione al dominio sulla porta
        connection = http.client.HTTPConnection(url_domain,port)
        # richiedo la path
        connection.request(http_methods[i], url_path)
        # estraggo la risposta
        response = connection.getresponse()
        # scrivo a schermo il codice di stato e il suo significato
        print(http_methods[i] + " : ", response.status, " - ", response.reason)
        # chiudo la connessione
        connection.close()
    except ConnectionRefusedError:
        # connessione non stabilita. Gestisco l'eccezione scrivendo a schermo
        print("Connessione fallita")

