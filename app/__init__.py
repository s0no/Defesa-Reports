from app.controller.cptec.make import make as cptec
from app.controller.covid.make import make as covid
from app.controller.alerts import alerts
from app.controller.bot.chat import chat
import threading

#threads = [threading.Thread(target=cptec), threading.Thread(target=covid)]

def run(): 
    #alerts()
    #covid()
    #cptec()
    chat()
    #for thread in threads:
    #    thread.start() 
    
    return None
    