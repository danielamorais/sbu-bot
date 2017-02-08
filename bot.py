#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


os.system("./download_gecko2.sh")
try:
    firefox = webdriver.Firefox(executable_path='./geckodriver')
except WebDriverException, err:
    print "Geckodriver não encontrado."
    raise


def login():
    firefox.get('http://acervus.unicamp.br/asp/login.asp?modo_busca=rapida&content=mensagens&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0')
    firefox.implicitly_wait(10)
    WebDriverWait(firefox, 60).until(EC.visibility_of_element_located((By.ID, 'button1')))
    try:
        input_login = firefox.find_element_by_name("codigo")
        input_login.send_keys('email')
        input_pwd = firefox.find_element_by_name("senha")
        input_pwd.send_keys('senha')
        send_button = firefox.find_element_by_id("button1")
        send_button.click()
        WebDriverWait(firefox, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'justificado')))
    except Exception, err:
        print "deu ruim"
        print Exception, err
    return

login()
firefox.get('http://acervus.unicamp.br/')
firefox.implicitly_wait(10)
WebDriverWait(firefox, 60).until(EC.visibility_of_element_located((By.ID, 'mainFrame')))
firefox.switch_to_frame(firefox.find_element_by_id('mainFrame'))
try:
    firefox.find_element_by_link_text('Serviços').click()
    firefox.implicitly_wait(10)
    firefox.find_element_by_link_text('Circ./Renovação').click()
    WebDriverWait(firefox, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Renovar itens selecionados')))
    #firefox.switch_to_frame(firefox.find_element_by_id('mainFrame'))
    checkboxes = firefox.find_elements_by_name('ck1')
    for checkbox in checkboxes:
        checkbox.click()
    #firefox.find_element_by_link_text('Renovar itens selecionados').click()
    print "renovou"
except Exception, err:
    print "bosta"
    print Exception, err
#firefox.close()
