import os

pasta = r"C:\*****\Desktop\*****"

for _ in range(2):
    arquivos = os.listdir(pasta)
    palavra_a_excluir = "_rotated"

    for arquivo in arquivos:
        nome_arquivo, extensao = os.path.splitext(arquivo)
        novo_nome = nome_arquivo.replace(palavra_a_excluir, "") + extensao
        caminho_arquivo_antigo = os.path.join(pasta, arquivo)
        caminho_arquivo_novo = os.path.join(pasta, novo_nome)
        os.rename(caminho_arquivo_antigo, caminho_arquivo_novo)

    for i in range(len(arquivos)):
        if arquivos[i].lower().endswith(("", "_rotated", "_1")):
            caminho_arquivo = os.path.join(pasta, arquivos[i])
            nome_arquivo, extensao = os.path.splitext(arquivos[i])
            if len(nome_arquivo) == 12 and (nome_arquivo.endswith("_rotated") or nome_arquivo.endswith("_1")):
                nome_sem_sufixo = nome_arquivo[:-2]
                if i < len(arquivos) - 1:
                    proximo_arquivo = arquivos[i + 1]
                    proximo_nome_arquivo, _ = os.path.splitext(proximo_arquivo)
                    if len(proximo_nome_arquivo) == 12 and proximo_nome_arquivo[:10] == nome_sem_sufixo[:10]:
                        continue
                novo_nome = nome_sem_sufixo + extensao
                novo_caminho = os.path.join(pasta, novo_nome)
                os.rename(caminho_arquivo, novo_caminho)
