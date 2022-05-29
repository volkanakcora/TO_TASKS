from http import server
from __init__ import web_app 
import os 

entrance = web_app()
application = entrance.server
os.chdir('./')

def main():
    application.run()
    
if __name__  ==  "__main__":
    application.run()
