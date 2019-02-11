# -*- coding: utf-8 -*-

from selenium import webdriver
from datetime import datetime
import dateutil.relativedelta
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import sys

print('[ {"inicio": "%s"},' % str(datetime.now()))
# necessario para funcionar remotamente
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
firefox = webdriver.Firefox(firefox_options=opts)
# ============================================


# PARAMETROS
try: 
    dir_file = sys.argv[1]
except:
    pass
default_file_name = 'erro.png'
# =====================================


# PAGINA DE PRECOS
firefox.get('http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos')
try:
    # =====================================
    # /html/body/div[1]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div/table[2]/tbody/tr[3]
    precos = firefox.find_elements_by_xpath("//table[2]/tbody/tr[contains(@class, 'camposTesouroDireto')]")
    for preco in precos:
        
        titulo = preco.find_element_by_xpath('./td[1]').text
        vencimento = datetime.strptime(preco.find_element_by_xpath('./td[2]').text, '%d/%m/%Y')
        taxa_rendimento = (preco.find_element_by_xpath('./td[3]').text).replace('.', '').replace(',','.').replace('R$', '')
        valor_minimo = (preco.find_element_by_xpath('./td[4]').text).replace('.', '').replace(',','.').replace('R$', '')
        preco_unitario = (preco.find_element_by_xpath('./td[5]').text).replace('.', '').replace(',','.').replace('R$', '')    

        # print valores
        print(' { "titulo": "%s", "vencimento": "%s", "taxa_rendimento": "%s", "valor_minimo": "%s", "preco_unitario": "%s" }, ' % (titulo, vencimento, taxa_rendimento, valor_minimo, preco_unitario ))
        # fechando modal 

    # Fechar navegador
    firefox.quit()
    print('{"fim": "%s"} ]' % str(datetime.now()))
    
except Exception:  
    if dir_file is not None:
        firefox.save_screenshot(dir_file + "/" + default_file_name)
        pass
    firefox.quit()
    raise