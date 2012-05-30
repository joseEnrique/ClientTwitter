#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import oauth2 as oauth
from lxml import etree
import urlparse
import urllib
import config



cgitb.enable() #inicializamos la biblioteca
print "Content-Type: text/html"     
print                               
form = cgi.FieldStorage() # con esto cargamos los datos del formulario

consumer_key = 'WoVDyNwvaeJIUzJ7IPo2Q'#raw_input('Consumer key? ')
consumer_secret = 'BljnBxfEi4sRFS35OVAtee861pi9i1EmAQVjfWQ59ZA'#raw_input('Consumer secret? ')

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

consumer = oauth.Consumer(consumer_key, consumer_secret)

client = oauth.Client(consumer)#creamos el objeto client con el consumer

token = oauth.Token(config.access_token['oauth_token'],config.access_token['oauth_token_secret']) #creamos el objeto token con el oauth_token y el oauth_token_secret

client = oauth.Client(consumer, token) #actualizamos el objeto client aniadiendole token

request_urlhome = 'http://api.twitter.com/1/statuses/home_timeline.xml'

idusuario = config.access_token['user_id']


resp, content = client.request(request_urlhome, 'GET') #peticion get para obtener el time limne

resp_xml = etree.fromstring(content)

twits= resp_xml.xpath("/statuses/status/user[id!='%s']/../text/text()" %idusuario)

ids= resp_xml.xpath("/statuses/status/user[id!='%s']/../id/text()" % idusuario)

nombres = resp_xml.xpath("/statuses/status/user[id!='%s']/screen_name/text()" %idusuario)

fotos = resp_xml.xpath("/statuses/status/user[id!='%s']/profile_image_url/text()" % idusuario)


cont = 0

f = open('/var/www/listatweet.html','w')

cabeza = ''' 
<html>
<head>
<title>Cliente Twitter</title>
<link rel="stylesheet" type="text/css" href="css/estilo.css" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<div id="cabecera">
<div id="titulo">
<h1>Cliente twitter</h1>
</div>
</div>
<div id="container">
<div id="cuerpo">
'''

f.write(cabeza)

for i in twits:
    f.write( '<p><img src="%s" alt="desc" /> <br/> %s: %s: %s</p>\n' % (unicode(fotos[cont]).encode("utf-8", "replace"), cont ,unicode(nombres[cont]).encode("utf-8", "replace"),unicode(i).encode("utf-8", "replace")) ) 
    cont = cont + 1
    if cont > 7:
        break


final = '''
</div>
<div id="botones">
<form  method="POST" action="cgi-bin/retweet.py">
<p>Escribe el numero del tweet: <input type="text" name="retweet"/></p>
<p><input type="submit" value="Enviar"/></p>
</form>
</div>
</div>
</body>
</html>
'''

f.write(final)
f.close()

print ''' 
<html>
<head>
<title>Introduccion pin</title>
<meta http-equiv="refresh" content="0; url=http://localhost/listatweet.html">
</head>
<body>
</body>
</html>
'''

























