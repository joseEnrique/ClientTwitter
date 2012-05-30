#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oauth2 as oauth
import urlparse
import urllib


consumer_key = 'WoVDyNwvaeJIUzJ7IPo2Q'#raw_input('Consumer key? ')
consumer_secret = 'BljnBxfEi4sRFS35OVAtee861pi9i1EmAQVjfWQ59ZA'#raw_input('Consumer secret? ')

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

consumer = oauth.Consumer(consumer_key, consumer_secret)

client = oauth.Client(consumer)#creamos el objeto client con el consumer

resp, content = client.request(request_token_url, "GET")#hacemos un get para sacar un token temporal que nos permitira autentificar

request_token = dict(urlparse.parse_qsl(content))#metemos la cadena de content en un diccionario

print 'Ve a la siguiente url:'
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token']) #redirigimos al usuarios a la url para que pueda cojer el pin

pin = raw_input('Introduce tu pin:  ')

token = oauth.Token(request_token['oauth_token'],request_token['oauth_token_secret'])#creamos el objeto token con el oauth_token y el oauth_token_secret

token.set_verifier(pin)

client = oauth.Client(consumer, token) #actualizamos el objeto client aniadiendole token

resp, content = client.request(access_token_url, "POST")#hacemos una peticion post para obtener token de acceso

access_token = dict(urlparse.parse_qsl(content))#aniadimos el contenido al diccionario


f = open('config.py','w')
f.write('access_token = %s\n' % repr(access_token))
f.close()


print '\n\nconfig.py Escrito\n'





    
















