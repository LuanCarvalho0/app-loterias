import PySimpleGUI as sg
from popups.popups import quantidade_de_jogos, dados_do_usuario
from gerador_jogos.gerador import sorteando_jogos
from utils.imprimir_jogos import imprimir
from utils.salvar_jogos import salvar_jogos_em_arquivo
from utils.limpar_jogos import limpar
from loterias.loterica import Loterica


lista_de_apostas = list()

layout_esquerdo = [
    [sg.Button('Mega da Virada',image_filename='./img/megaSena.png', image_size=(300, 20) ,image_subsample=2)],
    [sg.Button('Loto Fácil',image_filename='./img/lotoFacil.png', image_size=(300, 20) ,image_subsample=2)],
    [sg.Button('Quina',image_filename='./img/quina.png', image_size=(300, 20) ,image_subsample=2)],
    [sg.Button('Loto Mania',image_filename='./img/lotoMania.png', image_size=(300, 20) ,image_subsample=2)],
    [sg.Button('Dupla Sena',image_filename='./img/duplaSena.png', image_size=(300, 20) ,image_subsample=2)],
]

layout_direito = [
    [sg.Output(size=(70,15), key='OUTPUT')],
    [sg.Button('Fazer Apostas'), sg.Push(), sg.Button('Limpar'), sg.Button('Sair')],
]

layout = [
    [sg.Text('Escolha a loteria que deseja sortear os números:')],
    [sg.Column(layout_esquerdo), sg.VSeparator(), sg.Column(layout_direito)],
    
]

janela_inicial = sg.Window('Sistema de Loterias', layout=layout)
janela_inicial.set_icon('img/icone.ico')

while True:
    evento, valores = janela_inicial.read()

    match(evento):

        case 'Mega da Virada' | 'Loto Fácil' | 'Quina' | 'Loto Mania' | \
            'Time Mania' | 'Dupla Sena' | 'Dia de Sorte' | 'Super Sete':
            
            qtd_de_jogos = quantidade_de_jogos()

            match(evento):
                # limite_de_numeros_por_jogo: limte de números que cada jogo simples pode ter.
                # numero_maximo_do_sorteio: número maximo que pode ser sorteado.
                case 'Mega da Virada':
                    limite_de_numeros_por_jogo = 6
                    numero_maximo_do_sorteio = 60
                    url = 'https://www.loteriasonline.caixa.gov.br/silce-web/#/mega-sena/especial'

                case 'Loto Fácil':
                    limite_de_numeros_por_jogo = 15
                    numero_maximo_do_sorteio = 25
                    url = 'https://www.loteriasonline.caixa.gov.br/silce-web/#/lotofacil'

                case 'Quina':
                    limite_de_numeros_por_jogo = 5
                    numero_maximo_do_sorteio = 80
                    url = 'https://www.loteriasonline.caixa.gov.br/silce-web/#/quina'

                case 'Loto Mania':
                    limite_de_numeros_por_jogo = 50
                    numero_maximo_do_sorteio = 99
                    url = 'https://www.loteriasonline.caixa.gov.br/silce-web/#/lotomania'

                case 'Dupla Sena':
                    limite_de_numeros_por_jogo = 6
                    numero_maximo_do_sorteio = 50
                    url = 'https://www.loteriasonline.caixa.gov.br/silce-web/#/dupla-sena'

            if qtd_de_jogos > 0:
                jogos = sorteando_jogos(
                    limite_de_numeros_por_jogo=limite_de_numeros_por_jogo,
                    numero_maximo_do_sorteio=numero_maximo_do_sorteio,
                    quantidade_de_jogos=qtd_de_jogos,
                    )
                
                imprimir(janela=janela_inicial, evento=evento, jogos=jogos)

                salvar_jogos = sg.popup_yes_no('Você deseja salvar os números sorteados em um arquivo?')

                if salvar_jogos == 'Yes':
                    salvar_jogos_em_arquivo(evento=evento, jogos=jogos)

                lista_de_apostas.append((url, jogos))
                

        case 'Fazer Apostas':
            dados = dados_do_usuario()
            if valores != '':
                loterica = Loterica()
                loterica.fazendo_login_no_site_da_loterica(dados=dados)
                loterica.preencendo_jogos_no_site(lista_de_apostas=lista_de_apostas)
                limpar(lista_de_apostas, janela_inicial)
        
        case 'Limpar':
            limpar(lista_de_apostas, janela_inicial)

        case sg.WIN_CLOSED | 'Sair':
            break

janela_inicial.close()
