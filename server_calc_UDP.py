import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("Server in attesa di messaggi...")

while True:
    # ricezione dei dati dal client
    data, addr = sock.recvfrom(BUFFER_SIZE)
    if not data:
        break
    data = data.decode()
    data = json.loads(data)
    primoNumero = data["primoNumero"]
    operazione = data["operazione"]
    secondoNumero = data["secondoNumero"]

    if (operazione == "+"):
        risultato = primoNumero + secondoNumero
    elif (operazione == "-"):
        risultato = primoNumero - secondoNumero
    elif (operazione == "*"):
        risultato = primoNumero * secondoNumero
    elif (operazione == "/"):
        risultato = primoNumero / secondoNumero
    else:
        risultato = "operazione non valida"

    # invio di una risposta al client
    reply = f"risultato: {risultato}"
    sock.sendto(reply.encode(), addr)
    print(f"risultato dell'operazione: {primoNumero} {operazione} {secondoNumero} = {risultato}")