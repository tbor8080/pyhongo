# /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,datetime,subprocess
from time import sleep
try:
    from flask import Flask, render_template, request, redirect
except ModuleNotFoundError:
    print('Please "pip install Flask". ')
import inspect
from py.database import *

try:
    from selenium.webdriver import Chrome,ChromeOptions
except ModuleNotFoundError:
    print('Please "pip install selenium."')

class WebApp:
    """
        Web Application Class
        - Base Class: WebApp()
            - Sub Class: WebAppInFlask()
            - Sub Class: WebAppFrameWork()
    """
    
    __package__='__webapp__'

    __database__={
        'sqlite':False,
        'mysql':False,
        'pgsql':False,
    }

    __framework__={
        'flask':False,
        'django':False,
    }

    __install__={
        'document_root':'./applications',
        'directory':['/database','/templates','/static','/javascript','/css','/img']
    }
    host='127.0.0.1'

    def getMethod(self,cls=None):
        if cls is not None:
            lists=[]
            classList={}
            
            # return map(lambda x:x[0],inspect.getmembers(cls,inspect.isclass))
            for i in range(0,len(inspect.getmembers(cls))):
                # print(i,inspect.getmembers(cls)[i][0])
                lists.append(inspect.getmembers(cls)[i][0])
            classList[self.__class__.__name__]=tuple(lists)
            return classList
    def getInherit(self,cls):
        print(cls.__mro__)

    def getDoc(self):
        return self.__doc__

    def getCode(self):
        return self.__doc__

    def getConfigDatabase(self):
        return self.__database__
    
    def getConfigFramework(self):
        return self.__framework__
    
    def getConfigDirectory(self):
        return self.__install__
    
    def getPackageName(self):
        return self.__package__

    def getDateNow(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def makeDir(self,path):
        if not os.path.isdir(path):
            os.makedirs(path)
    
    def getFile(self):
        return self.file

    def setFile(self,file):
        self.file=filename
    
    def getPyFile(self):
        return self.py_filename

    def setPyFile(self, file):
        self.py_filename=file

    def getTmplFile(self):
        return self.tmpl_filename
    
    def setTmplFile(self,file):
        self.tmpl_filename=file
    
    def getJsonFile(self):
        return self.config_json
    
    def setJsonFile(self,file):
        self.config_json=file
    
    def getYAMLFile(self):
        return self.config_yaml

    def setYAMLFile(self,file):
        self.config_yaml=file

    def mkdir(self):
        return False

    def getPath(self):
        # Short cut method
        return self.getWorkingDirectory()
    
    def getWorkingDirectory(self):
        # working directory
        return os.path.dirname(os.getcwd())
    
    def getCurrentDirectory(self):
        # curent directory
        return os.getcwd()
    
    def getInstallDir(self):
        return self.__install__['document_root']

    def setInstallDir(self,document_root='./'):
        self.__install__['document_root']=document_root
    
    def getDocumentRoot(self):
        return self.getInstallDir()

    def setDocumentRoot(self,document_root='./'):
        self.setInstallDir(document_root)
    
    def read(self,filename=None):
        if filename is not None:
            with open(filename, 'rt') as fp:
                text=fp.read()
            return text

    def write(self, filename=None, text=None):
        if filename is not None and text is not None:
            with open(filename, 'wt') as fp:
                fp.write(text)

    def run(self,file=None):
        # execute python code
        if file is None:
            file=self.getPyFile()
        subprocess.call('python %s' % file, shell=True)

    def installAction(self,count):
        for i in range(0, count):
            print('*',end="",flush=True)
            sleep(0.1)

    def getFunctionInfo(self, f='function name'):
        functions=eval(f)
        global_name=functions.__globals__
        name=functions.__name__
        args=functions.__defaults__
        docs=''
        if functions.__doc__:
            docs=functions.__doc__
        info=f'''
        # {global_name['__file__']}
        ============== {name}(Infomation) ==============
        
        [class name]: {self.getClassName()}
            
            - [arguments]: {args}

            - [document]: {docs}
        ============== {name}(Infomation) ==============
        '''
        return info
    
    def show(self,text=None):
        print(text)
    
    def browse(self):
        (host,port)=self.getHost(),self.getPort()
        url=f'http://{host}:{port}/'
        # selenium code:
        driver=Chrome()
        driver.get(url)

class WebAppInDjango(WebApp):
    """
    WebApplication Templates in Django.
    """
    __package__='__django__'

class WebAppInFlask(WebApp):

    '''
    This Class is Automation Test Class.
    Web Application Templates in Flask.

    Web App HTML Template Module :Flask

    WebApp(Flask) Sample Code > sample.py    

    [ Document Root (Working Directory)]

    - main.py
    - config.json
    - config.yaml
    - templates/
        - main.html
    - static/
        - javascript/*.js
        - css/*.css
        - img/*.[jpg|png|gif...]

    # run the Flask WebApp !!
    # typing a any code
    > python main.py

    [method]
        - setPyFile
            - Python File:str
        - setTitle
            - title:str
        - setPort
            - port number:int(1024-65535)
        - setDebug
            - True/False
        - setHost
            - Host Name:str
        - setTmplFile
            - HTML Template File:str
        - route
            - path
            - function
        - install
        - preview
        - run

'''
    __package__='__webapp__'

    def __init__(self, db=False):

        # print(db.getType())
        self.db=db
        self.appType(self.db)

        # {'path':'/','function':function}
        self.route=[]
        
        self.title='SampleWebApp'
        self.tmpl_file='main.html'

        self.port=8080
        self.host='127.0.0.1'
        self.debug=False


    def selectDataBase(self):
        pass

    def appType(self,db=False):
        self.appType=False
        if self.db:
            self.appType=True
            self.dbtype=db.getType()
            self.dbname=db.getDatabaseName()
            self.tbl=db.getTable()
        else:
            self.dbtype=False
            self.dbname=None
            self.tbl=[]

    def getClassName(self):
        return self.__class__.__name__

    def getType(self):
        return self.dbtype

    def setType(self,type):
        self.dbtype=dbtype

    def getDatabaseName(self):
        return self.dbname

    def setDatabaseName(self,name):
        self.dbname=name

    def getTable(self):
        return self.tbl

    def setTable(self,name):
        self.tbl.append(name)

    def getRoute(self):
        return self.route

    def setRoute(self, route={'path':'','function':''}):
        self.route.append(route)
    
    def setRouteMulti(self, route=[]):
        if len(route)>0:
            for r in range(0,len(route)):
                self.setRoute(route[r])

    def getTitle(self):
        if self.title=='':
            print('setTitle("WebApp Title")')
        return self.title

    def setTitle(self,title):
        self.title=title
    
    def getPort(self):
        return self.port

    def setPort(self,port):
        self.port=port
    
    def getHost(self):
        return self.host

    def setHost(self,host):
        self.host=host

    def getDebug(self):
        return self.debug

    def setDebug(self,debug):
        self.debug=debug

    def getComment(self):
        return self.comment

    def setComment(self,text):
        self.comment=text

    def setCodeJson(self):
        filename='config.json'

        doc_root=self.getDocumentRoot()
        database_dir=doc_root+self.__install__['directory'][0]
        templates=doc_root+self.__install__['directory'][1]
        static=doc_root+self.__install__['directory'][2]
        javascript=static+self.__install__['directory'][3]
        css=static+self.__install__['directory'][4]
        img=static+self.__install__['directory'][5]

        self.setJsonFile(filename)
        text='\t{\n'
        text+=f'''
            "tmpl_file":"{self.getTmplFile()}",
            "host":"{self.getHost()}",
            "port":"{self.getPort()}",
            "appname":"{self.getTitle()}",
            "dbtype":"{self.getType()}",
            "dbname":"{self.getDatabaseName()}",
            "dbtbl":{self.getTable()},
            "apppath":"{self.getCurrentDirectory()}",
            "doc_root":"{self.getDocumentRoot()}",
            "directory":'''
        text+='''{
            '''
        text+=f'''"database":"{database_dir}",
                "templates":"{templates}",
                "static": "{static}",
                "javascript":"{javascript}",
                "css":"{css}",
                "img":"{img}"'''
        text+='''},
        '''
        text+=f'''
        "route":"{self.getRoute()}"
        '''
        text+='}\n'
        return text
    
    def setCodeYAML(self):
        filename='config.yaml'
        self.setYAMLFile(filename)
        text=f'''config:
    appname:{self.getTitle()}
    doc_root:{self.getDocumentRoot()}
    apppath:{self.getPath()}
    dbname:{self.getDatabaseName()}
    dbtbl:{self.getTable()}
    tmplfile:{self.getTmplFile()}
    approute:{self.getRoute()}

'''
        return text

    def setCodeSqlite(self):
        # sqlite3 :code
        text='''
# Example: DataBase >> Sqlite3
# Sqlite3 Test Connection
conn=sqlite3.connect(dbname)
cursor=conn.cursor()

# SQL Code Start

# SQL Code End

# Database Close
conn.close()'''
        # sqlite3 :code
        return text

    def setCodeNotSQL(self):
        text=f'''
        '''
        return text

    def getImportModule(self):
        return importModule

    # setImportModule('os','sys','datetime')
    def setImportModule(self,module=['os','sys','datetime']):
        self.importModule=module

    def setCodePy(self):
        filename='main.py'
        self.setComment('This code was created by Automation tools')
        text=f'''# /usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: {self.getInstallDir()}/main.py
# Virtual Env(comamnd line.) > "python -m venv [venv name]"
# install Flask > "pip install Flask"
# 
# Please Your Application Enviroment.
import os,sys,datetime
from flask import Flask, render_template, request, redirect
'''

        if self.getType()=='sqlite':
            text+='import sqlite3'

        text+=f'''
# Production Server variable: debug,port,host
debug={self.getDebug()} # True or False
port={self.getPort()} # Your Envroment to change Port Number: [1024-65535]

# Loopback Address
# host="{self.host}" 

# Template File Path
tmpl_file="{self.getTmplFile()}" # Path: {self.getInstallDir()}/templates/main.html

# WebApp Title
page_title='{self.getTitle()}'

# DB Name
dbname='{self.getDatabaseName()}'

#Table Name
tbl={self.getTable()}

# Flask Instanse
app=Flask(__name__)
'''
        # for Loop(Flask Routing)
        for rt in self.route:
            print(rt['path'])
            method=''
            if 'method' in rt:
                method=',methods=[\''+rt['method']+'\']'
            text+=f'''        
# ======================================== routing start

@app.route('{rt['path']}'{method})
def {rt['function']}():'''
            if self.getType()=='sqlite':
                text+=self.setCodeSqlite()
            if self.getType()==False:
                text+=self.setCodeNotSQL()
            text+='''
    return render_template(
        tmpl_file, 
        title=page_title
    )

# routing end ==========================================
'''
# End for
        text+=f'''

# run to app
# browser access <Your Host&Port>
if __name__=="__main__":
    app.run(debug=debug, port=port)
'''
        # Please, Typing a command line tools(right here) >python main.py
        # success 
        return text
    
    def setCodeHtml(self):
        text='''<!DOCTYPE html>
<html lang='ja'>
    <head>
        <meta charset='utf-8'>
        <title>{{page_title}}</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    </head>
    <body>
        <!-- Image and text -->
        <nav class="navbar navbar-light bg-light">
        <a class="navbar-brand" href="#">
            <img src="https://getbootstrap.jp/docs/4.5/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">
            Bootstrap
        </a>
        </nav>
        <div class='container'>
            
        </div>
        <!-- 
            JQuery(https://api.jquery.com/) 
                & 
            Bootstrap(https://getbootstrap.jp/docs/4.5/getting-started/introduction/)
         -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        <!-- /JQuery & Bootstrap -->
    </body>
</html>
'''
        text+=f'''<!-- {self.getComment()} -->'''
        return text

    def setCodeShell(self):
        text=f'''python {self.getPyFile()}
'''
        return text

    def preview(self):
        self.setYAMLFile('config.yaml')
        self.setJsonFile('config.json')
        text=self.setCodePy()
        text+=f'\nwriting: {self.getPyFile()}'
        text+='\n-------------------------------------------------------------------------------------------\n'
        text+=f'\nwriting: {self.getYAMLFile()}'
        text+=self.setCodeYAML()
        text+='\n-------------------------------------------------------------------------------------------\n'
        text+=self.setCodeJson()
        text+='\n-------------------------------------------------------------------------------------------\n'
        text+=self.setCodeHtml()
        text+='\n-------------------------------------------------------------------------------------------\n'
        text+=self.setCodeShell()
        print(text)

    def install(self):
        dir=self.getInstallDir()
        log_file=dir+'/install.log'
        log_text='*********************************************************************\n'
        log_text+=f'Install to "{self.getInstallDir()}" Directory\n'
        log_text+='*********************************************************************\n'
        # Text in File Variable 
        log_file_text=log_text
        print(log_text)
        
        text=self.setCodePy()
        file=dir+'/'+self.getPyFile()
        self.setPyFile(file)
        self.write(self.getPyFile(),text)
        
        log_text='create python program > '+self.getPyFile()
        print(log_text)
        log_file_text+=log_text
        
        self.installAction(15)

        # text=self.setCodeYAML()
        # self.setYAMLFile(dir+'/'+self.getYAMLFile())
        # self.write(self.getYAMLFile(),text)
        # print('\ncreate config > ',self.getYAMLFile())

        text=self.setCodeJson()
        file=dir+'/'+self.getJsonFile()
        self.setJsonFile(file)
        self.write(self.getJsonFile(),text)
        log_text='\ncreate config > '+self.getJsonFile()
        print(log_text)
        log_file_text+=log_text

        text=self.setCodeHtml()

        templates=dir+'/templates'
        self.makeDir(templates)
        log_text='\ncreate template directory:'+templates
        print(log_text)
        log_file_text+=log_text

        tmpl_file=templates+'/'+self.getTmplFile()
        self.write(tmpl_file, text)
        log_text='\ncreate template file:'+tmpl_file
        print(log_text)
        log_file_text+=log_text

        self.installAction(15)

        static=dir+'/static'
        self.makeDir(static)
        log_text='\ncreate static directory:'+static
        print(log_text)
        log_file_text+=log_text

        javascript=static+'/javascript'
        self.makeDir(javascript)
        log_text='\ncreate javascript directory:'+javascript
        print(log_text)
        log_file_text+=log_text
        
        css=static+'/css'
        self.makeDir(css)
        log_text='\ncreate css directory:'+css
        print(log_text)
        log_file_text+=log_text

        img=static+'/img'
        self.makeDir(img)
        log_text='\ncreate img directory:'+img
        print(log_text)
        log_file_text+=log_text

        self.installAction(20)
        log_text='\n'
        print(log_text)
        log_file_text+=log_text

        success=f'''install success !!!
        =================================================
        write to Python(WebApp) code !!! :)
        > {self.getPyFile()}
        
        =================================================
        '''
        log_text=success
        print(log_text)
        log_file_text+=log_text
        self.write(log_file,log_file_text)

#####################################################################################

