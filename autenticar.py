import requests
from lxml import etree
import oauth2

consumer_key = 'llave que te da twitter'
consumer_secret = 'secret que te da twitter'

request_token_url = 'http://twitter.com/oauth/request_token'
access_token_url = 'http://twitter.com/oauth/access_token'
authorize_url = 'http://twitter.com/oauth/authorize'

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)



resp, content = client.request(request_token_url, "GET")


request_token = dict(urlparse.parse_qsl(content))




accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Estas autorizando? (s/n) ')
    oauth_verifier = raw_input('Pon tu pin ')



token = oauth.Token(request_token['oauth_token'],
    request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))

