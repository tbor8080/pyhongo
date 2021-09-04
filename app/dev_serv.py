from py.webconfig import *
from sqlite import *
from threading import Thread
import json,subprocess

json_file='./first_flask_app/manage/config.json'

def main():

    Instanse=WebAppConfig()
    Instanse.set_config(json_file)
    config=Instanse.get_config()
    # print(Instanse.is_config())
    dir=config["doc_root"]
    Instanse.config(document_root=dir)

    (app,db)=Instanse.app(),Instanse.db()
    
    app.setInstallDir(dir)
    app.setPyFile('main.py')
    app.setPort(config["port"])
    app.setHost(config["host"])
    
    Thread(target=app.browse).start()
    Thread(target=app.run).start()
    gui_main(app,db)

if __name__=='__main__':    
    main()
