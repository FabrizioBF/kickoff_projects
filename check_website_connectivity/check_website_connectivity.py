import csv
import requests


def main():
    status_dict = {}  # Inicializa o dicionário vazio

    with open("websites.txt", "r") as fr:
        for line in fr:
            website = line.strip()
            try:
                response = requests.get(website, timeout=5)
                status = response.status_code
                status_dict[website] = "working" if status == 200 else "not working"
            except requests.exceptions.RequestException:
                status_dict[website] = "not reachable"

    # Grava os resultados no arquivo CSV
    with open("website_status.csv", "w", newline="") as fw:
        csv_writer = csv.writer(fw)
        csv_writer.writerow(["Website", "Status"])  # Cabeçalho
        for key, value in status_dict.items():
            csv_writer.writerow([key, value])


if __name__ == "__main__":
    main()
