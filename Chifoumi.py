#!/sys/bin/env python3

from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/Chifoumi')

@ask.launch
def start_skill():
    welcome_message = "Bonjour dite moi quand vous êtes prêts"  #Message que vas dire Alexa
    return statement(welcome_message)

@ask.intent('StartIntent')
def start():
    text = "D'accord tenez vous prêts ...   3 , 2 , 1.  Chiii Fou Mii."
    return statement(text)

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True)