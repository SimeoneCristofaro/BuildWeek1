import http.client

http_methods = ('GET', 'POST', 'DELETE', 'PATCH', 'OPTIONS', 'PUT', 'HEAD', 'CONNECT', 'TRACE')

host = input('Inserire URL completa del sistema target (default:192.168.100.110/phpMyAdmin/index.php):')

if host == "":
    host = "192.168.100.110/phpMyAdmin/index.php"

url_path = ""
url_domain = host.split('/')[0]

for i in range(1, len(host.split('/'))):
    url_path = url_path + "/" + host.split('/')[i]

port = input('Inserire la porta del sistema target (default:80): ')

if(port == ""):
    port = 80

for i in range(len(http_methods)):
    try:
        connection = http.client.HTTPConnection(url_domain,port)
        connection.request(http_methods[i], url_path)
        response = connection.getresponse()
        print(http_methods[i] + " : ", response.status, " - ", response.reason)
        connection.close()
    except ConnectionRefusedError:
        print("Connessione fallita")

