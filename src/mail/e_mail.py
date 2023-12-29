import email
import imaplib
import re


def obtendo_codigo_de_verificacao(user_email: str, senha: str, servidor: str) -> str:

    # Conectamos ao servidor do outlook.
    # lista de imaps: https://www.systoolsgroup.com/imap/
    if servidor:
        conexao = imaplib.IMAP4_SSL('imap.gmail.com')
    else:
        conexao = imaplib.IMAP4_SSL('imap-mail.outlook.com')

    # logando no email
    conexao.login(user=user_email, password=senha)

    # abrindo caixa de entrada
    conexao.select(mailbox='inbox')

    _, ids_email = conexao.search(None, '(FROM "logincaixa@caixa.gov.br")')
    id = ids_email[0].split()[-1]

    _, datos = conexao.fetch(id, "(RFC822)")

    messagem = email.message_from_bytes(datos[0][1])

    for parte in messagem.walk():
        if parte.get_content_type() == "text/plain":
            texto = parte.as_string()

    codigo = re.search(r"\d{6}", texto)
    codigo_verificacao = codigo.group()
    conexao.close()
    return codigo_verificacao
