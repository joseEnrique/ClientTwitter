import requests
from lxml import etree
import oauth2


consumer = oauth.Consumer(key="your-twitter-consumer-key", 
                          secret="your-twitter-consumer-secret")


request_token_url = "http://twitter.com/oauth/request_token"

cliente = oauth.Client(consumer)

resp, content = client.request(request_token_url, "GET")


print resp
print content



