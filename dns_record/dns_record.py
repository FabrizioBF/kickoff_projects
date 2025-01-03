import dns.resolver

# Dicionário para armazenar os registros DNS de um site
dns_record = {}

try:
    # Site definido pelo usuário
    website = input("Enter the name of the website: ").strip()

    # Obtendo o registro 'A' e armazenando no dicionário
    a_record = dns.resolver.resolve(website, 'A')
    dns_record['A_Record_IPs'] = [ipval.to_text() for ipval in a_record]

    # Lista para armazenar os registros MX
    mx_record_list = []

    # Obtendo os registros MX e armazenando no dicionário
    mx_record = dns.resolver.resolve(website, 'MX')
    for server in mx_record:
        mx_record_list.append(server.to_text())

    dns_record['MX_Records'] = mx_record_list

    # Exibindo os registros no console
    print("\nDNS Records:")
    for key, value in dns_record.items():
        print(f"{key}: {value}")

except dns.resolver.NXDOMAIN:
    print("Error: Domain does not exist.")
except dns.resolver.NoAnswer:
    print("Error: No DNS record found.")
except dns.resolver.Timeout:
    print("Error: Query timed out.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
