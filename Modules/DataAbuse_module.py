import requests

def check_ip_abuse(api_key, ip, dias_max=90):
    """
    Consulta la API de AbuseIPDB para verificar si una IP ha sido reportada. Se necesita la Api Key, la Ip/Dominio y la cantidad máxima de días para ser tomado en cuenta el reporte 
    Muestra información sobre el historial de abuso de la IP.
    """
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": api_key,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": dias_max
    }

    try:
        print(f"Consultando AbuseIPDB para la IP: {ip}")
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()["data"]

        print(f"\nIP: {data['ipAddress']}")
        print(f"Abuso reportado: {data['totalReports']} veces")
        print(f"Último reporte: {data['lastReportedAt']}")
        print(f"Puntaje de abuso: {data['abuseConfidenceScore']} / 100")
        print(f"ISP: {data['isp']}")
        print(f"Dominio: {data['domain']}")
        print(f"País: {data['countryCode']}")

    except requests.exceptions.RequestException as e:
        print(f"Error al consultar AbuseIPDB: {e}")
