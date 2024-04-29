from selenium import webdriver #pegar o navegador
from selenium.webdriver.common.by import By #pegar o By para selecionar campos em um site
from time import sleep
import PySimpleGUI as sg

sg.theme('reddit')
layout=[
    [sg.Text('Matricula'), sg.Input(key = 'Matricula')],
    [sg.Text('Senha do SUAP'), sg.Input(key = 'Senha')],
    [sg.Button('Salvar')]
]

janela = sg.Window('Buscador de Notas do SUAP', layout= layout)

while True:
    evento, infomacoes = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    elif evento == 'Salvar':
        matricula_usuario = infomacoes['Matricula']
        senha_usuario = infomacoes['Senha']
        break

#abrindo o site do if 
driver= webdriver.Chrome()
driver.get('https://www.ifpb.edu.br/ti/acesso-a-sistemas')
sleep(4)

#indo para a pagina so SUAP
suap = driver.find_element(By.XPATH, "//img[@title='SUAP']")
sleep(1)
suap.click()
sleep(5)

#mudando a url em que estão sendo buscados os elementos para a nova aba que abriu(a da sequencia)
driver.switch_to.window(driver.window_handles[1])
#colocar matricula e senha digitadas pelo usuario no simplegui
driver.find_element(By.ID, 'id_username').send_keys(matricula_usuario)
sleep(1)


driver.find_element(By.ID, 'id_password').send_keys(senha_usuario)
sleep(1)

botao_entrar_suap = driver.find_element(By.XPATH, "//input[@value='Acessar']")
botao_entrar_suap.click()
sleep(15)

#mudando a url em que estão sendo buscados os elementos para a nova aba que abriu(a da sequencia)
driver.switch_to.window(driver.window_handles[1])
meus_dados = driver.find_element(By.XPATH, f"//a[@href='/edu/aluno/{matricula_usuario}/']")
meus_dados.click()
sleep(2)

boletim = driver.find_element(By.XPATH, "//a[@data-tab='boletim']")
boletim.click()
sleep(14)

#mudando a url em que estão sendo buscados os elementos para a nova aba que abriu(a da sequencia)
driver.switch_to.window(driver.window_handles[1])
emitir_boletim = driver.find_element(By.XPATH, "//a[@class='btn success']")
emitir_boletim.click()
sleep(4)