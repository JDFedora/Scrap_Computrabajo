import requests
import bs4
import re
import pandas as pd


url_semilla ="https://co.computrabajo.com/"

Nombre_Trabajo =[]
Nombre_Empresa =[]
Ubicacion =[]
Fecha_Publicacion =[]
Descripcion_Trabajo =[]
Salario_Trabajo =[]

#Idea es aplicar y enviar la hoja de vida de los trabajos nuevos automaticamente
#si se cumplen las condiciones de: salario, nombre del cargo.
