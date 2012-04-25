import requests
from lxml import etree

nombre = raw_input("inserta el nombre de usuario: ") #para introducir nombre usuario

respuesta = requests.get("https://api.twitter.com/1/statuses/user_timeline.xml",params={"include_entities":"true","include_rts":"true","screen_name":nombre,
"count":"3" }) #una peticion con la api de twitter, donde count es el numero de twitts que nos dara

resp_xml = etree.fromstring(respuesta.content)

twits= resp_xml.xpath("/statuses/status/text/text()") # buscamos los twits
imagen = resp_xml.xpath("/statuses/status/user/profile_image_url/text()")# url de la imagen de perfil


raiz = etree.Element("html",attrib={"xmlns":"http://www.w3.org/1999/xhtml"}) #creamos la estructura

arbol = etree.ElementTree(raiz)

head = etree.SubElement(raiz,"head")
title = etree.SubElement(head,"title")
title.text = "Cliente twitter Python"
body = etree.SubElement(raiz,"body")

parrafo = etree.SubElement(body,"p")
imagen = etree.SubElement(parrafo,"img",attrib={"src":imagen[0],"alt":"imagen de perfil","height":"42px","width":"42px"}) # la imagen de perfil (imagen[0]) que hace referencia al xpath de la url
imagen.tail = nombre #el nombre de usuario

for i in twits: #bucle para recorrer y poner los twits
    parrafo = etree.SubElement(body,"p")
    parrafo.text =i

salida = open("prueba.html","w")


salida.write(etree.tostring(arbol,pretty_print=True)) #pegamos todo en un html
    








    
