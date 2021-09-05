# /usr/bin/env python
# -*- coding: utf-8 -*-

def ErrorMessage(modulename=None):
    print(f'Import Can\'t Module "{modulename}"')
    print('Read the .md file')
    print('pip -r requirements.txt')

import inspect,sqlite3
# load module 
from py.sheet.sheet import *

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

    __config__={}

    def __init__(self, dbtype=None, dbname=None):

        self.setType(dbtype)
        self.setDatabaseName(dbname)
        super().__init__()
    
    def className(self):
        return self.__class__.__name__
    
    def __config(self):
        pass
    
    def get(self):
        return self.__config__

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

    def getDatabase(self):
        return self.dbtype

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

    def isPgSQL(self):
        return False
    
    def isMySQL(self):
        return False 
    
    def isSQLite(self):
        return False
    
    def asStoredText(self):
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
    __config__={}
    matrixData=[]

    def __init__(self,dbtype=False,dbname='sample.txt'):
        super().__init__(dbtype,dbname)
        self.setFile(dbname)
    
    def __config(self):
        self.__config__['notdb']=self.isNonDB()
        self.__config__['sqlite']=False
        self.__config__['pgsql']=False
        self.__config__['psql']=False
        self.__config__['dbname']=None
        self.__config__['dbtype']='text'
    
    def isNonDB(self):
        return True

    def asStoredText(self):
        return True
    
    def getFile(self):
        return self.filename
    
    def setFile(self,filename='sample.csv'):
        self.filename=filename

    def saveCsv(self,column=[]):
        text=''
        self.save(text)

    def saveExcel(self,colmun=[]):
        text=''
        self.save(text)

    def save(self,text=''):
        with open(self.getFile(),'wt') as fp:
            fwrite(text)
    def asExcel(self):
        file=self.getFile()
    
class SelectSQLite3(Database):

    """
        - Database 
            - Sub Class: SelectSQLite3
    """
    __package__='__sqlite__'
    __config__={}

    def __init__(self,dbtype=None,dbname=None):
        super().__init__(dbtype,dbname)
        
        if dbname is None:
            print('database name is not found.')
            exit()

        self.setType(dbtype)
        self.setDatabaseName(dbname)

        if self.test() is False:
            print('+ Database Test is Failed.')
            exit()

    def isSQLite(self):
        return True

    def sqlite_config(self):
        return self.__config__

    def __config(self):
        self.__config__['sqlite']=self.isSQLite()
        self.__config__['dbname']=self.getDatabaseName()
        self.__config__['dbtype']=self.getType()

    def createDatabase(self):
        pass

    def test(self):
        self.__connect()
        cur=self.__cursor().execute('select sqlite_version();')
        response=cur.fetchall()
        self.__close()
        if len(response) > 0:
            return response
        return False

    def __connect(self):
        self.connection=None
        self.connection=sqlite3.connect(self.getDatabaseName())

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
            - postgres version(install)
        > ¥q
            - quit

    """
    __package__='__pgsql__'
    __config__={}

    def __init__(self,dbtype=None,dbname='sample_pgsql',**kwargs):
        super().__init__(dbtype,dbname)

        try:
            self.setHost(kwargs['host'])
        except KeyError:
            self.setHost('localhost')

        try:
            self.setUser(kwargs['user'])
        except KeyError:
            self.setUser((None,None))
        
        try:
            self.setPort(kwargs['port'])
        except KeyError:
            self.setPort(5432)

        self.setType(dbtype)
        self.setDatabaseName(dbname)

        self.__config()
    
    def isPgSQL(self):
        return True
    
    def pg_config(self):
        return self.__config__

    def __config(self):
        self.__config__['pgsql']=self.isPgSQL()
        self.__config__['user']=self.getUser()
        self.__config__['host']=self.getHost()
        self.__config__['port']=self.getPort()
        self.__config__['dbname']=self.getDatabaseName()
        self.__config__['dbtype']=self.getType()
        return self.__config__

    def __test(self):
        try:
            self.__connect()
            cur=self.__cursor()
            cur.execute('select version();')
            print(cur.fetchall())
            self.__close()
            return True
        except ModuleNotFoundError:
            print('Database connection failed.')
        return False

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
