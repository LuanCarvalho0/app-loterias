from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from mail.e_mail import obtendo_codigo_de_verificacao
from PySimpleGUI import popup_ok
from time import sleep


class Loterica():

    def __init__(self) -> None:
        
        options = Options()
        options.add_experimental_option("detach", True)

        self.service = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.service, options=options)
        self.navegador.implicitly_wait(10)
        self.navegador.set_window_size(724,858)

    def fazendo_login_no_site_da_loterica(self, dados: dict) -> None:
        
        self.navegador.get('https://www.loteriasonline.caixa.gov.br/silce-web/#/termos-de-uso')
        sleep(1)
        self.navegador.find_element(By.XPATH, '//*[@id="adopt-accept-all-button"]').click()
        sleep(1)
        self.navegador.find_element(By.ID, 'botaosim').click()
        sleep(1)
        self.navegador.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
        sleep(1)
        self.navegador.find_element(By.XPATH, '//*[@id="username"]').send_keys(dados['CPF'] + Keys.ENTER)
        sleep(1)
        self.navegador.find_element(By.XPATH, '//*[@id="form-login"]/div[2]/button[1]').click()


        sleep(6)
        codigo = obtendo_codigo_de_verificacao(user_email=dados['Email'], senha=dados['senha_email'], servidor=dados['Gmail'])
        self.navegador.find_element(By.XPATH, '//*[@id="codigo"]').send_keys(codigo + Keys.ENTER)
        sleep(1)
        self.navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys(dados['senha'] + Keys.ENTER)

    def preencendo_jogos_no_site(self, lista_de_apostas) -> None:

        for aposta in lista_de_apostas:
            self.navegador.get(aposta[0])
            sleep(2)
            for jogo in aposta[1]:
                elemento = self.navegador.find_element(By.XPATH, '//*[@id="container-volante"]/div/div[1]/div[1]/h3')
                self.navegador.execute_script("arguments[0].scrollIntoView(true);", elemento)
                for numero in jogo:
                    WebDriverWait(self.navegador, 10).until(
                        EC.presence_of_element_located((By.XPATH, f'//*[@id="n{numero}"]'))
                    )
                    sleep(1)
                    elemento = self.navegador.find_element(By.XPATH, f'//*[@id="n{numero}"]')
                    self.navegador.execute_script("arguments[0].click();", elemento)
                sleep(1)
                elemento = self.navegador.find_element(By.XPATH, '//*[@id="colocarnocarrinho"]')
                self.navegador.execute_script("arguments[0].click();", elemento)
                sleep(1)
            
        # Clicar em Ir para Pagamento
        sleep(1)
        elemento = self.navegador.find_element(By.XPATH, '//*[@id="irparapagamento"]')
        self.navegador.execute_script("arguments[0].click();", elemento)

        popup_ok('Atenção', 'Agora é só escolher a forma de pagamento.' ,'Em seguida, clique em "OK" para fechar o navegador.')
        try:
            self.navegador.close()
        except:
            pass
