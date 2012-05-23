#!/usr/bin/python
import cgi
import cgitb
import oauth2 as oauth
from lxml import etree
import urlparse

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

resp, content = client.request(request_token_url, "GET")#hacemos un get para sacar un token temporal que nos permitira autentificar

request_token = dict(urlparse.parse_qsl(content))#metemos la cadena de content en un diccionario

print '<Ve a la siguiente url:'
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token']) #redirigimos al usuarios a la url para que pueda cojer el pin

print <html>
print <head>
print <title>Introduccion pin</title>
print </head>
print <body>
print <form name="formulario" method="post" action="cgi-bin/busqueda.py">
print <p>PIN: <input type="text" name="pin"/></p>
print <p><input type="submit" value="Enviar pin..."/></p>
print </form>
print </body>
print </html>









