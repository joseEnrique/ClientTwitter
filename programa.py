#!/usr/bin/env python

import oauth2 as oauth
import urllib
import urlparse


consumer_key = 'WoVDyNwvaeJIUzJ7IPo2Q'#raw_input('Consumer key? ')
consumer_secret = 'BljnBxfEi4sRFS35OVAtee861pi9i1EmAQVjfWQ59ZA'#raw_input('Consumer secret? ')

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

consumer = oauth.Consumer(consumer_key, consumer_secret)

#creamos el objeto client con el consumer

client = oauth.Client(consumer)

#hacemos un get para sacar un token temporal que nos permitira autentificar

resp, content = client.request(request_token_url, "GET")

#metemos la cadena de content en un diccionario

request_token = dict(urlparse.parse_qsl(content))

#redirigimos al usuarios a la url para que pueda cojer el pin

print 'Ve a la siguiente url:'
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])


pin = raw_input('Introduce tu pin:  ')

#creamos el objeto token con el oauth_token y el oauth_token_secret

token = oauth.Token(request_token['oauth_token'],request_token['oauth_token_secret'])

token.set_verifier(pin)

#actualizamos el elemento client añadiendole token

client = oauth.Client(consumer, token)

#hacemos una peticion post para obtener token de acceso

resp, content = client.request(access_token_url, "POST")

#añadimos el contenido al diccionario

access_token = dict(urlparse.parse_qsl(content))

#actualizamos el objeto token con los token de acceso

token = oauth.Token(access_token['oauth_token'],access_token['oauth_token_secret'])

#actualizamos el objeto client con los nuevos token

client = oauth.Client(consumer, token)

request_uri = 'https://api.twitter.com/1/statuses/update.xml'

data = {'status': raw_input("What's happening? ")}

#hacemos una peticion post para publicar un tweet

resp, content = client.request(request_uri, 'POST', urllib.urlencode(data))

funcio = resp.status

print funcio



