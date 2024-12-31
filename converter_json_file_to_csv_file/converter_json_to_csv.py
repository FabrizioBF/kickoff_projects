import json

if __name__ == '__main__':
    try:
        # Ler o arquivo JSON
        with open('input.json', 'r') as f:
            data = json.loads(f.read())

        # Criar o cabeçalho para o CSV
        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        # Escrever o arquivo CSV
        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
