import pyautogui as saure
import flet as ft
from time import sleep
from random import randint
import pyperclip as cola

saure.PAUSE = 0.5
#abrir o chrome
#entrar no sistema
#logar no sistema
#criar um novo funcionário
#Criar a senha do atendente
#Entrar no pdv e sincronizar os dados

def main(atendente):
    
    def automatizar(event):
        saure.press("win")
        saure.write("chrome")
        saure.press("enter")
        saure.press("enter")       
        sleep(3)
        saure.click(x=242, y=66)
        saure.write("https://rotta34oficial.marketup.com/index.html#/login")
        saure.press("enter")
        sleep(4)#espera 4 segundos após entrar na página de login
        saure.click(x=148, y=516)#Clica no botão de login
        sleep(15)#espera 12 segundos após entrar no sistema
        saure.click(x=1316, y=142)#fecha o anúncio
        saure.click(x=1243, y=155)#Clica na engrenagem
        saure.click(x=1184, y=217)#Clica na opção empresa
        saure.click(x=1156, y=321)#Clica na opção usuários
        sleep(7)
        saure.scroll(-50000)
        saure.click(x=863, y=613)
        saure.click(x=251, y=379)
        nome_maiusculo = att.value.upper()
        saure.write(nome_maiusculo)#escreve o nome do atendente
        saure.press("tab")
        nome_minusculo = att.value.lower()#transforma o nome em minúsculo para usar no email e no login
        saure.write(f"{nome_minusculo}@gmail.com")#escreve um email fictício
        
        for i in range(0,2):
            saure.press("tab")
        
        for i in range(0,7):
            saure.press("down")
            
        saure.click(x=477, y=432)
        saure.click(x=645, y=428)
        saure.click(x=786, y=429)
        saure.click(x=904, y=429)
        saure.click(x=494, y=490)
        
        saure.write(att.value)
        saure.press("tab")
        senha = f"{att.value}@2024"#senha do atendente
        senha_string = ft.Text(f"Senha do login: {senha}")#transforma o conteúdo da senha em um texto exibível
        saure.write(senha)
        login = ft.Text(f"Login: {nome_minusculo}")
        atendente.add(login)
        atendente.add(senha_string)#Exibe a senha do atendente a tela
        saure.click(x=882, y=523)
        sleep(3)
        
        #seguda parte
        saure.click(x=1180, y=369)
        saure.click(x=919, y=305)#clica em ok
        saure.click(x=919, y=305)#clica em ok
        sleep(2)
        saure.click(x=1299, y=193)#clica em mais configurações
        saure.click(x=1296, y=289)#clica em restaurantes
        saure.click(x=1162, y=274)#clica em dados gerais
        sleep(10)
        #saure.click(x=1318, y=147)
        saure.scroll(-400)
        saure.click(x=589, y=548)
        saure.click(x=631, y=576)
        saure.press("tab")
        saure.write(n_aleatorio_txt)
        saure.doubleClick(x=804, y=541)
        sleep(2)
        saure.hotkey("ctrl","c")
        senha_atendente = cola.paste()
        saure.click(x=912, y=542)
        sleep(3)
        saure.scroll(-5000000)
        saure.click(x=868, y=617)
        sleep(3)
        saure.click(x=909, y=296)#clica em ok
        sleep(5)
        saure.click(x=217, y=138)
        saure.click(x=119, y=187)
        
        sleep(4)
        saure.click(x=32, y=481)
        saure.click(x=553, y=552)
        
        txt_senha_att = ft.Text(f"Senha do atendente: {senha_atendente}")
        atendente.add(txt_senha_att)
        print(n_ocupados)
    
    att = ft.TextField(label="Nome do(a) atendente ")
    botão_att = ft.ElevatedButton("Enviar",on_click=automatizar)
    n_ocupados = [1,2,4,5,6,7,9,15,23,24,25,27,28,29,36]
    n_aleatorio = randint(41,130)
    n_aleatorio_txt = str(n_aleatorio)
    
    while n_aleatorio in n_ocupados:
        if n_aleatorio in n_ocupados:
            n_aleatorio = randint(41,130)
            n_aleatorio_txt = str(n_aleatorio)
        else:
            n_ocupados.append(n_aleatorio)
    
    atendente.add(att)
    atendente.add(botão_att)
ft.app(target=main)    