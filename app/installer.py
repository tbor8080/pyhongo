# /usr/bin/env python
# -*- coding: utf-8 -*-

from py.webconfig import *
from sqlite import *

####################################################################################################
# global variable
####################################################################################################
doc_root='./first_flask_app'


####################################################################################################
# installer.py: Function
####################################################################################################
# Database Setting
def createTable(db):
    database=db.getDatabaseName()

    # Create Table Code
    db.setTableName('COMMODITY_LIST2')
    db.appendColumn(columnname='xxxx_id',datatype='INTEGER',const='NOT NULL',primarykey=('xxxx_id',True),unique=False)
    db.appendColumn(columnname='document_sample_name',datatype='TEXT')
    db.appendColumn(columnname='regist_date',datatype='DATE')

    # db.show(db.getCreateTableCode())

# Installer main:config
def main():
    # Framework Class
    Instanse=WebAppConfig()
    # SQLite Config Example
    # Instanse.config(database='sqlite',dbname='sample.db',document_root='./doc_root')
    # Not Database Config Example
    Instanse.config(document_root=doc_root)
    
    (db,app)=Instanse.db(),Instanse.app()
    # createTable(db)
    # Python&Template File Name
    (PyFile,TmplFile)=('main.py','main.html')

    app.setPyFile(PyFile)
    app.setTmplFile(TmplFile)
    
    app.setPort(8080)

    # Append Flask Routing
    app.setRoute({'path':'/', 'function':'index'})
    app.setRoute({'path':'/main', 'function':'main'})
    app.setRoute({'path':'/test', 'function':'test'})
    
    # Web Application Title
    app.setTitle('Automatic Create WebApp')
    
    # Install to <document_root> in Files
    app.install()

    # Automation WSGI Run Script
    # Look at Your Set Host & Port Number!!
    app.run()
    return app,db

# debug script

def forDebug():
    Instanse=WebAppConfig()
    print(Instanse.getMethod(SelectSQLite3))

    classname=['WebAppConfig','SelectSQLite3']
    for clsname in classname:
        Instanse.getInherit(eval(clsname))

if __name__=='__main__':
    (app,db)=main()
    # main()
    # print(app)
    # gui_main(app)
    # forDebug()
    
    
