import shodan

def get_host_info(api_key, ip):
    """Consulta la API de Shodan para obtener información de una IP específica, se necesita una Api Key y la Ip/Dominio a busccar.
    Muestra en consola la información de la IP y los servicios expuestos.
    """
    api = shodan.Shodan(api_key)

    try:
        print(f"Resultados obtenidos de Shodan para la IP: {ip}")
        result = api.host(ip)

        print(f"\nIP: {ip}")
        print(f"Organización: {result.get('org', 'N/A')}")
        print(f"Sistema Operativo: {result.get('os', 'N/A')}")
        print(f"País: {result.get('country_name', 'Desconocido')}")
        print(f"Dominios: {', '.join(result.get('domains', []))}")
        print(f"Hostnames: {', '.join(result.get('hostnames', []))}")

        print("\n--- Servicios encontrados ---")
        for service in result['data']:
            print(f"\n Puerto: {service['port']}")
            print(f"Protocolo: {service.get('transport', 'tcp')}")
            print(f"Banner:\n{service['data'][:300]}")

    except shodan.APIError as e:
        print(f" Error al consultar Shodan: {e}")
