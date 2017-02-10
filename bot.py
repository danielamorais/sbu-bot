#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import yaml

from datetime import date, datetime

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


CONFIG_DIR = os.path.join(os.environ['HOME'], '.sbu-bot/')
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.yml")
INSTALL_PATH = '/usr/local/bin/sbu-bot'
GECKO_PATH = os.path.join(INSTALL_PATH, 'geckodriver')
RODAR_SEMPRE = False
RENOVAR_SEMPRE = False
SEM_CABECA = True
TAM_SENHA = 8  # tamanho máximo da senha

logging.basicConfig(
    filename=os.path.join(CONFIG_DIR, 'log.log'), level=logging.INFO,
    format='%(asctime)s\t\t%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')


def load_config():
    """
    loads config dictionary containing keys "email", "senha" and "lastrun"
    from config.yml file
    """
    try:
        with open(CONFIG_FILE, "r") as config_file:
            config_dict = yaml.load(config_file)
    except Exception, err:
        error_message = "Erro na leitura de configuração."
        print error_message
        logging.exception(error_message)
        raise
    return config_dict


def write_config(config):
    """
    writes config to config.yml
    """
    try:
        with open(CONFIG_FILE, "w") as config_file:
            yaml.dump(config, default_flow_style=False, stream=config_file)
    except Exception, err:
        error_message = "Erro as escrever configuração."
        print error_message
        logging.exception(error_message)
        raise


def login(email, senha, firefox):
    firefox.get('http://acervus.unicamp.br/asp/login.asp?modo_busca=rapida&content=mensagens&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0')
    firefox.implicitly_wait(10)
    WebDriverWait(firefox, 60).until(EC.visibility_of_element_located((By.ID, 'button1')))
    try:
        input_login = firefox.find_element_by_name("codigo")
        input_login.send_keys(email)
        input_pwd = firefox.find_element_by_name("senha")
        input_pwd.send_keys(senha)
        send_button = firefox.find_element_by_id("button1")
        send_button.click()
        WebDriverWait(firefox, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'justificado')))
    except Exception, err:
        error_message = "Erro no login. Verifique usuário e senha."
        print error_message
        logging.exception(error_message)
        raise
    return


def renova(firefox):
    firefox.get('http://acervus.unicamp.br/')
    firefox.implicitly_wait(30)
    WebDriverWait(firefox, 60).until(EC.visibility_of_element_located((By.ID, 'mainFrame')))
    firefox.switch_to_frame(firefox.find_element_by_id('mainFrame'))
    try:
        # seleciona e clica no menu "Serviços"
        # print firefox.page_source
        firefox.find_element_by_xpath(
            '//a[contains(text(), "Serviços")]').click()
        # selecion e clica "Circ./Renovação"
        firefox.find_element_by_xpath(
            '//a[contains(text(), "Circ./Renovação")]').click()

        WebDriverWait(
            firefox, 30).until(
            EC.visibility_of_element_located(
                (By.LINK_TEXT, 'Renovar itens selecionados')))

        tabela = firefox.find_elements_by_css_selector(
            'table.tab_circulacoes')[0]
        livros = tabela.find_elements_by_css_selector('tr')[1:]

        # renovar = True só se há alguma entrega para hoje
        renovar = False
        hoje = date.today()
        for livro in livros:
            data_devolucao_str = livro.find_elements_by_css_selector(
                'td')[-1].text
            data_devolucao = datetime.strptime(
                data_devolucao_str.strip(), '%d/%m/%y').date()

            if data_devolucao == hoje or RENOVAR_SEMPRE:
                renovar = True
                livro.find_element_by_tag_name('input').click()

        if renovar or RENOVAR_SEMPRE:
            firefox.find_element_by_link_text(
                'Renovar itens selecionados').click()
            firefox.implicitly_wait(30)
            WebDriverWait(
                firefox, 60).until(
                EC.visibility_of_element_located((By.ID, 'mainFrame')))
            logging.info("Renovado.")
    except Exception, err:
        error_message = "Erro ao renovar."
        print error_message
        logging.exception(error_message)
        raise


config_dict = load_config()
try:
    email = config_dict['email']
    senha = str(config_dict['senha'])[:TAM_SENHA]
except Exception, err:
    error_message = "Arquivo de configuração mal-formatado."
    print error_message
    logging.exception(error_message)
    raise
lastrun = config_dict.get('lastrun')
if lastrun == date.today() and not RODAR_SEMPRE:
    exit()

rodar_sempre = config_dict.get("rodar_sempre")
renovar_sempre = config_dict.get("renovar_sempre")
if rodar_sempre is not None:
    RODAR_SEMPRE = rodar_sempre
if renovar_sempre is not None:
    RENOVAR_SEMPRE = renovar_sempre

try:
    if SEM_CABECA:
        display = Display(visible=0, size=(800, 600))
        display.start()
    firefox = webdriver.Firefox(executable_path=GECKO_PATH)
except WebDriverException, err:
    error_message = "Geckodriver não encontrado."
    print error_message
    logging.exception(error_message)
    raise
login(email, senha, firefox)
renova(firefox)
firefox.close()
config_dict['lastrun'] = date.today()
write_config(config_dict)
