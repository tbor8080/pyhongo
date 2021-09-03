# /usr/bin/env python
# -*- coding: utf-8 -*-

from py.webconfig import *
from sqlite import *
from threading import Thread
import json

####################################################################################################
# change at variable:doc_root etc...
####################################################################################################
# + Web Application: DOCUMENT_ROOT
doc_root='./first_flask_app'

# + WebApplication Title:
web_title='Automatic Create WebApp'

# + Python&Template File Name
# For Python
PyFile='main.py'

# For HTML Template (by Bootstrap)
TmplFile='main.html'

# + for database: type is sqlite or postgres sql(pgsql | psql)
#   - User Account: password is None OK.(but database security is no good, a lot of risk.)
#   - DatabaseUser=('<username>','<password>') or DatabaseUser=('<username>',None) or DatabaseUser=('<username>','')
#   - <password> is more than 8 charactors.
DatabaseUser=('ryohei',None)
# Database Type is sqlite or pgsql or psql.
# DatabaseType='sqlite' or DatabaseType='psql' or DatabaseType='pgsql'
# mysql is not type.
DatabaseType='pgsql'
# Database Name is Your database
DatabaseName='test'

# + Flask : Routing List Example.(Tuple List)
FlaskRouting=(
    {'path':'/', 'function':'index', 'code':'hello="Hello."'},
    {'path':'/main', 'function':'main'},
    {'path':'/test', 'function':'test'},
)

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
#   - $ python installer.py [press enter key]
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
    # For SQLite Example
    # Instanse.config(database=DatabaseType,dbname=DatabaseName,document_root=doc_root)
    # For PostgreSQL
    Instanse.config(database=DatabaseType,dbname=DatabaseName,user=DatabaseUser,document_root=doc_root)
    # Non Database Config Example
    # Instanse.config(document_root=doc_root)
    
    (db,app)=Instanse.db(),Instanse.app()
    
    app.setPyFile(PyFile)
    app.setTmplFile(TmplFile)
    
    app.setPort(5000)

    # Set Routing for Flask
    for i in range(len(FlaskRouting)):
        app.setRoute(FlaskRouting[i])
    
    # Web Application Title
    app.setTitle(web_title)
    
    # Install to <document_root> in Files
    if os.path.exists(app.getPyFile()) is not True and app.switch_to('install',__switch__['install']):
        app.install()
    else:
        error_message=f"""
++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Install Directory: {app.getInstallDir()} is exists.
+ Skip to app.install()
++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Would like to delete the directory?
+ Directory delete, warning.
+ $ rm -rf {app.getInstallDir()}
+
++++++++++++++++++++++++++++++++++++++++++++++++++++"""

        print(error_message)
        # debug code:

        json_file=app.getInstallDir()+'/manage/config.json'
        app.setJsonFile(json_file)

        app.setGunicornFile('gunicorn_start')
        app.setGunicorn()
        # print(db.getType())
        # app.appConfig()
        
        # print(app.getJsonFile())
        # print(app.loadJson(app.getJsonFile()))

    # Automation WSGI Run Script
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

# debug script

def forDebug():
    Instanse=WebAppConfig()
    print(Instanse.getMethod(SelectSQLite3))

    classname=['WebAppConfig','SelectSQLite3']
    for clsname in classname:
        Instanse.getInherit(eval(clsname))

if __name__=='__main__':
    main()    
