import os
from tabulate import tabulate

nome_arquivo = "seguidores.txt"
seguidores = [["geissoncr", 30]]

# 1. Verifica se o arquivo NÃO existe ou se está totalmente vazio (0 bytes)
arquivo_vazio = not os.path.exists(nome_arquivo) or os.path.getsize(nome_arquivo) == 0

# 2. Abre o arquivo no modo "a" (append) para sempre acrescentar no final
with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
    if arquivo_vazio:
        # Se estiver vazio, gera a tabela COMPLETA com o cabeçalho
        tabela = tabulate(seguidores, headers=["usuario", "qtde Seguidores"])
        print(tabela, file=arquivo)
    else:
        # Se NÃO estiver vazio, gera APENAS as linhas de dados, sem o cabeçalho
        # O parâmetro tablefmt="plain" ajuda a manter o alinhamento simples
        tabela_sem_header = tabulate(seguidores, tablefmt="plain")
        print(tabela_sem_header, file=arquivo)
