import os


def salvar_jogos_em_arquivo(evento, jogos):
    nome_arquivo = evento.replace(" ", "_")
    with open(f'{nome_arquivo}.txt', 'a+', newline='') as arquivo:
        for jogo in jogos:
            arquivo.write(str(jogo) + os.linesep)
