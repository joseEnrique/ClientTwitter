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

resp, content = client.request(request_urlhome, 'GET')

idusuario = config.access_token['user_id']

resp_xml = etree.fromstring(content)

request_url = 'http://api.twitter.com/1/statuses/retweet/%s.xml'

ids= resp_xml.xpath("/statuses/status/user[id!='%s']/../id/text()" % idusuario)

retw = form["retweet"].value

retw = int(retw)

eleccion = ids[retw]


resp, content = client.request(request_url % eleccion, 'POST') #hacemos un post con la id del tweet


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

