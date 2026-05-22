import os
import requests

url='https://api.open-meteo.com/v1/forecast?latitude=-23.48&longitude=-46.68&hourly=apparent_temperature&current=temperature_2m&timezone=America%2FSao_Paulo&forecast_days=1'
nome_arquivo = "temperaturas.txt"

temperatura_hoje = requests.get(url).json()['current']
data = temperatura_hoje['time']
temperatura_agora = temperatura_hoje['temperature_2m']
#seguidores = [["geissoncr", 30]]
#nome_arquivo = "seguidores.txt"
#usuario = "geissoncr"
#qtde = 30

arquivo_vazio = not os.path.exists(nome_arquivo) or os.path.getsize(nome_arquivo) == 0

with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
    if arquivo_vazio:
        # Cria um cabeçalho simples separado por tabulação (\t)
        arquivo.write("data\t\ttemperaturaAgora\n")
        arquivo.write("-" * 30 + "\n")

    # Acrescenta o registro formatado
    arquivo.write(f"{data:<15}\t{temperatura_agora}\n")
