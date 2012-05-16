#!/usr/bin/python
import cgi
import cgitb
import requests
from lxml import etree
cgitb.enable() #inicializamos la biblioteca
print "Content-Type: text/html"     
print                               
form = cgi.FieldStorage() # con esto cargamos los datos del formulario
print "<p>name:", form["user"].value # imprimimos por pantalla el dato user que hemos introducido y se ha guardado en el diccionario 
print "<p>contrasena:", form["pass"].value # igual que user
    



