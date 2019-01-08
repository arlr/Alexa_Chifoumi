from random import *

item_list = ["pierre", "feuille", "ciseaux" ]

def regle(Alexa , Player):
    #Alexa Win
    print("Fonction regle")
    if (((str(Alexa) == "pierre") and (str(Player) == "ciseau")) or ((str(Alexa) == "feuille") and (str(Player) == "pierre")) or ((str(Alexa) == "ciseaux") and (str(Player) == "feuille"))):
        text = "Alexa à gagnée"
        #return(text)
    else:
        text = "Vous avez gagné"
    return(text)

def In_game(Item):
    print("Fonction In_game")
    AlexaItem = item_list[randint(0,2)]
    alexaText ="Alexa : " + AlexaItem
    print(alexaText)
    joueurText = "Joueur : " + Item
    print(joueurText)

    if str(AlexaItem) == str(Item):
        phrase = "J'ai choisi " + Item +" aussi nous avons donc fais égalité"
        return(phrase)
    else:
        phrase = regle(AlexaItem, Item)
        return(phrase) 


if __name__ == '__main__':
    
    itemJoueur = input("Entree pierre, ciseaux ou feuille : ")
    text  = In_game(itemJoueur)
    print(text)