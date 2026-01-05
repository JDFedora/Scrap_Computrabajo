import requests
import bs4
from playwright.sync_api import sync_playwright
import re
import pandas as pd


url_semilla ="https://co.computrabajo.com/"

Nombre_Trabajo =[]
Nombre_Empresa =[]
Ubicacion =[]
Fecha_Publicacion =[]
Descripcion_Trabajo =[]
Salario_Trabajo =[]

url= "https://co.computrabajo.com/trabajo-de-analista-de-informacion-en-bogota-dc"

#Idea es aplicar y enviar la hoja de vida de los trabajos nuevos automaticamente
#si se cumplen las condiciones de: salario, nombre del cargo.
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.expect_request_finished
    soup = bs4.BeautifulSoup(page.content(), 'html.parser')
    trabajos = soup.find_all('a', class_='js-o-link fc_base')
    
    for trabajo in trabajos:
        Nombre_Trabajo.append(trabajo.text.strip())

    browser.close()




print(Nombre_Trabajo)
print(len(Nombre_Trabajo))