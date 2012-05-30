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

tweet = form["tweet"].value #cogemos el valor recibido del formulario

data = {'status':tweet} #cogemos el valor recibido del formulario

request_url = 'https://api.twitter.com/1/statuses/update.xml'

resp, content = client.request(request_url, 'POST', urllib.urlencode(data)) #Hacemos la peticion


#print que nos sirve para redirigir la pagina
print ''' 
<html>
<head>
<title>Introduccion pin</title>
<meta http-equiv="refresh" content="0; url=http://localhost/timelime.html">
</head>
<body>
</body>
</html>
'''
