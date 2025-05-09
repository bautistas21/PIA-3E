import hashlib
import requests
import time
import os
from pathlib import Path

def get_hash(texto, algoritmo='sha256'):
    """Genera el hash de un texto usando el algoritmo especificado."""
    hasher = hashlib.new(algoritmo)
    hasher.update(texto.encode('utf-8'))
    return hasher.hexdigest()

def write_hash(hash_texto, texto_original, nombre_archivo="hashes.txt"):
    """
    Guarda el hash y texto original en una wordlist personalizada.
    Si el archivo no existe, lo crea en la carpeta 'Diccionarios'.
    """
    diccionarios_dir = Path("Diccionarios")
    diccionarios_dir.mkdir(exist_ok=True)
    
    archivo_path = diccionarios_dir / nombre_archivo
    
    with open(archivo_path, 'a', encoding='utf-8') as f:
        f.write(f"{hash_texto}:{texto_original}\n")
    
    print(f"Hash guardado en: {archivo_path}")

def verify_hash(texto, hash_objetivo, algoritmo='sha256'):
    """Verifica si el texto coincide con el hash proporcionado."""
    return get_hash(texto, algoritmo) == hash_objetivo

def search(hash_objetivo, ruta_wordlist, algoritmo='sha256'):
    """Intenta descifrar un hash usando una wordlist."""
    if not os.path.exists(ruta_wordlist):
        print("Archivo de wordlist no encontrado.")
        return None
    
    with open(ruta_wordlist, 'r', encoding='utf-8', errors='ignore') as archivo:
        for linea in archivo:
            if ':' in linea:
                hash_guardado, texto = linea.strip().split(':', 1)
                if hash_guardado == hash_objetivo:
                    return texto
            else:
                palabra = linea.strip()
                if verify_hash(palabra, hash_objetivo, algoritmo):
                    return palabra
    return None

def check_hibp(password):
    """Consulta en HIBP si el hash aparece en algun breach"""
    sha1_hash=hashlib.sha1(password.encode()).hexdigest().upper()
    prefix=sha1_hash[:5]
    suffix=sha1_hash[5:]
    
    try:
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{prefix}",
            headers={"User-Agent": "MyPasswordChecker"}
        )
        response.raise_for_status()
        
        for line in response.text.splitlines():
            if line.split(":")[0] == suffix:
                return int(line.split(":")[1])
        return 0
    
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar HIBP: {e}")
        return -1
    finally:
        time.sleep(1.6)#Para que no sobrepase el límite y respetar el tiempo de espera

from pathlib import Path

def show_hashes(nombre_archivo="hashes.txt", max_hashes=None):
    """Muestra los hashes que hay en el diccionario"""
    ruta_archivo = Path("Diccionarios") / nombre_archivo
    
    if not ruta_archivo.exists():
        print(f"\n El archivo {ruta_archivo} no existe.")
        return
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        lineas = [linea.strip() for linea in f.readlines() if linea.strip()]

    if not lineas:
        print("\n El archivo no contiene hashes.")
        return
    total = len(lineas)
    mostrar_todos = True
    
    if max_hashes is None and total > 50:
        respuesta = input(f"\n Quieres mostrar todos los {total} hashes? (s/n): ").lower()
        if respuesta != 's':
            max_hashes = 50
            mostrar_todos = False

    print(f"\n=== Hashes almacenados ({total} registros) ===\n")
    
    for i, linea in enumerate(lineas[:max_hashes], 1):
        if ':' in linea:
            hash_val, texto = linea.split(':', 1)
            print(f"{i}. {hash_val} : {texto}")
        else:
            print(f"{i}. {linea}")

    if not mostrar_todos and max_hashes < total:
        print(f"\n[Mostrando {max_hashes} de {total} hashes.")
