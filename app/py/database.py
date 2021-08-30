# /usr/bin/env python
# -*- coding: utf-8 -*-

def ErrorMessage(modulename=None):
    print(f'Import Can\'t Module "{modulename}"')
    print('Read the .md file')
    print('pip -r requirements.txt')

import inspect,sqlite3
# load module 

try:
    # PostgreSQL
    import psycopg2
except ModuleNotFoundError as e:
    ErrorMessage('psycopg2')
    exit()

try:
    # MySQL
    import pymysql
except ModuleNotFoundError as e:
    ErrorMessage('MySQLdb')
    exit()

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
    
    def getPackage(self):
        return self.__package

    def setPackage(self,**package):
        self.__package=package

    def getHost(self):
        return self.host

    def setHost(self,host=None):
        self.host=host
    
    def getPort(self):
        return self.port
    
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
    
    def getUser(self):
        return (self.__user,self.__password)

    def setUser(self,user=(None,None)):
        (self.__user,self.__password)=user
    
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
        self.__connect()
        self.__close()
        pass

    def test(self):
        self.__connect()
        self.__close()

    def __connect(self):
        self.connection=None
        self.connection=sqlite3.connect(self.getDatabaseName())
        return self.connection

    def __cursor(self):
        return self.connection.cursor()

    def __close(self):
        self.connection.close()

class SelectPgSQL(Database):
    """
    PostgresSQL:
        [how to install]
        <homebrew ver.> - 
        $ brew install postgresql
        $ brew service (start | stop) postgresql
        [psql(database connection)]
        $ psql --V
        $ psql --help
        $ psql -d postgres -U [username] -W [password]
        [psql console]
        > ¥h
            - help
        > ¥dt
            - table info
        > select verison();
            - postgres install version
        > ¥q
            - quit

    """
    __package__='__pgsql__'
    __config__={}

    def __init__(self,dbtype=False,dbname='sample_pgsql',host='localhost',**kwargs):
        super().__init__(dbtype,dbname)
        self.setHost(host)
        try:
            self.setUser(kwargs['user'])
        except KeyError:
            pass

        self.setDatabaseName(dbname)
        self.__config(dbtype)
    
    def pg_config(self):
        return self.__config__

    def __config(self,dbtype):
        self.__config__['user']=self.getUser()
        self.__config__['host']=self.getHost()
        self.__config__['dbname']=self.getDatabaseName()
        self.__config__['dbtype']=(dbtype,self.__package__.replace('__',''))

    def test(self):
        try:
            self.__connect()
            cur=self.__cursor()
            cur.execute('select version();')
            print(cur.fetchall())
            self.__close()
        except ModuleNotFoundError:
            print('Database connection failed.')

    def __connect(self):
        usertext=''
        try:
            (user,password)=self.getUser()
            if user is not None:
                usertext=f' user={user}'
                if password is not None or password!='':
                    usertext+=f' password={password}'
        except AttributeError:
            print('Postgres User is not set.')

        self.connection=psycopg2.connect(f'host={self.getHost()} dbname={self.getDatabaseName()}{usertext}')
        return self.connection
    
    def __cursor(self):
        return self.connection.cursor()

    def __close(self):
        self.connection.close()
