#!/sys/bin/env python3

from flask import Flask, render_template
from flask_ask import Ask, statement, question
from random import *

app = Flask(__name__)
ask = Ask(app, '/Chifoumi')

item_list = ["pierre", "feuille", "ciseaux" ]

def regle(Alexa , Player):
    #Alexa Win
    print("Fonction regle")
    if (((str(Alexa) == "pierre") and (str(Player) == "ciseau")) or ((str(Alexa) == "feuille") and (str(Player) == "pierre")) or ((str(Alexa) == "ciseaux") and (str(Player) == "feuille"))):
        text = "Alexa à gagnée"
        #return(text)
    else:
        text = "Vous avez gagné"

    text = text + "1"    
    print(text)
    return(text)

@ask.launch
def start_skill():
    welcome_message = "Bonjour, voulez-vous que je sois le maître du jeu ou que je joue avec vous ?"  #Message que vas dire Alexa
    return question(welcome_message)

#@ask.intent('ChoixIntent')
#def Choix():
#    phrase = "D'accord. Dite moi quand vous êtes prêts ?"
#    return question(phrase)

@ask.intent('MDJ_StartIntent')
def MDJ_start():
    phrase = "D'accord c'est parti  .......   3 ...., 2 ..., 1....  Chiii Fou My !!!!"
    return statement(phrase)

@ask.intent('JeuxIntent')
def Jeux_Start():
    phrase = "D'accord c'est parti, dite moi ce que vous avez choisi ?"
    return question(phrase)

@ask.intent('ItemIntentt')
def In_game(Item):
    print("Fonction In_game")
    AlexaItem = item_list[randint(0,2)]
    alexaText ="Alexa : " + AlexaItem
    print(alexaText)
    joueurText = "Joueur : " + Item
    print(joueurText)

    if (str(AlexaItem) == str(Item)):
        
        phrase = "J'ai choisi " + Item +" aussi nous avons donc fais égalité"
        #return(phrase)
    else:
        phrase = regle(AlexaItem, Item)
    print(phrase)
    return statement(phrase) 




@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True)