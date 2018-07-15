# -*- coding: utf-8 -*-

# =========== IMPORTS =========== 
from datetime import datetime
import dateutil.relativedelta
from time import sleep
import sys
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# ===============================


# ========== FUNCTIONS ==========
# Check if xpath existis
def is_element_present_xpath(xpath):
    try: firefox.find_element_by_xpath(xpath)
    except NoSuchElementException: return False
    return True
# ===============================

print('[ {"inicio": "%s"},' % str(datetime.now()))
# necessario para funcionar remotamente
opts = FirefoxOptions()
# opts.add_argument("--headless")
firefox = webdriver.Firefox(firefox_options=opts)
# ============================================

# parametros
user_login = sys.argv[1]
user_pass = sys.argv[2]
wait_time = 10
# =====================================

# PAGINA DE LOGIN
firefox.get('https://tesourodireto.bmfbovespa.com.br/portalinvestidor/')

# preenchendo formulario de login
login = WebDriverWait(firefox, wait_time).until(EC.presence_of_element_located((By.ID, 'BodyContent_txtLogin'))) 
password = WebDriverWait(firefox, wait_time).until(EC.presence_of_element_located((By.ID, 'BodyContent_txtSenha'))) 
login.send_keys("", user_login)
password.send_keys("", user_pass)
login_attempt = WebDriverWait(firefox, wait_time).until(EC.presence_of_element_located((By.ID, 'BodyContent_btnLogar'))) 
login_attempt.click()
# ====================================

# pagina de protocolos
firefox.get('https://tesourodireto.bmfbovespa.com.br/portalinvestidor/consulta-protocolo.aspx')


# INVESTIMENTOS
# selecionando a operação
select_operacao = Select(firefox.find_element_by_id('BodyContent_ddlOperacao'))
select_operacao.select_by_visible_text('Investimento')

# selecionando a data
key_data_inicial = datetime.now()
key_data_final = key_data_inicial - dateutil.relativedelta.relativedelta(months=1)
# data inicial
data_inicial = firefox.find_element_by_id('BodyContent_dtRealizacaoInicial')
data_inicial.send_keys("", key_data_final.strftime("%d%m%Y"))
# data_inicial.send_keys("", key_data_final.strftime("17102017")) 
# data final
data_final = firefox.find_element_by_id('BodyContent_dtRealizacaoFinal')
data_final.send_keys("", key_data_inicial.strftime("%d%m%Y"))
# data_final.send_keys("", key_data_inicial.strftime("13062018"))  
# clicando em consulta
btn_consultar = firefox.find_element_by_id('BodyContent_btnConsultar')
btn_consultar.click()

# =====================================

protocolos = firefox.find_elements_by_xpath("//table[contains(@class, 'responsive')]/tbody[2]/tr[contains(@class, 'nowrap')]")

if is_element_present_xpath("//table[contains(@class, 'responsive')]/tbody[2]/tr[contains(@class, 'nowrap')][1]/td[2]"):    
    for protocolo in protocolos:
        numero_protocolo = protocolo.find_element_by_xpath('./td[1]').text
        operacao = protocolo.find_element_by_xpath('./td[2]').text
        situacao = protocolo.find_element_by_xpath('./td[3]').text
        realizacao = datetime.strptime(protocolo.find_element_by_xpath('./td[4]').text, '%d/%m/%Y')
        liquidacao = protocolo.find_element_by_xpath('./td[5]').text
        if liquidacao:        
            liquidacao = datetime.strptime(liquidacao, '%d/%m/%Y')
        
        detalhes = protocolo.find_element_by_xpath('./td[6]/img')
        detalhes.click()
        sleep(2)
        # modal detalhes 
        # modal_frame = firefox.switch_to.frame('modal')    
        detalhes_modal = firefox.find_element_by_xpath('//*[@id="modal"]')    
        # Dados Modal
        nome_representante = detalhes_modal.find_element_by_xpath('./div[1]/div[2]/div[4]/div[2]/label').text.split(' - ')
        nome_representante = nome_representante[0]
        titulo = detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[1]').text
        quantidade = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[2]').text).replace('.', '').replace(',','.')
        valor_unitario = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[3]').text).replace('.', '').replace(',','.')
        taxa_juros = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[4]').text).replace('.', '').replace(',','.')
        taxa_b3 = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[5]').text).replace('.', '').replace(',','.')
        taxa_custodia = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[6]').text).replace('.', '').replace(',','.')
        valor_total = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[7]').text).replace('.', '').replace(',','.')
        # print valores
        print('{ "numero_protocolo": "%s", "operacao": "%s", "situacao": "%s", "realizacao": "%s", "liquidacao": "%s", "representante": "%s", "titulo": "%s", "quantidade": "%s", "valor_unitario": "%s", "taxa_juros": "%s", "taxa_b3": "%s", "taxa_custodia": "%s", "valor_total": "%s" }, ' % (numero_protocolo, operacao, situacao, realizacao, liquidacao, nome_representante, titulo, quantidade, valor_unitario, taxa_juros, taxa_b3, taxa_custodia, valor_total))#.encode('utf8')
        # fechando modal 
        sair_modal = detalhes_modal.find_element_by_class_name('close-reveal-modal')
        sair_modal.click()
