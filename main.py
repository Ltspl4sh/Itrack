import socket
import requests

def get_ip_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'fail':
            return f"Could not locate IP: {ip}"
        return f"""
        IP: {data['query']}
        Country: {data['country']}
        Region: {data['regionName']}
        City: {data['city']}
        Latitude: {data['lat']}
        Longitude: {data['lon']}
        """
    except requests.RequestException as e:
        return f"Error retrieving information: {str(e)}"

def print_ascii_art():
    print("""
    *****************************
    *     Itrack IP Locator     *
    *        by lt_Spl4sh       *
    *****************************
    """)

def main():
    print_ascii_art()
    ip = input("Enter the IP address to locate: ")
    print(get_ip_info(ip))

if __name__ == "__main__":
    main()
