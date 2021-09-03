# /usr/bin/env python
# -*- coding: utf-8 -*-

from py.webapp import *

class WebAppConfig(Database,WebAppInFlask):
    """
        FlaskApp Class
        - setDatabase
        - setFramework

        (sample code)
        
        #=====================================================================================
            def main():
                framework=WebAppFrameWork()
                
                ###############################################################################
                # + config method
                # database config:
                #    - database :(None | sqlite | pgsql)
                #    - dbname: (None | <Database Name>)
                #    - document_root: <Document Root Directory> (* required)
                ###############################################################################
                # + Stored Text:
                # - framework.config(document_root='doc_root')
                ###############################################################################
                # + SQLite:
                # - framework.config(database='sqlite',dbname='sample.db',document_root='./doc_root')
                ###############################################################################
                # + PgSQL:
                # - framework.config(database='pgsql',dbname='<dbname>',document_root='./doc_root')
                ###############################################################################

                (db,app)=framework.db(),framework.app()
                ...... and more
            
        #####################################################################################
    """
    __package__='__database_env__'
    
    __database__={
        'sqlite':False,
        'mysql':False,
        'pgsql':False,
        'psql':False,
    }

    __framework__={
        'flask':False,
        'django':False,
        'cart':False
    }
    
    def __init__(self):
        self.setType(None)
        self.setDatabaseName(None)
        super().__init__(self.dbtype,self.dbname)
        self.setDatabase(None)
    
    def __doc(self):
        """
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
                    
                # Example SQL Sample:
                # sql=f'SELECT * from {db.getDatanaseName()};'

                # db.connect()
                # data=db.cursor().execute(sql).fetchall()
                # db.close()
                # print(data.fetchall())
        """
        return self.__doc__

    def config(self,database=None,framework=None,dbname=None,document_root=None,**kwargs):

        if database is not None:
            self.setDatabase(database)
        if framework is not None:
            self.setFramework(framework)
        if dbname is not None:
            self.setDatabaseName(dbname)
        if document_root is not None:
            self.setDocumentRoot(document_root)
            self.makeDir(document_root)

        for kw in kwargs:
            if kw == 'user':
                self.setUser(kwargs[kw])

    def Database(self):
        database_application=self.getDatabase()
        if self.__database__['sqlite']:
            database_dir=document_root+self.__install__['directory'][0]
            self.makeDir(database_dir)
            return SelectSQLite3(database_application,dbname=database_dir+self.getDatabaseName())

        elif self.__database__['pgsql'] or self.__database__['psql']:
            try:
                user=self.getUser()
            except AttributeError:
                self.setUser((None,None))

            return SelectPgSQL(database_application,dbname=self.getDatabaseName(),user=user)

        # No Database Application
        return FileinFlask(database_application)
    
    def Application(self):

        framework=WebAppInFlask()
        document_root=self.getInstallDir()
        if document_root=='':
            print('+ document_root is not found.')
            print('     - look at method config(document_root="xxx")',self.__doc())
            
            exit()
        
        if self.__framework__['django']:
            framework=WebAppInDjango()
        elif self.__framework__['cart']:
            framework=ShoppingCart()

        framework.setInstallDir(document_root)
        framework.setDatabaseName(self.getDatabaseName())
        return framework

    def getGlobalVar(self):
        return self.__install__

    def getDatabase(self):
        return self.__database_application

    def setDatabase(self,database=None):
        if database is not None:
           self.__database__[database]=True
        self.__database_application=database
    
    def setFramework(self,framework=None):
        if framework is not None:
            self.__framework__[framework]=True

    def app(self):
        return self.Application()

    def db(self):
        return self.Database()