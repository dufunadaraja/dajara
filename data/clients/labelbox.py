import json
import requests
from graphqlclient import GraphQLClient


def client():
	req = requests.get("https://storage.googleapis.com/daraja-storage/keys.json")
	keys = json.loads(req.text)
	api_key = keys['labelbox']
	client = GraphQLClient('https://api.labelbox.com/graphql')
	client.inject_token('Bearer {}'.format(api_key))
	return client