# INVESTIMENTOS -- FIM

# RESGATE
# Reiniciando a Consulta
btn_consultar = firefox.find_element_by_id('BodyContent_btnConsultar')
btn_consultar.click()
# selecionando a operação
select_operacao = Select(firefox.find_element_by_id('BodyContent_ddlOperacao'))
select_operacao.select_by_visible_text('Resgate')

# selecionando a data
key_data_inicial = datetime.now()
key_data_final = key_data_inicial - dateutil.relativedelta.relativedelta(months=1)
# data inicial
data_inicial = firefox.find_element_by_id('BodyContent_dtRealizacaoInicial')
data_inicial.send_keys("", key_data_final.strftime("%d%m%Y"))
# data_inicial.send_keys("", key_data_final.strftime("17102017")) 
# data final
data_final = firefox.find_element_by_id('BodyContent_dtRealizacaoFinal')
data_final.send_keys("", key_data_inicial.strftime("%d%m%Y"))
# data_final.send_keys("", key_data_inicial.strftime("13062018"))  

# clicando em consulta
btn_consultar = firefox.find_element_by_id('BodyContent_btnConsultar')
btn_consultar.click()

# =====================================

protocolos = firefox.find_elements_by_xpath("//table[contains(@class, 'responsive')]/tbody[2]/tr[contains(@class, 'nowrap')]")
if is_element_present_xpath("//table[contains(@class, 'responsive')]/tbody[2]/tr[contains(@class, 'nowrap')][1]/td[2]"):    
    for protocolo in protocolos:
        numero_protocolo = protocolo.find_element_by_xpath('./td[1]').text
        operacao = protocolo.find_element_by_xpath('./td[2]').text
        situacao = protocolo.find_element_by_xpath('./td[3]').text
        realizacao = datetime.strptime(protocolo.find_element_by_xpath('./td[4]').text, '%d/%m/%Y')
        liquidacao = protocolo.find_element_by_xpath('./td[5]').text
        if liquidacao:        
            liquidacao = datetime.strptime(liquidacao, '%d/%m/%Y')
        
        detalhes = protocolo.find_element_by_xpath('./td[6]/img')
        detalhes.click()
        sleep(2)
        # modal detalhes 
        # modal_frame = firefox.switch_to.frame('modal')    
        detalhes_modal = firefox.find_element_by_xpath('//*[@id="modal"]')    
        # Dados Modal
        nome_representante = detalhes_modal.find_element_by_xpath('./div[1]/div[2]/div[4]/div[2]/label').text.split(' - ')
        nome_representante = nome_representante[0]
        titulo = detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[1]').text
        quantidade = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[2]').text).replace('.', '').replace(',','.')
        valor_unitario = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[3]').text).replace('.', '').replace(',','.')
        taxa_juros = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[4]').text).replace('.', '').replace(',','.')
        taxa_b3 = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[5]').text).replace('.', '').replace(',','.')
        taxa_custodia = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[6]').text).replace('.', '').replace(',','.')
        valor_total = (detalhes_modal.find_element_by_xpath('./div[2]/div/div/table/tbody/tr/td[7]').text).replace('.', '').replace(',','.')
        # print valores
        print('{ "numero_protocolo": "%s", "operacao": "%s", "situacao": "%s", "realizacao": "%s", "liquidacao": "%s", "representante": "%s", "titulo": "%s", "quantidade": "%s", "valor_unitario": "%s", "taxa_juros": "%s", "taxa_b3": "%s", "taxa_custodia": "%s", "valor_total": "%s" }, ' % (numero_protocolo, operacao, situacao, realizacao, liquidacao, nome_representante, titulo, quantidade, valor_unitario, taxa_juros, taxa_b3, taxa_custodia, valor_total))#.encode('utf8')
        # fechando modal 
        sair_modal = detalhes_modal.find_element_by_class_name('close-reveal-modal')
        sair_modal.click()
# RESGATE -- FIM

# Fechar navegador
# firefox.quit()
print('{"fim": "%s"} ]' % str(datetime.now()))