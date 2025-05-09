import socket

def Ports(target, inicio=20, fin=100):
    """Muestra los puertos abiertos de un Dominio/IP"""
    for port in range(inicio, fin):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Puerto {port} abierto")
        sock.close()