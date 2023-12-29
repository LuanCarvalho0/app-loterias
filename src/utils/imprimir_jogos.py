from time import sleep


def imprimir(janela, evento, jogos) -> None:
    print('-=' * 3, f'SORTEANDO {len(jogos)} JOGOS DA {evento.upper()}', '-=' * 3)
    janela.Refresh()
    for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
        janela.Refresh()
        sleep(1)
    print('-=' * 5, '< BOA SORTE! >', '-=' * 5, '\n')
