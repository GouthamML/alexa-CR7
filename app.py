from flask import Flask,request
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
import random

app = Flask(__name__)
ask = Ask(app, "/fact")

@app.route('/')
def homepage():
    return 'hello world skill running perfectly fine :)'

def getNews():
    news = requests.get('https://facts-response.herokuapp.com/getNews').content
    news = json.loads(news)
    print random.choice(news)
    return random.choice(news)


@ask.launch
def launch():
    fact = getNews()
    response = fact + '...........Do you want more?'
    return question(response)


@ask.intent('YesIntent')
def yesIntent():
    fact = getNews()
    response = fact + '...........Do you want more?'
    return question(response)

@ask.intent('NoIntent')
def noIntent():
    response = 'Okay...hmmm...Bye'
    return statement(response)

@ask.intent('AMAZON.HelpIntent')
def help():
    response = 'This skill tell you facts about christmas!'
    return question(response)

if __name__ =='__main__':
    app.run(debug=True)