from flask import Flask
from threading import Thread
from flask_restful import Resource, Api
import random
import json

app = Flask('')
api = Api(app)


def getFacts(factType):
	if factType == "random":
		fileAddress = 'Facts/random.json'
	elif factType == "technology":
		fileAddress = 'Facts/technology.json'
	else:
		fileAddress = 'errormsg.json'
	with open(fileAddress, 'r') as factfile:
		data = json.load(factfile)
	fact = random.choice(list(data['Facts']))
	return fact


def getQuotes(quoteType):
	if quoteType == "motivation":
		fileAddress = 'Quotes/motivation.json'
	elif quoteType == "funny":
		fileAddress = 'Quotes/funny.json'
	else:
		fileAddress = 'errormsg.json'
	with open(fileAddress, 'r') as quotefile:
		data = json.load(quotefile)
	quote = random.choice(list(data['Quotes']))
	return quote


class Facts(Resource):

	def get(self, factType):
		return getFacts(factType)


class Quotes(Resource):

	def get(self, quoteType):
		return getQuotes(quoteType)


class Test(Resource):

	def get(self):
		return "Example with Flask-Restful"


#creating api endpoint
api.add_resource(Facts, '/api/facts/<string:factType>')
api.add_resource(Quotes, '/api/quotes/<string:quoteType>')
api.add_resource(Test, '/api/restful')


def run():
	app.run(host='0.0.0.0', port=7210)


t = Thread(target=run)
t.start()
