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
Links_Trabajo =[]

url= "https://co.computrabajo.com/trabajo-de-analista-de-datos-en-bogota-dc-ciudad"
url_bucle = url+'?p=2'

def Scrap_Trabajos(url):
    page.goto(url)
    page.expect_request_finished
    soup = bs4.BeautifulSoup(page.content(), 'html.parser')
    #se toma todas las propuestas de la pagina
    prop = soup.find_all('article', class_='box_offer')

    #se evalua una por una la informacion
    for p in prop:
        #nombre del trabajo
        nom_t = p.find('a', class_='js-o-link fc_base')
        Nombre_Trabajo.append(nom_t.text.strip())
        #nombre de la empresa ( no siempre esta disponible)
        try:
            nom_e = p.find('a', class_='fc_base t_ellipsis')
            Nombre_Empresa.append(nom_e.text.strip())
        except:
            Nombre_Empresa.append('No disponible - Importante empresa del sector')
        #ciudad
        try:
            ubi = p.find('span', class_='mr10')
            Ubicacion.append(ubi.text.strip()) 
        except:
            Ubicacion.append('No disponible')
        #fecha de publicacion
        try:   
            fecha = p.find('p', class_='fs13 fc_aux mt15')
            Fecha_Publicacion.append(fecha.text.strip())
        except:
            Fecha_Publicacion.append('No disponible')
        #salario
        try:
            sal = p.find('span', class_='dIB mr10')  
            Salario_Trabajo.append(sal.text.strip())
        except:
            Salario_Trabajo.append('No disponible')
        #link del trabajo
        try:
            link = p.find('a', class_='js-o-link fc_base')
            Links_Trabajo.append(url_semilla + link['href'])
        except:
            Links_Trabajo.append('No disponible')

#Idea es aplicar y enviar la hoja de vida de los trabajos nuevos automaticamente
#si se cumplen las condiciones de: salario, nombre del cargo.
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    Scrap_Trabajos(url)
    for i in range(2,11):
        url_pagina = url+'?p='+str(i)
        Scrap_Trabajos(url_pagina)

    browser.close()


df = pd.DataFrame({'Nombre_Trabajo':Nombre_Trabajo,
                   'Nombre_Empresa':Nombre_Empresa,
                   'Ubicacion':Ubicacion,
                   'Fecha_Publicacion':Fecha_Publicacion,
                   'Salario_Trabajo':Salario_Trabajo,
                   'Link_Trabajo':Links_Trabajo
                   })
df.to_excel('./CompuTrabajo.xlsx', index=False)

#print(Nombre_Trabajo)
print(len(Nombre_Trabajo),len(Nombre_Empresa),len(Ubicacion),len(Fecha_Publicacion),len(Salario_Trabajo))
