import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# invio del messaggio al server
primoNumero = float(input("inserisci il primo numero: "))
operazione = input("inserisci l'operazione (simbolo): ")
secondoNumero = float(input("inserisci il secondo numero: "))
messaggio = {"primoNumero": primoNumero,
            "operazione": operazione,
            "secondoNumero": secondoNumero}
messaggio = json.dumps(messaggio)
sock.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))


# ricezione della risposta dal server
data, addr = sock.recvfrom(BUFFER_SIZE)
print(f"Messaggio ricevuto dal server {addr}: {data.decode()}")

# chiusura del socket
sock.close()