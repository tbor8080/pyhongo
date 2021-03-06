# /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,datetime,subprocess,json
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
        'directory':['/database','/templates','/static','/javascript','/css','/img','/manage','/logs'],
    }
    host='127.0.0.1'

    def __init__(self):
        self.setInstallOption()

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
        self.py_filename=self.getInstallDir()+'/'+file

    def getTmplFile(self):
        return self.tmpl_filename
    
    def setTmplFile(self,file):
        self.tmpl_filename=file
    
    def getJsonFile(self):
        return self.config_json
    
    def setJsonFile(self,file=None):
        if file is None:
            exit()
        self.config_json=file

    def loadJson(self,filename=None):
        if filename is None:
            exit()
        with open(filename,'rt') as fp:
            return json.load(fp)
    
    def getGunicorn(self):
        return self.__gunicorn
    
    def setGunicorn(self,host='127.0.0.1',port=8080,worker=2,program='main'):
        self.__gunicorn=(host,port,worker,program,self.getGunicornFile())
        self.__install__['gunicorn']=self.__gunicorn

    def getGunicornFile(self):
        return self.config_gunicorn
    
    def setGunicornFile(self,file=None):
        self.config_gunicorn=file
    
    def setGunicornLog(self,access_log=None,error_log=None):
        self.access_log_gunicorn=access_log
        self.error_log_gunicorn=error_log

    def getGunicornLog(self):
        return (self.access_log_gunicorn,self.error_log_gunicorn)
    
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
        # command for .py file
        if file is None:
            file=self.getPyFile()
            # print(self.getPyFile())
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
    
    def gunicorn_start(self):
        subprocess.call(f'{self.getInstallDir()}/gunicorn_start', shell=True)
    
    def setInstallOption(self):

        self.__options={
            "install":True,
            "run":{
                "flask":True,
                "sqlite":False,
                "gunicorn":False,
                "browser":{
                    "chrome":True,
                    "firefox":False,
                    "edge":False,
                    "safari":False
                }
            }
        }

    # Switch the Install Option

    def switch_to(self,types='install',options=(True,None)):
        try:
            if types=='install':
                self.option()[types]
            else:
                self.option()['run'][types]
            
        except KeyError:
            print(types,self.option())
            print('Function : switch_to(type="install",option=(True,None))')
            print('type="value" is "install" or "flask" or "browser" or "database(sqlite,mysql,psql)" or "gunicorn".')
            exit()
        
        # print(options, type(options) is bool)

        if type(options) is bool:
            options=(options,None)

        (flag,option)=options
        result=None

        if types=="install":
            result=self.switch_installer(flag)
        elif types=="flask":
            result=self.switch_run_flask(flag)
        elif types=="browser":
            result=self.switch_run_browser(option, flag)
        elif types=="sqlite":
            result=self.switch_run_sql_exproler(types, flag)
        elif types=='gunicorn':
            result=self.switch_run_gunicorn(flag)
        
        return result
        

    def switch_installer(self,flag=True):

        self.__options["install"]=flag
        return self.__options["install"]

    def switch_run_flask(self,flag=True):

        self.__options["run"]["flask"]=flag
        return self.__options["run"]["flask"]

    def switch_run_browser(self,browser='chrome', flag=True):

        try:
            self.__options["run"]["browser"][browser]
        except KeyError:
            print('browser=(variable) is "chrome" or "firefox" or "edge" or "safari".',file=sys.stdout)
            exit()

        self.__options["run"]["browser"][browser]=flag
        return self.__options["run"]["browser"][browser]
    
    def switch_run_gunicorn(self, flag=False):

        self.__options["run"]["gunicorn"]=flag
        return self.__options["run"]["gunicorn"]
    
    def switch_run_sql_exproler(self, database='sqlite', flag=False):
        try:
            self.__options["run"][database]
        except KeyError:
            print('database=(variable) is "sqlite" or "pgsql" or "psql".',file=sys.stdout)
            exit()

        self.__options["run"][database]=flag
        return self.__options["run"][database]

    def option(self):
        return self.__options

