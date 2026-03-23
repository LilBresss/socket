# client
import socket
import json

HOST = "127.0.0.1"  # Indirizzo del server
PORT = 65432        # Porta usata dal server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))
    primoNumero = float(input("inserisci il primo numero: "))
    operazione = input("inserisci l'operazione (simbolo): ")
    secondoNumero = float(input("inserisci il secondo numero: "))
    messaggio = {"primoNumero": primoNumero,
                "operazione": operazione,
                "secondoNumero": secondoNumero}
    messaggio = json.dumps(messaggio)
    sock_service.sendall(messaggio.encode())
    
    
    data = sock_service.recv(1024)
    # a questo punto la socket è stata chiusa automaticamente
    print("\nReceived\n", data.decode())
