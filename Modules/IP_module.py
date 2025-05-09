import socket
import requests

def get_public_ip():
    """Obtiene la dirección IP pública del sistema.
    Muestra la Ip local, pública, o ambas  
    """
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json().get("ip")
    
    except:
        return None

def get_local_ip():
    """ Obtiene la dirección IP local del sistema en la red actual. """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
        
    except:
        try:
            return socket.gethostbyname(socket.gethostname())
        
        except:
            return None