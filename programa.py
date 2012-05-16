#!/usr/bin/env python

import oauth2 as oauth
import urllib
import urlparse
from lxml import etree


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

token = oauth.Token(access_token['oauth_token'],access_token['oauth_token_secret'])#actualizamos el objeto token con los token de acceso

client = oauth.Client(consumer, token)#actualizamos el objeto client con los nuevos token



while True:

    cont = 0
    print ' '
    print 'Menu'
    print '1) Ver timeline'
    print '2) Enviar un tweet'
    print '3) Hacer un retweet'
    print '4) Seguir a un user'
    print '5) Salir'
    print ' '

    elegir = raw_input('Elige una opcion: ') 

    if elegir == '1':

        request_url = 'http://api.twitter.com/1/statuses/home_timeline.xml'

        resp, content = client.request(request_url, 'GET')

        resp_xml = etree.fromstring(content)
        twits= resp_xml.xpath("/statuses/status/text/text()")

        for i in twits:
            print cont,i
            cont = cont+1


    if elegir == '2':

        request_url = 'https://api.twitter.com/1/statuses/update.xml'

        data = {'status': raw_input("Escribe el tweet: ")}

        resp, content = client.request(request_url, 'POST', urllib.urlencode(data)) #hacemos una peticion post para publicar un tweet

    if elegir == '3':

        request_url = 'http://api.twitter.com/1/statuses/retweet/%s.xml'
        request_urlhome = 'http://api.twitter.com/1/statuses/home_timeline.xml'

        resp, content = client.request(request_urlhome, 'GET')
        resp_xml = etree.fromstring(content)
        twits= resp_xml.xpath("/statuses/status/user[id!='562651916']/../text/text()")
        ids= resp_xml.xpath("/statuses/status/user[id!='562651916']/../id/text()")

        for i in twits:
            print cont,i
            cont = cont+1
        cual = input('Elige el tweet que quieres hacer retweet: ')

        ret = ids[cual]
        resp, content = client.request(request_url % ret, 'POST')
        print resp.status


    if elegir == '4':

        request_url = 'https://api.twitter.com/1/friendships/create.xml'
        data = {'screen_name': raw_input("Escribe el nombre:  ")}
        resp, content = client.request(request_url, 'POST', urllib.urlencode(data))        

        

    elif elegir == '5':
        break
            


