class WebAppInDjango(WebApp):
    """
    WebApplication Templates in Django.
    """
    __package__='__django__'
    def __init__(self):
        super().__init__()

# WebAppInFlask: Class
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
        super().__init__()

        # {'path':'/','function':function}
        self.route=[]
        self.tbl=[]
        self.setTitle('SampleWebApp')
        self.setTmplFile('main.html')
        self.setPort(8080)
        self.setHost('127.0.0.1')
        self.debug=False

    def __initialize_app(self):

        self.setTitle('SampleWebApp')
        self.setTmplFile('main.html')
        self.setPort(8080)
        self.setHost('127.0.0.1')
        self.debug=False

    def selectDataBase(self):
        pass

    def getClassName(self):
        return self.__class__.__name__

    def getDatabase(self):
        return self.db

    def setDatabase(self,database=None):
        self.db=database

    def getType(self):
        return self.dbtype

    def setType(self,types):
        self.dbtype=types

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
    
    def getFramework(self,framework=None):
        return self.__framework

    def setFramework(self,framework=None):
        self.__framework=framework

    def loadConfig(self,filename=None):
        try:
            self.getJsonFile()
        except:
            self.setJsonFile(f'{self.getInstallDir()}/manage/config.json')

        if os.path.exists(self.getJsonFile()):
            # print(self.getJsonFile())
            with open(self.getJsonFile(),'rt') as fp:
                data=fp.read()
            return json.loads(data)
        return {'result':'404 Not Found.'}

    def appConfig(self):

        doc_root=self.getDocumentRoot()
        database=self.getDatabase()
        database_dir=doc_root+self.__install__['directory'][0]
        templates=doc_root+self.__install__['directory'][1]
        static=doc_root+self.__install__['directory'][2]
        javascript=static+self.__install__['directory'][3]
        css=static+self.__install__['directory'][4]
        img=static+self.__install__['directory'][5]
        (dbuser,dbhost,dbport)=(None,None,None)
        try:
            dbuser=database.getUser()
        except AttributeError:
            database.setUser((None,None))
            dbuser=database.getUser()
        try:
            dbhost=database.getHost()
        except AttributeError:
            database.setHost(None)
            dbhost=database.getHost()
        try:
            dbport=database.getPort()
        except AttributeError:
            database.setPort(1234)
            dbport=database.getPort()
        dbuser=list(dbuser)
        dbuser[1]='*'*len(str(dbuser[1]))

        self.__config={
            'host':self.getHost(),
            'port':self.getPort(),
            'install_path':self.getCurrentDirectory(),
            'doc_root':self.getCurrentDirectory()+'/'+self.getDocumentRoot().replace('./',''),
            'main':self.getPyFile(),
            'framework':self.getFramework(),
            'database':{
                'dir':database_dir,
                'type':self.getType(),
                'name':self.getDatabaseName(),
                'user':dbuser,
                'host':dbhost,
                'port':dbport,
            },
            'flask':{
                'title':self.getTitle(),
                'tmpl':{
                    'file':templates+'/'+self.getTmplFile(),
                    'html':templates,
                    'static':{
                        'static':static,
                        'javascript':javascript,
                        'css':css,
                        'img':img,
                    }
                }
            },
            'gunicorn':{
                'file':self.getGunicornFile(),
                'host':self.getGunicorn()[0],
                'port':self.getGunicorn()[1],
                'worker':self.getGunicorn()[2],
                'program':self.getGunicorn()[3],
                'access_log':self.getGunicornLog()[0],
                'error_log':self.getGunicornLog()[1],
            }
        }

        return self.__config

    def setCodeJson(self):
        self.setJsonFile('config.json')
        return self.appConfig()
    
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
    # code
        '''
        return text

    def getImportModule(self):
        return self.import_module

    # setImportModule('os','sys','datetime')
    def setImportModule(self,module=['os','sys','datetime']):
        self.import_module=module
    
    def debug_code(self):
        sharp='#'*32
        massage=f"""{sharp}
        + 
        + 
        + 
        + 
{sharp}
"""
        print(massage)

    def setCodeGunicorn(self):
        (host,port,worker,program,run_gunicorn)=self.getGunicorn()
        (access_log,error_log)=self.getGunicornLog()
        source=f'''# Input Your Setting({run_gunicorn}):
