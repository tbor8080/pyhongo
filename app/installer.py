# /usr/bin/env python
# -*- coding: utf-8 -*-

from py.webconfig import *
from gui import *
from cui import *

from threading import Thread
import json
from time import sleep


print('wait',end='')
sleep(1)

try:
    from app import *
except:
    print('Module File NotFound')
    print('% python -m installer')
    exit()

####################################################################################################
####################################################################################################
# + Swtich To Installer.py: 
__switch__={
    "install":True,
    "flask":True,
    "gunicorn":False,
    "database":(True,'sqlite'),
    "browser":(True,'chrome')
}

# + save as installer.py, run the python script.(terminal,bash|zsh)
#   - install directory chmod 755 <directory> 
#   - $ python -m installer [press enter key]
#   - start install ... please wait ... for a littie bit. 

####################################################################################################
# installer.py: Function
####################################################################################################
# Database Setting
def createTable(db):
    database=db.getDatabaseName()

    # Create Table
    db.setTableName('COMMODITY_LIST2')
    db.appendColumn(columnname='xxxx_id',datatype='INTEGER',const='NOT NULL',primarykey=('xxxx_id',True),unique=False)
    db.appendColumn(columnname='document_sample_name',datatype='TEXT')
    db.appendColumn(columnname='regist_date',datatype='DATE')

    db.show(db.getCreateTableCode())

# Installer main:config
def main():
    # Framework: Create WebApp:
    Instanse=WebAppConfig()
    # config json
    Instanse.set_config(f'{doc_root}/manage/config.json')
    # For SQLite Example
    if DatabaseType=='sqlite':
        Instanse.config(database=DatabaseType,dbname=DatabaseName,document_root=doc_root)
    # For PostgreSQL
    if DatabaseType=='pgsql' or DatabaseType=='psql':
        # For PostgreSQL (Custom Host & Port)
        Instanse.config(database=DatabaseType,dbname=DatabaseName,user=DatabaseUser,document_root=doc_root,host=DatabaseHost,port=DatabasePort,)
    if DatabaseType is None:
    # Non Database Config Example
        Instanse.config(document_root=doc_root)

    (db,app)=Instanse.db(),Instanse.app()
    
    app.setPyFile(PyFile)
    app.setTmplFile(TmplFile)
    
    app.setPort(5000)

    # Set Routing for Flask
    for i in range(len(FlaskRouting)):
        app.setRoute(FlaskRouting[i])
    
    # Web Application Title
    app.setTitle(web_title)
    
    # Install to <document_root> in Files(main.py)
    if isMainFile(app.getPyFile(),app) is False and app.switch_to('install',__switch__['install']):
        app.install()
    else:
        error_message=f"""
####################################################
* Finish This program.
++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Install Directory: {app.getInstallDir()} is exists.
+ or __switch__['install'] is False.
+ Skip to app.install()
++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Would like to delete the directory?
+ Directory delete.
+ % ./remove_sample
++++++++++++++++++++++++++++++++++++++++++++++++++++
####################################################"""
        print(error_message)
        # exit()

    # Automatic WSGI Start Run Script
    # Look at Your Set Host & Port Number!!
    # And stay a little time, webdriver(chrome) run! (auto browse host (& port))
    
    # Look at __switch__ variable True or False
    if app.switch_to('gunicorn',__switch__['gunicorn']):
        Thread(target=app.gunicorn_start).start()

    if app.switch_to('flask',__switch__['flask']):
        Thread(target=app.run).start()

    if app.switch_to('browser',__switch__['browser']):
        Thread(target=app.browse).start()
    
    # SQLite Explorer (GUI Application)
    if app.switch_to('sqlite',__switch__['database']):
        # create database table:
        # createTable(db)
        gui_main(app,db)

    # return for the GUI Application
    return app,db

def isMainFile(file=None,app=None):
    if file is not None and app is not None:
        return os.path.exists(app.getPyFile())

# debug script
def forDebug():
    Instanse=WebAppConfig()
    print(Instanse.getMethod(SelectSQLite3))

    classname=['WebAppConfig','SelectSQLite3','SelectPgSQL']
    for clsname in classname:
        Instanse.getInherit(eval(clsname))

if __name__=='__main__':
    if __switch__['install'] is False:
        exit()
    main()    
