from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd

#creating chat bot object with name Assistance
bot=ChatBot("Assistence",    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.SpecificResponseAdapter",
    ])
# Creazione del trainer e addestramento del bot
trainer=ListTrainer(bot)

trainer.train([
    "Ciao",
    "Cosa posso memorizzare per te?",
    "Hai bisogno di altro?",
    "Fatto",
    "Prego",
    "Di niente",
    "Aggiungi un evento al calendario",
    "Vuoi che memorizzi un evento sul calendario?",
    "Qual è la data dell'evento?",
    "Qual è l'ora dell'evento?",
    "L'evento è stato memorizzato correttamente.",
    "Hai bisogno di altro?", 
    "Cosa devo eliminare?",
    "Cosa devo rimuovere?",
    "Cosa devo rinominare?",
    "Cosa devo cambiare?" ,
    "L'evento è stato rinominato corretamente",
    "L'evento è stato rimosso correttamnete",
    "L'vento è stato cancellato correttamento",
    "Si",
    "Posso fare altro per te?",
    "Data del evento:",
    "Ora dell'evento:",
    "Vuoi altro?",
    "Ti serve aiuto per memorizzare qualcosa?",
    "Ti serve aiuto per rinominare qualcosa?",
    "Ti serve aiuto per cancellare qualcosa?",
])
#funzione per frase inizo conversazione
def phrase_start():
    start=("Ciao sono Assistence, l'assistente virtuale che ti aiuta a gestire al meglio il tuo calendario. Come ti posso aiutare? ")
    return start

def response(user_input):
    #frasi da utilizzare nel dialogo
    response = bot.get_response(user_input)
    return response

