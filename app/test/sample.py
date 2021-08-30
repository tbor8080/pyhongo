# /usr/bin/env python
# -*- coding: utf-8 -*-

from py.webconfig import *

# Case 1. SQL Class Test
def SQLSampleCode(db):

    # install script
    # 1. create db
    # 2. create table
    #       - sql code write
    
    db.setTableName('TEST1')
    
    dbconf=FileinFlask()
    # print(db.getTableName,db.getTable)
    dbconf.createDatabaseName('test.db')
    
    # dbconf.access('localhost','5043')

    # Table: COMMODITY_LIST =====================================
    dbconf.setTableName('COMMODITY_LIST')
    #print(dbconf.getTableName)
    # Column: COMMODITY_LIST ====================================
    dbconf.appendColumn('commodity_id','INTEGER','NOT NULL',('commodity_id',True))
    dbconf.appendColumn('company_id','INTEGER')
    dbconf.appendColumn('commodity_name','TEXT','NOT NULL')
    dbconf.appendColumn('commodity_maker','TEXT')
    dbconf.appendColumn('commodity_word','TEXT')
    dbconf.appendColumn('stock','INTEGER','NOT NULL')
    dbconf.appendColumn('remark','TEXT')
    # dbconf.createTable()
    
    # Table: COMMODITY_LIST2 =====================================
    dbconf.setTableName('COMMODITY_LIST2')
    # Column: COMMODITY_LIST2 ====================================
    dbconf.appendColumn('commodity2_id','INTEGER','NOT NULL',('commodity_id',False))
    dbconf.appendColumn('company_id','INTEGER')

    # Table: COMMODITY_LIST3 =====================================
    dbconf.setTableName('COMMODITY_LIST3')
    # Column: COMMODITY_LIST3 ====================================
    dbconf.appendColumn('commodity3_id','INTEGER','NOT NULL')
    dbconf.appendColumn('company_id','INTEGER')

    dbconf.setTableName('COMMODITY_LIST3')
    print(dbconf.selectCode())
    # SQL Preview
    dbconf.show(dbconf.getCreateDBCode())
    dbconf.show(dbconf.getCreateTableCode())
    # print(dbconf.getScheme())

    dbconf.setTableName('COMMODITY_LIST4')
    select=dbconf.selectCode(where={})
    print(select)
    # SELECT {col} from {tablename} [WHERE {where}];

# Case 2. Web App Class Test
def WebAppSampleCode(webapp):
    
    FlaskRoute=[
        {'path':'/', 'function':'index'},
        {'path':'/insert','function':'insert'}
    ]
    webapp.setRouteMulti(FlaskRoute)
    
    webapp.setRoute({'path':'/static', 'function':'static'})

    # print(webapp.route)
    webapp.setPyFile('main.py')
    webapp.setTitle('Automatic Create WebApp')
    webapp.setTmplFile('main.html')

    # Write all file code preview
    # webapp.getDoc()
    webapp.previewPy()
    # writing files: .py(1),.html(1),directory(templates, static/javascript, static/css, static/img)
    webapp.install()

    # print('Working Directory:', webapp.getPath())

    # Run the Python Code: python <python file>
    # webapp.run(webapp.getPyFile())

# Class Infomantion for Check ################################################
def ClassDocument(config,app,db):
    # Class Documentation / application & database
    print(config.getDoc())
    print(app.getDoc())
    print(db.getDoc())

def ClassInheritance(): 

    classList=[WebApp,WebAppConfig,ForSQL,Database,FileinFlask,SelectSQLite3]
    for obj in range(0,len(classList)):
        print(f'{str(classList[obj])} of ',classList[obj].__mro__,'\n')
    
# Class Infomantion for Check ################################################

def main():
    config=WebAppConfig()
    config.config(document_root='./sample')
    (db,app)=config.db(),config.app()
    
    # WebAppSampleCode(app)
    # SQLSampleCode(db)

    # ClassDocument(config,app,db)
    ClassInheritance()
main()