# Read the gunicorn Documents
# - (https://gunicorn.org/#quickstart)
#
#  Example 1)
#	+ main.py in app=Flask(__name__)
#		>> PROGRAM="main:app"
#
#  Example 2)
#	+ main.py in application=Flask(__name__)
#		>> PROGRAM="main"
#               or
#       >> PROGRAM="main:application"
#

PROGRAM="{program}"

# ACCESSLOG
ACCESSLOG="{access_log}"
# ERRORLOG
ERRORLOG="{error_log}"

# Input Your Host & Port Number:
ADDRESS="{host}:{port}"

# WORKER
WORKER={worker}

cd `dirname $0`

GUNICORN_COMMAND=`which gunicorn`

if [ "$GUNICORN_COMMAND" = "" ] ;then
	echo "- command not found ( at gunicorn ) "
	echo "- install gunicorn, read the document."
	echo "- https://gunicorn.org/#quickstart"
	echo "> pip install gunicorn"
	echo "> gunicorn -w 4 main"
	`open "https://gunicorn.org/#quickstart"`
	exit 1
fi

if [ -z "$ADDRESS" ] ;then
	# Default Address
	ADDRESS='127.0.0.1:8080'
fi

gunicorn -w "$WORKER" -b "$ADDRESS" --access-logfile "$ACCESSLOG" --error-logfile "$ERRORLOG" "$PROGRAM"

        '''
        return source

    def setCodePy(self):
        filename='main.py'
        self.setComment('This code was created by Automation tools')
        try:
            self.getTable()
        except AttributeError:
            self.setTable([])

        code=''
        if self.getType()=='sqlite':
            code=self.setCodeSqlite()
        elif self.getType()==False:
            code=self.setCodeNotSQL()

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
application=Flask(__name__)
'''
        # for Loop(Flask Routing)
        for rt in self.route:
            # print(rt['path'])
            method=''
            if 'method' in rt:
                method=',methods=[\''+rt['method']+'\']'
            text+=f'''        
# ======================================== routing start

@application.route('{rt['path']}'{method})
def {rt['function']}():
    {code}
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
    application.run(debug=debug, port=port)
'''
        # Please, Typing a command line tools(right here) >python main.py
        # success 
        return text
    
    def setCodeHtml(self):
        text='''<!DOCTYPE html>
<html lang='ja'>
    <!-- https://flask.palletsprojects.com/en/2.0.x/ -->
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
            <h1>Work It!</h1>
            <buttton id='editable'>??????????????????????????????</button>
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
        text=f'''python {self.getPyFile()}'''
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

    def remove_docroot_code(self):
        file=self.getJsonFile()
        config=self.loadJson(file)
        doc_root=config["doc_root"]
        install_dir=config["install_path"]
        return f'rm -rf {doc_root.replace(install_dir,".")}'
    
    def auto_run_code(self):
        file=self.getJsonFile()
        config=self.loadJson(file)
        return f'python {config["install_path"]}'

    def install(self):

        dir=self.getInstallDir()
        doc_root=self.getDocumentRoot()
        app_path=self.getCurrentDirectory()

        log_text='*********************************************************************\n'
        log_text+=f'Install to "{self.getInstallDir()}" Directory\n'
        log_text+='*********************************************************************\n'
        # Text in File Variable 
        log_file_text=log_text
        print(log_text)
        
        text=self.setCodePy()
        # file=self.getPyFile()
        # self.setPyFile(file)
        self.write(self.getPyFile(),text)
        
        log_text='+ create python program > '+self.getPyFile()
        print(log_text)
        log_file_text+=log_text
        
        self.installAction(15)

        # text=self.setCodeYAML()
        # self.setYAMLFile(dir+'/'+self.getYAMLFile())
        # self.write(self.getYAMLFile(),text)
        # print('\ncreate config > ',self.getYAMLFile())

        # manage directory
        manage=dir+'/manage'
        self.makeDir(manage)
        # log directory
        logs=manage+'/logs'
        self.makeDir(logs)

        # install log 
        log_file=manage+'/install.log'

        # gunicorn files
        self.setGunicornFile('gunicorn_start')
        access_log=f'{app_path}{logs.replace("./","/")}/gunicorn_access_log'
        error_log=f'{app_path}{logs.replace("./","/")}/gunicorn_error_log'
        
        self.setGunicornLog(access_log,error_log)
        self.setGunicorn(host='127.0.0.1',port=5001,worker=2,program='main')

        text=self.setCodeGunicorn()
        file=dir+'/'+self.getGunicornFile()
        self.setGunicornFile(file)
        self.write(self.getGunicornFile(),text)
        subprocess.call('chmod 755 %s' % file, shell=True)
        log_text='\n+ create config(gunicorn) > '+self.getGunicornFile()
        print(log_text,end='')
        log_file_text+=log_text

        # gunicorn log        
        log_text='\n+ access_log(gunicorn) > '+access_log
        print(log_text,end='')
        log_text='\n+ error_log(gunicorn) > '+error_log
        print(log_text,end='')
        log_file_text+=log_text

        # config json
        text=self.setCodeJson()
        file=manage+'/'+self.getJsonFile()
        self.setJsonFile(file)
        # self.write(self.getJsonFile(),text)
        with open(self.getJsonFile(),'wt') as fp:
            json.dump(text,fp,indent=4,ensure_ascii=False)

        log_text='\n+ create config > '+self.getJsonFile()
        print(log_text)
        log_file_text+=log_text

        self.installAction(15)

        text=self.setCodeHtml()

        templates=dir+'/templates'
        self.makeDir(templates)
        log_text='\n+ create template directory:'+templates
        print(log_text,end='')
        log_file_text+=log_text

        tmpl_file=templates+'/'+self.getTmplFile()
        self.write(tmpl_file, text)
        log_text='\n+ create template file:'+tmpl_file
        print(log_text)
        log_file_text+=log_text

        self.installAction(15)

        static=dir+'/static'
        self.makeDir(static)
        log_text='\n+ create static directory:'+static
        print(log_text,end='')
        log_file_text+=log_text

        javascript=static+'/javascript'
        self.makeDir(javascript)
        log_text='\n+ create javascript directory:'+javascript
        print(log_text,end='')
        log_file_text+=log_text
        
        css=static+'/css'
        self.makeDir(css)
        log_text='\n+ create css directory:'+css
        print(log_text,end='')
        log_file_text+=log_text

        img=static+'/img'
        self.makeDir(img)
        log_text='\n+ create img directory:'+img
        print(log_text)
        log_file_text+=log_text

        self.installAction(20)

        log_text='\n'
        print(log_text,end='')
        log_file_text+=log_text

        success=f'''+ Install Finish and Success !!!
        =================================================
        >> Start Coding Python(WebApp) {self.getPyFile()} !!! :)
        > Project Directory: {self.getInstallDir()}
        > Python File: {self.getPyFile()}
        >> For Command:
        >       $python {self.getPyFile()}
        >> Gunicorn Server Start(OSX/Linux):
        > {self.getGunicornFile()}
        >> install log: {log_file}
        =================================================
        '''
        log_text=success
        print(log_text)
        log_file_text+=log_text
        self.write(log_file,log_file_text)

#####################################################################################

class ShoppingCart(WebAppInFlask):
    def __init__(self):
        super.__init__()
    
    def get(self):
        pass