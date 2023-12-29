import PySimpleGUI as sg


def quantidade_de_jogos() -> int:
    layout = [
        [sg.Text('Quantos jogos você quer que eu sorteie?'), sg.InputText(key='numero')],
        [sg.Button('Confirmar'), sg.Button('Cancelar')]
    ]

    janela_qtd_de_jogos = sg.Window('Número de Jogos', layout=layout)

    while True:
        evento, valores = janela_qtd_de_jogos.read()

        match(evento):

            case 'Confirmar':
                qtd_de_jogos = valores['numero']
                try:
                    qtd_de_jogos = int(qtd_de_jogos)
                    janela_qtd_de_jogos.close()
                    return qtd_de_jogos
                except ValueError:
                    sg.popup_error('Por favor, digite um número válido.')

            case sg.WINDOW_CLOSED | 'Cancelar':
                janela_qtd_de_jogos.close()
                return 0

def dados_do_usuario() -> dict:
    layout = [
        [sg.Text('Preencha os campos para realizar as apostas automaticamente.')],
        [sg.Text('Informações da sua conta na Loteria da Caixa:')],
        [sg.Push(), sg.Text('CPF:'), sg.InputText(key='CPF'), sg.Push()],
        [sg.Push(), sg.Text('Senha:'), sg.InputText(password_char='*' ,key='senha'), sg.Push()],

        [sg.Text('E-mail cadastrado associado à conta para obtenção do código de verificação.')],
        [sg.Radio('Outlook', "RADIO1", default=True, key='Outlook'), sg.Radio('Gmail', "RADIO1", key='Gmail')],
        [sg.Push(), sg.Text('E-mail:'), sg.InputText(key='Email'), sg.Push()],
        [sg.Push(), sg.Text('Senha:'), sg.InputText(password_char='*', key='senha_email'), sg.Push()],

        [sg.Button('Apostar'), sg.Button('Cancelar')]
    ]

    janela_dados_do_usuario = sg.Window('Dados do Usuário', layout=layout)

    while True:
        evento, valores = janela_dados_do_usuario.read()
        
        match(evento):

            case 'Apostar':
                cpf = valores['CPF']
                senha = valores['senha']
                email = valores['Email']
                senha_email = valores['senha_email']
                try:
                    if cpf == '' or senha == '' or email == '' or senha_email == '':
                        raise ValueError()
                    janela_dados_do_usuario.close()
                    return valores                 
                except ValueError:
                    sg.popup_error('Por favor, Digite todos os valores.')


            case sg.WINDOW_CLOSED | 'Cancelar':
                janela_dados_do_usuario.close()
                return ''
