from random import randint


def sorteando_jogos(
        limite_de_numeros_por_jogo, 
        numero_maximo_do_sorteio,
        quantidade_de_jogos
        ) -> list[list[str]]:
    
    jogo = list()
    lista_de_jogos = list()

    jogos_sorteados = 0

    while jogos_sorteados < quantidade_de_jogos:
        numeros_sorteados = 0
        while numeros_sorteados < limite_de_numeros_por_jogo:
            numero = randint(1, numero_maximo_do_sorteio)
            numero = f'{numero:02}'
            if numero not in jogo:
                jogo.append(numero)
                numeros_sorteados += 1
        jogo.sort()

        if jogo not in lista_de_jogos:
            lista_de_jogos.append(jogo[:])
            jogo.clear()
            jogos_sorteados += 1

    return lista_de_jogos
