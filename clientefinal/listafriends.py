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

screen_name = config.access_token['screen_name'] #guardamos el screen_name

request_url = 'https://api.twitter.com/1/friends/ids.xml?cursor=-1&screen_name=%s' 

resp, content = client.request(request_url % screen_name, 'GET') #hacemos la peticion

resp_xml = etree.fromstring(content)


ids = resp_xml.xpath("/id_list/ids/id/text()")

request_urlnames = 'https://api.twitter.com/1/friendships/lookup.xml?user_id=%s '

nombre = ids[0]

for i in ids:
    nombre = nombre +','+i

resp, content = client.request(request_urlnames % nombre, 'GET')

resp_xml = etree.fromstring(content)

names = resp_xml.xpath("/relationships/relationship/screen_name/text()")

f = open('/var/www/listaamigos.html','w')

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

for i in names: #guardamos en <p> los nombres

    f.write('<p>%s</p>' % unicode(i).encode("utf-8", "replace"))




final = '''
</div>
<div id="botones">
<form  method="POST" action="cgi-bin/home.py">
<p><input type="submit" value="Volver al home"/></p>
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
<meta http-equiv="refresh" content="0; url=http://localhost/listaamigos.html">
</head>
<body>
</body>
</html>
'''


