import logging
from datetime import datetime
import os
from pathlib import Path
#Configuración LOGS
def setup_logging():
    logs_dir = Path("Logs")
    logs_dir.mkdir(exist_ok=True)
    
    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
    log_path = logs_dir / log_filename

    logging.basicConfig(
        level = logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path)
        ]
    )
    logging.propagate = False

# SHODAN API KEY: 5zksrz4bnCwty0cKpaCUBhcKpi9mDato
# ABUSE IPDB API KEY: 4d22fb392b0549afbbc1def71623f1dc6d5f26371f2af2cfde2483b8baacf8e3f1641c69e5b8df01
# EJEMPLOS IPS: SHOPIFY: 23.227.38.74
#               GOOGLE: 8.8.8.8        
from Modules.IP_module import get_public_ip, get_local_ip
from Modules.Ports_module import Ports
from Modules.Shodan_module import get_host_info
from Modules.DataAbuse_module import check_ip_abuse
from Modules.Hash_module import get_hash, write_hash, verify_hash, search, check_hibp, show_hashes

def main():
    setup_logging()
    logging.info("Inicio de la aplicación de Ciberseguridad")
    
    while True:
        print("""-----Menú de Tareas de Ciberseguridad-----
            1- Ver IP (Local o pública)
            2- Ver puertos abiertos de un dominio o IP
            3- API Shodan
            4- API IP Data Abuse
            5- Generar Hashes/Buscar hashes
            6- Salir
            """)
        
        while True:
            try:
                opcion = int(input("Ingresa la tarea que deseas realizar: "))
                if (1 <= opcion <= 6):
                    logging.info(f"Opción seleccionada: {opcion}")
                    break
            except:
                logging.warning("Opción no válida ingresada")
                print("Opción no válida, vuelve a intentarlo")
                
        if (opcion == 1):
            logging.info("Inicio de consulta de IP")
            while True:
                try:
                    opcion_ip = int(input("Deseas ver tu ip: 1-Local 2-Pública 3-Ambas: "))
                    if (1 <= opcion_ip <= 3):
                        break
                except:
                    logging.warning("Opción de IP no válida")
                    print("Opción no válida, vuelve a intentarlo")
            
            if (opcion_ip == 1):
                Ip_publica = get_public_ip()
                print(f"Tu ip pública es {Ip_publica}")
                logging.info(f"IP pública obtenida: {Ip_publica}")
            elif (opcion_ip == 2): 
                Ip_local = get_local_ip()
                print(f"Tu ip local es {Ip_local}")
                logging.info(f"IP local obtenida: {Ip_local}")
            elif (opcion_ip == 3):
                Ip_publica = get_public_ip()
                Ip_local = get_local_ip()
                print(f"Tu ip pública es {Ip_publica}")
                print(f"Tu ip local es {Ip_local}")
                logging.info(f"IPs obtenidas - Pública: {Ip_publica}, Local: {Ip_local}")
            input("Presiona enter para continuar\n")

        elif (opcion == 2):
            logging.info("Inicio de escaneo de puertos")
            try:
                target = input("Ingresa el dominio o la IP de la cual deseas escanear los puertos: ")
                start = int(input("Ingresa el puerto desde donde inciará el escaneo: "))
                end = int(input("Ingresa el puerto en donde finalizará el escaneo: "))
                logging.info(f"Iniciando escaneo en {target} desde puerto {start} hasta {end}")
                Ports(target, start, end)
                logging.info("Escaneo de puertos completado")
            except Exception as e:
                logging.error(f"Error en escaneo de puertos: {str(e)}")
                print("Ocurrió un error con el dominio/IP")
            finally:
                input("Presiona enter para continuar\n")

        elif (opcion == 3):
            logging.info("Inicio de consulta Shodan")
            try:
                api_key = input("Ingresa tu api key: ")
                ip_shodan = input("Ingresa la IP deseas buscar dentro de shodan: ")
                logging.info(f"Consultando Shodan para IP: {ip_shodan}")
                get_host_info(api_key, ip_shodan)
                logging.info("Consulta Shodan completada")
            except Exception as e:
                logging.error(f"Error en consulta Shodan: {str(e)}")
            finally:
                input("Presiona enter para continuar\n")

        elif (opcion == 4):
            logging.info("Inicio de consulta AbuseIPDB")
            try:
                api_key = input("Ingresa tu api key: ")
                ip_data = input("Ingresa la dirección IP a consultar: ")
                dias = int(input("Ingresa el rango de días máximo para considerar los reportes de la ip: "))
                logging.info(f"Consultando AbuseIPDB para IP: {ip_data} con {dias} días de historial")
                check_ip_abuse(api_key, ip_data, dias)
                logging.info("Consulta AbuseIPDB completada")
            except Exception as e:
                logging.error(f"Error en consulta AbuseIPDB: {str(e)}")
            finally:
                input("Presiona enter para continuar\n")

        elif (opcion == 5):
            logging.info("Inicio de operaciones con hashes")
            print("""\n Opciones:
                1- Generar Hash
                2- Consultar Diccionario  
                3- Buscar Hash dentro de un diccionario
                4- Verificar si hay coincidencias del Hash en HaveIBeenPwned
                """)
            while True:
                try:
                    opcion_hash = int(input("Ingresa la opción a realizar: "))
                    if (1 <= opcion_hash <= 4):
                        logging.info(f"Opción hash seleccionada: {opcion_hash}")
                        break
                except:
                    logging.warning("Opción hash no válida")
                    print("Opcion no válida")
            
            if (opcion_hash == 1):
                try:
                    texto = input("Ingrese el texto a hashear: ")
                    algoritmo = input("Algoritmo (md5/sha1/sha256/sha512): ").lower() or 'sha256'
                    logging.info(f"Generando hash {algoritmo} para texto")
                    hash_generado = get_hash(texto, algoritmo)
                    print(f"\nHash ({algoritmo.upper()}): {hash_generado}")
                    logging.info(f"Hash generado: {hash_generado}")
                    
                    guardar = input("\nQuieres guardar el hash en un diccionario? (s/n): ").lower()
                    if guardar == 's':
                        diccionario = input("Nombre del archivo con .txt: ") or "hashes.txt"
                        write_hash(hash_generado, texto, diccionario)
                        print("Hash guardado con éxito")
                        logging.info(f"Hash guardado en {diccionario}")
                except Exception as e:
                    logging.error(f"Error generando hash: {str(e)}")
                finally:
                    input("Presiona enter para continuar\n")
            
            elif (opcion_hash == 2):
                try:
                    nombre = input("Ingresa el nombre del diccionario: ")
                    cant = int(input("Ingresa cuántos hashes quieres ver: "))
                    logging.info(f"Mostrando {cant} hashes de {nombre}")
                    show_hashes(nombre, cant)
                except Exception as e:
                    logging.error(f"Error mostrando hashes: {str(e)}")
                finally:
                    input("Presiona enter para continuar\n")
            
            elif (opcion_hash == 3):
                try:
                    diccionario = input("Ruta completa a el diccionario (con txt): ")
                    hash_generado = input("Ingrese el hash a buscar: ")
                    algoritmo = input("Algoritmo (md5/sha1/sha256/sha512): ").lower() or 'sha256'
                    logging.info(f"Buscando hash {hash_generado} en {diccionario}")
                    palabra_descifrada = search(hash_generado, diccionario, algoritmo)
                    if palabra_descifrada:
                        print(f"\nContraseña encontrada: '{palabra_descifrada}'")
                        logging.info(f"Hash encontrado: {palabra_descifrada}")
                    else:
                        print("\nContraseña no encontrada en el diccionario.")
                        logging.info("Hash no encontrado en diccionario")
                except Exception as e:
                    logging.error(f"Error buscando hash: {str(e)}")
                finally:
                    input("Presiona enter para continuar\n")

            elif (opcion_hash == 4):
                try:
                    password = input("Ingresa una contraseña para verificar: ")
                    logging.info("Verificando contraseña en HIBP")
                    breaches = check_hibp(password)
                    if (breaches > 0):
                        print(f"Esta contraseña apareció en {breaches} brechas de datos.")
                        logging.warning(f"Contraseña comprometida encontrada en {breaches} brechas")
                    elif (breaches == 0):
                        print("Contraseña no encontrada en brechas conocidas.")
                        logging.info("Contraseña no encontrada en HIBP")
                    else:
                        print("No se pudo verificar (error de conexión).")
                        logging.error("Error de conexión con HIBP")
                except Exception as e:
                    logging.error(f"Error verificando HIBP: {str(e)}")
                finally:
                    input("Presiona enter para continuar\n")

        elif (opcion == 6):
            logging.info("Se finalizó el programa")
            break

if __name__ == "__main__":
    main()