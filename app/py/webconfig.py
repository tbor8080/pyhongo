# /usr/bin/env python
# -*- coding: utf-8 -*-

from py.webapp import *
class WebAppConfig(Database,WebAppInFlask):

    """
        FlaskApp Class
        - setDatabase
        - setFramework

        (sample code)
        #####################################################################################
            def createTable(db=None):
                if is not None:
                    # Create Table
                    db.setTableName('TEST1')
                    # append column
                    #    - name:None
                    #    - types:None
                    #    - val:None
                    #    - primarykey: Tuple(<column name>,<True | False)
                    #    - unique: <True | False>
                    db.appendColumn('commodity_id','INTEGER','NOT NULL',('commodity_id',True))
                    db.appendColumn('company_id','TEXT','NOT NULL')
                    db.appendColumn('doc_name','TEXT','NOT NULL')
                    db.appendColumn('reg_date','DATE','NOT NULL')
                    # Preview SQL Code
                    db.previewCode(db.getCreateTableCode())

                    # Execute SQL Code
                    sql=db.getCreateTableCode()
                    db.connect()
                    db.cursor().execute(sql)
                    db.close()
        #=====================================================================================
            def main():
                framework=WebAppFrameWork()
                (db,app)=framework.db(),framework.app()
                # database config:
                #    - database :None | sqlite | mysql | pgsql
                #    - dbname: None | <Your Database Name>
                #    - document_root: './application' | <Your Document Root Directory>
                # Text Based Application ETC....
                # framework.config(document_root='doc_root')
                # SQLite
                framework.config(database='sqlite',dbname='sample.db',document_root='./doc_root')
                # MySQL(Comming Soon)
                # framework.config(database='mysql',dbname='sample.db',document_root='./doc_root')
                # PgSQL(Comming Soon)
                # framework.config(database='pgsql',dbname='sample.db',document_root='./doc_root')

                # db.createDatabase()
                
                createTable(db)
                
                # Execute Sample:
                # sql=f'SELECT * from {db.getDatanaseName()};'

                # db.connect()
                # data=db.cursor().execute(sql).fetchall()
                # db.close()
                # print(data)
            
        #####################################################################################
    """
    __package__='__database_env__'
    
    __database__={
        'sqlite':False,
        'mysql':False,
        'pgsql':False,
    }

    __framework__={
        'flask':False,
        'django':False,
    }
    
    def __init__(self):
        self.setType(True)
        self.setDatabaseName(None)
        super().__init__(self.dbtype,self.dbname)

    def config(self,database=None,framework=None,dbname=None,document_root=None):
        if database is not None:
            self.setDatabase(database)
        if framework is not None:
            self.setFramework(framework)
        if dbname is not None:
            self.setDatabaseName(dbname)
        if document_root is not None:
            self.setDocumentRoot(document_root)

    def Database(self):
        document_root=self.getInstallDir()
        self.makeDir(document_root)
        if self.__database__['sqlite']:
            database_dir=document_root+self.__install__['directory'][0]
            self.makeDir(database_dir)
            return SelectSQLite3(True,dbname=database_dir+self.getDatabaseName())

        elif self.__database__['mysql']:
            return SelectMySQL(True,dbname=self.getDatabaseName())

        elif self.__database__['pgsql']:
            return SelectPgSQL(True,dbname=self.getDatabaseName())

        # No Database Application
        return FileinFlask(False)
    
    def Application(self):
        framework=WebAppInFlask()
        document_root=self.getInstallDir()
        
        if self.__framework__['django']:
            framework=WebAppInDjango()

        framework.setInstallDir(document_root)
        framework.setDatabaseName(self.getDatabaseName())
        return framework

    def getGlobalVar(self):
        return self.__install__

    def setDatabase(self,database=None):
        if database is not None:
           self.__database__[database]=True
    
    def setFramework(self,framework=None):
        if framework is not None:
            self.__framework__[framework]=True

    def app(self):
        return self.Application()

    def db(self):
        return self.Database()