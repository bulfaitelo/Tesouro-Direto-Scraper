# -*- coding: utf-8 -*-

from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import sys

print('[ {"inicio": "%s"},' % str(datetime.now()))
# necessario para funcionar remotamente
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
firefox = webdriver.Firefox(firefox_options=opts)
# ============================================

# parametros
user_login = sys.argv[1]
user_pass = sys.argv[2]
# =====================================

# PAGINA DE LOGIN
firefox.get('https://tesourodireto.bmfbovespa.com.br/portalinvestidor/')

# preenchendo formulario de login
login = firefox.find_element_by_id('BodyContent_txtLogin')
password = firefox.find_element_by_id('BodyContent_txtSenha')
login.send_keys("", user_login)
password.send_keys("", user_pass)
login_attempt = firefox.find_element_by_id('BodyContent_btnLogar')
login_attempt.click()
# ====================================

#  pagina de consulta
firefox.get('https://tesourodireto.bmfbovespa.com.br/portalinvestidor/extrato.aspx')
btn_consultar = firefox.find_element_by_id('BodyContent_btnConsultar')
btn_consultar.click()
# =====================================

representantes = firefox.find_elements_by_xpath("//div[contains(@class, 'section-container')]")

# print(vars(representantes))
for representante in representantes:   
    nome_representante = representante.find_element_by_xpath('./section/p/a').text.split(' - ')
    table_rows = representante.find_elements_by_xpath('./section/div/table/tbody/tr')
    nome_representante = nome_representante[1]
    for table_row in table_rows:
        titulo = table_row.find_element_by_xpath('./td[1]').text
        vencimento = datetime.strptime(table_row.find_element_by_xpath('./td[2]').text, '%d/%m/%Y')
        valor_investido = (table_row.find_element_by_xpath('./td[3]').text).replace('.', '').replace(',','.')
        valor_bruto_atual = (table_row.find_element_by_xpath('./td[4]').text).replace('.', '').replace(',','.')
        valor_liquido_atual = (table_row.find_element_by_xpath('./td[5]').text).replace('.', '').replace(',','.')
        quant_total = (table_row.find_element_by_xpath('./td[6]').text).replace(',', '.')
        quant_bloqueado = (table_row.find_element_by_xpath('./td[7]').text).replace(',', '.')
        print('{ "nome_representante": "%s", "titulo": "%s", "vencimento": "%s", "valor_investido": "%s", "valor_bruto_atual": "%s", "valor_liquido_atual": "%s", "quant_total": "%s", "quant_bloqueado": "%s" },' % (nome_representante, titulo, vencimento, valor_investido, valor_bruto_atual, valor_liquido_atual, quant_total, quant_bloqueado))
        
# Fechar navegador
firefox.quit()
print('{"fim": "%s"} ]' % str(datetime.now()))