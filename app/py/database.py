# /usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import sqlite3,pycopg2
from py.sql import *

class Database(ForSQL):
    """
        Database Class
    """
    __package__='__database__'

    __install__={
        'document_root':'',
        'directory':['/database/']
    }

    def __init__(self, dbtype=True, dbname=None):
        self.setType(dbtype)
        self.setDatabaseName(dbname)
        super().__init__()
    
    def className(self):
        return self.__class__.__name__

    def getType(self):
        return self.dbtype
    
    def setType(self,types):
        self.dbtype=types

    def getHost(self):
        return self.host
    
    def getPort(self):
        return self.port

    def setHost(self,host=None):
        self.host=host
    
    def setPort(self,port=None):
        self.port=port

    def getDatabaseName(self):
        return self.dbname
    
    def setDatabaseName(self,name):
        self.dbname=name

    def access(self, dbname):
        self.conn=None
        return self.conn

    def getInstallDir(self):
        return self.__install__['document_root']

    def setInstallDir(self,document_root='./data'):
        self.__install__['document_root']=document_root

    def isDatabase(self):
        if self.getType():
            return True
        return False

######################################################################################################

class FileinFlask(Database):

    """# Non Database
        - getFile
        - setFile
        - saveCsv
        - saveExcel: (x:column:{},y:row:{})
        - save: Save File method
    """
    __package__='__file__'

    matrixData=[]

    def __init__(self,dbtype=False,dbname='sample.txt'):
        super().__init__(dbtype,dbname)
        self.setFile(dbname)
    
    def getFile(self):
        return self.filename
    
    def setFile(self,filename='sample.csv'):
        self.filename=filename

    def appendMatrix(self,x,y,data):
        self.matrixData.append(x)
        self.matrixData[x].append(y)

    def saveCsv(self,column=[]):
        text=''
        self.save(text)

    def saveExcel(self,colmun=[]):
        text=''
        self.save(text)

    def save(self,text=''):
        with open(self.filename,'wt') as fp:
            fwrite(text)
    
class SelectSQLite3(Database):

    """
        - Database 
            - Sub Class: SelectSQLite3
    """
    __package__='__sqlite__'

    def __init__(self,dbtype=True,dbname=None):
        super().__init__(dbtype,dbname)
        self.setType(dbtype)
        if dbname is not None:
            self.setDatabaseName(dbname)
            self.createDatabase()

    def createDatabase(self):
        self._connect()
        self._close()
        pass

    def _connect(self):
        self.conn=None
        if self.getType():
            self.conn=sqlite3.connect(self.getDatabaseName())
        return self.conn

    def _cursor(self):
        self.csr=None
        if self.getType() and self.conn is not None:
            self.csr=self.conn.cursor()
        return self.csr

    def _close(self):
        if self.conn is not None:
            self.conn.close()

class SelectMySQL(Database):
    """MySQL:
    """
    __package__='__mysql__'
    def __init__(self,dbtype=False,dbname='sample_mysql'):
        super().__init__(dbtype,dbname)

    def getHost(self):
        return self.host

    def setHost(self, host='127.0.0.1'):
        return self.host

class SelectPgSQL(Database):
    """PostgresSQL:
    """
    __package__='__pgsql__'
    def __init__(self,dbtype=False,dbname='sample_pgsql'):
        super().__init__(dbtype,dbname)

    def getHost(self):
        return self.host

    def setHost(self, host='127.0.0.1'):
        return self.host
