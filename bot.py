from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# binary = FirefoxBinary('firefox')
firefox = webdriver.Firefox()
firefox.get('http://acervus.unicamp.br/')
firefox.implicitly_wait(30)
WebDriverWait(firefox, 60).until(EC.visibility_of_element_located((By.ID, 'mainFrame')))
firefox.switch_to_frame(firefox.find_element_by_id('mainFrame'))
try:
    #login = firefox.find_element_by_class_name('transparent-icon span_imagem icon_20 icon-key')
    firefox.find_element_by_link_text('Login').click()
    WebDriverWait(firefox, 60).until(EC.visibility_of_element_located((By.XPATH, '//iframe[@src="asp/login.asp?modo_busca=rapida&content=mensagens&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0"]'))) 
    firefox.switch_to_frame(firefox.find_element_by_xpath('//iframe[@src="asp/login.asp?modo_busca=rapida&content=mensagens&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0"]'))
    input_login = firefox.find_element_by_class_name("codigo")
    input_login.send_keys('blabla')
    input_pwd = firefox.find_element_by_class_name("senha")
    input_pwd.send_keys('123')
    send_button = firefox.find_element_by_id("button1")
    #login.click()
except Exception:
    print "deu ruim"
#firefox.implicitly_wait(10) # segundos
#firefox.close()
