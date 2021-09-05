from py.database import *
from py.webapp import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd
import sqlite3,requests

from threading import Thread

try :
    import MySQLdb
except ModuleNotFoundError:
    # print('pip install mysqlclient')
    pass

try:
    # PostgreSQL
    import psycopg2
except ModuleNotFoundError as e:
    ErrorMessage('psycopg2')
    exit()
try:
    from selenium.webdriver import Chrome,ChromeOptions
except ModuleNotFoundError:
    print('Please "pip install selenium."')

# Base Class
class DatabaseManagement(Database,WebApp):
    """
    """
    __package__='__database_management__'
    __databasetype__=['sqlite','mysql','pgsql']
    filetype=[()]
    def __init__(self,host=None,port=None,dbname=None):
        super().__init__(port,dbname)
        self.config()
        
    def config(self,host=None,port=None,dbname=None,**kwargs):
        self.setHost(host)
        self.setPort(port)
        self.setDatabaseName(dbname)
        # self.setUser(kwargs['user'])

    def open(self):
        self.window()
    
    def window(self):
        root=tk.Tk()
        root.geometry('800x300')
        root.mainloop()

    def asOpen(self):
        wd=self.getCurrentDirectory()
        return fd.askopenfilename(filetypes=self.filetype,initialdir=wd)

    def save(self):
        return fd.asksaveasfilename(filetypes=self.filetype,initialdir=self.getWorkingDirectory())

class SQLiteWindow(DatabaseManagement):

    filetype=[('*','*.db')]
    def __init__(self,host=None,port=None,dbname=None):
        super().__init__(host,port,dbname)

    def window(self):
        self._root=tk.Tk()

        self._root.title('SQLite Exproler')
        self._root.geometry('1024x768')

        self.lists=[]
        self.file=None

        self.sqliteBrowser(self._root)
        # view result table name & column name
        self.sqlCodeFrame(self._root)
        
        # view result table name
        self.viewSQLTextAndListFrame(self._root)

        # view list: viewTableForSQL()
        self.viewTableFrame(self._root)

        self.setLayout()
        self._root.mainloop()
        
    
    def sqlCodeinEntry(self,root=None,handler=None):
        self.oneline_text=None
        
        if root is not None:
            self.oneline_text =tk.Entry(root,width=100)
            self.oneline_text.bind('<Key>',handler)
            self.oneline_text['state']=tk.DISABLED #tk.NORMAL
            return self.oneline_text
        return None
    
    def sqlCodeExe(self,root=None,label=None,handler=None):
        self.exebutton=None
        if root is not None:
            self.exebutton=tk.Button(root,text=label)
            self.exebutton.bind('<1>',handler)
            return self.exebutton

    def sqlCodeFrame(self,root=None):
        self.sql_code_frame=tk.Frame(root)
        self.sqlCodeinEntry(self.sql_code_frame,self.sqlCodeWrite)
        self.sqlCodeExe(self.sql_code_frame,'execute',self.sqlCodeHandle)
        return self.sql_code_frame

    def sqlCodeHandle(self,e):
        sql=self.oneline_text.get()
        lists=[]
        if self.file is not None:
            conn=sqlite3.connect(self.file)
            csr=conn.cursor()
            csr.execute(sql)
            lists=csr.fetchall()
            
            conn.close()
        print(lists)

    def sqlCodeWrite(self,e):
        if e.keysym=='Return':
            sql=self.oneline_text.get()
            self.parseSQL(sql)
            lists=[]
            if self.file is not None:
                conn=sqlite3.connect(self.file)
                csr=conn.cursor()

                try:
                    csr.execute(sql)
                except sqlite3.OperationalError:
                    print(sql)
                    
                lists=csr.fetchall()
                conn.close()
                # self.updateTableForSQL(data=lists)
            print(lists)

    def parseSQL(self,sql):
        print(type(sql),'select * from tablename where'.split(' '))
        
    def fileOpenButton(self,root=None,label=None,handler=None):
        self.asFileOpenButton=None
        if root is not None:
            self.asFileOpenButton=tk.Button(root,text=label)
            self.asFileOpenButton.bind('<1>',handler)
            self.asFileOpenButton.configure(width=70)
        return self.asFileOpenButton
    
    def sqliteBrowser(self,root=None):
        # label:filename
        self.sqlite_browser=tk.Frame(root)

        self.sqlite_browser_label_text=tk.StringVar()
        self.sqlite_browser_label_text.set('File Not Found.')

        self.sqlite_browser_label=tk.Label(self.sqlite_browser,textvariable=self.sqlite_browser_label_text)
        
        self.fileOpenButton(self.sqlite_browser,'Open the SQLite(.db) File',self.sqliteFileOpenDialog)

        return 

    # SQLite File Open in Listbox
    def sqliteFileOpenDialog(self,e):
        self.file=self.asOpen()
        # print(file)
        conn=sqlite3.connect(self.file)
        csr=conn.cursor()
        csr.execute('SELECT tbl_name from sqlite_master;')
        lists=csr.fetchall()
        csr=conn.cursor()
        table_name=[]
        dict_table={}
        for li in range(0,len(lists)):
            csr.execute(f'PRAGMA table_info({lists[li][0]});')
            column=csr.fetchall()
            dict_table[lists[li][0]]={'data': column}
        # table_name.clear()
        self.lists=dict_table
        conn.close()
        
        self.view_sql_in_text['state']=tk.NORMAL
        self.oneline_text['state']=tk.NORMAL #tk.NORMAL

        self.sqlite_browser_label_text.set(f'SQLite File is {self.file}')
        self.viewUpdateText()
        # Listbox Activate > in Table(in Event Handle)
        self.viewUpdateListbox(self.viewListBoxHandle)
        self.view_sql_in_text['state']=tk.DISABLED
        
    def viewSQLinList(self,root=None,label=None):
        self.view_sql_in_text=tk.Text(root)
        self.view_sql_in_text['state']=tk.DISABLED
        return self.view_sql_in_text
    
    def viewSQLTextAndListFrame(self,root=None):
        self.view_sql_text_and_list_frame=tk.Frame(root)

        self.viewSQLinList(self.view_sql_text_and_list_frame)
        self.viewListbox(self.view_sql_text_and_list_frame)

        return self.view_sql_text_and_list_frame

    # Update Text
    def viewUpdateText(self):
        self.view_sql_in_text.delete('1.0','end')
        text='[Table Info]\n'
        for name in self.lists:
            text+=f'\t- {name}\n'
            # print(dict_table[name]['data'])
            rows=self.lists[name]['data']
            for data in range(0,len(rows)):
                # print(rows[data])
                text+=f'\t\t- {data}.{rows[data][1]} {rows[data][2]}\n'
            text+='\n'
        self.view_sql_in_text.insert('1.0',text)
        # self.view.disable()

    # Table - Treeview 
    def viewTableForSQL(self,root):
        self.table=ttk.Treeview(root)        
        tuple_list=tuple(range(1,2))

        self.table['column']=tuple_list
        # self.table['show']='headings'

        return self.table
    
    def viewTableFrame(self,root=None):
        self.view_table_frame=tk.Frame(root)
        self.viewTableForSQL(self.view_table_frame)

    def updateTableForSQL(self, heading=None, data=None):

        # Update Label
        select=self.listBox.get(tk.ACTIVE)
        self.label_listbox['text']=f'Select Table:[{select}]'

        tuple_list=tuple(range(1,2))
        if len(self.lists) > 0:
            tuple_list=tuple(range(0,len(heading)))
        
        self.table['column']=tuple_list
        self.table['show']='headings'
        # print(int(1024/len(heading)))
        minw=int(1024/len(heading))
        for i in range(0,len(heading)):
            self.table.heading(i, text=heading[i][1])
            self.table.column(i, stretch=False, minwidth=80,width=minw)

        # delete table data
        self.table.delete(*self.table.get_children())
        for i in range(0,len(data)):
            self.table.insert('','end',values=data[i])

    def activeListTableName(self,e):
        print(e)

    # Listbox
    def viewListbox(self,root=None):
        self.label_listbox=tk.Label(self.view_sql_text_and_list_frame,text='Select Table Name')
        self.listBox=tk.Listbox(root)
        return self.listBox

    # Listbox Update: 
    def viewUpdateListbox(self,handler=None):
        self.listBox.bind('<Double-Button-1>',handler)
        self.listBox.delete(0,tk.END)
        for dt in self.lists:
            self.listBox.insert(tk.END,dt)
    
    # Active List Column
    def viewListBoxHandle(self,e):
        select=self.listBox.get(tk.ACTIVE)
        conn=self.connect()
        cur=self.cursor(conn)
        cur.execute(f'SELECT * FROM {select};')
        data=cur.fetchall()
        conn.close()
        heading=self.lists[select]['data']
        self.updateTableForSQL(heading,data)
    
    def updateWindow(self,e):
        # print(self._root.winfo_width(), self.sqlite_browser_label.winfo_width())
        # w=e.winfo_width()
        # self.h=e.height
        pass

    def setLayout(self):
        self._root.update_idletasks()
        root_w=int(self._root.winfo_width())
        # self._root.configure(bg='#222')
        self._root.resizable(False,False)
        self._root.bind('<Configure>',self.updateWindow)
        
        # Browse sqlite
        self.sqlite_browser_label.grid(row=0)
        self.asFileOpenButton.grid(row=1,sticky=tk.W)
        self.sqlite_browser.grid(row=0,sticky=tk.W)

        sql_code_frame_w=int(root_w/9)
        self.sqlite_browser_label.configure(anchor='w',width=sql_code_frame_w)
        self.asFileOpenButton.configure(width=sql_code_frame_w)
        self.sqlite_browser.configure(bg='systemTransparent')

        # self.oneline_text.grid(row=0,column=0)
        # self.exebutton.grid(row=0,column=1)
        # self.sql_code_frame.grid(row=1,sticky=tk.NW)

        self.sql_code_frame.configure(bg='systemTransparent')

        self.label_listbox.grid(row=0,column=0)
        self.listBox.grid(row=1, column=0)
        self.view_sql_in_text.grid(row=1, column=1,sticky=tk.NW)
        self.view_sql_text_and_list_frame.grid(row=3,sticky=tk.NW)

        self.label_listbox.configure(anchor='w',width=20)
        self.listBox.configure(height=16,width=20)
        self.view_sql_in_text.configure(height=20,width=120)
        
        self.table.grid(row=0)
        minw=int(self._root.winfo_width())
        self.table.column(0, stretch=False, minwidth=80,width=minw)
        self.view_table_frame.grid(row=4,sticky=tk.NW)
        self.table.configure(height=18)
        self.view_table_frame.configure(width=root_w/9)
        
    def connect(self):
        return sqlite3.connect(self.file)
    
    def cursor(self,conn=None):
        return self.connect().cursor()

class PgSQLWindow(SelectPgSQL):
    __config__={}
    def __init__(self,arg=None):
        # super().__init__(host=None,)
        self.__config__=arg.pg_config()
        self.window()

    def user(self):
        return self.__config__['user']
    
    def dbname(self):
        return self.__config__['dbname']
    
    def host(self):
        return self.__config__['host']

    def open(self):
        self._root.mainloop()

    def window(self):
        self._root=tk.Tk()
        self._root.geometry('720x480')
        self._root.title('PostgreSQL Browser')
        self.browser()
        self.panel()
        self.setLayout()

    def browser(self):
        self.frame=tk.Frame(self._root)
    
    def panel(self):
        (self.__user,self.__password)=self.user()
        title=f'username[{self.__user}]'
        self.__usernameLabel=tk.Label(self.frame,text=title)
        
        title=f'password[{str(self.__password)}]'
        self.__passwordLabel=tk.Label(self.frame,text=title)

        title=f'Database Name[{str(self.dbname())}]'
        self.__dbnameLabel=tk.Label(self.frame,text=title)

        title=f'TEST CODE'
        self.__testCode=tk.Entry(self.frame,text=title)

        message='Push the Connection Test'
        self.__testButton=tk.Button(self.frame,text=message)
        self.__testButton.bind('<1>',self.click_test_btn)
    
    def click_test_btn(self,e):
        self.__connect()
        self.cur=self.__cursor()
        self.cur.execute('select version();')
        self.cur.execute('')
        self.response=self.cur.fetchall()
        self.__close()
        print(self.response)
        self.__testCode.delete(0,tk.END)
        self.__testCode.insert(tk.END,('success!',self.response))

    def setLayout(self):
        # self.frame.configure()
        self.__usernameLabel.grid(column=0,row=0)
        self.__passwordLabel.grid(column=1,row=0)
        self.__testButton.grid(columnspan=2,row=1)
        self.__testCode.grid(columnspan=2,row=2)
        self.__dbnameLabel.grid(columnspan=2,row=3)
        # self.__passwordEntry.grid(column=1,row=1)
        self.frame.grid(column=0,row=0)

    def __connect(self):
        usertext=''
        try:
            (user,password)=self.user()
            if user is not None:
                usertext=f' user={user}'
                if password is not None or password!='':
                    usertext+=f' password={password}'
        except AttributeError:
            print('Postgres User is not set.')
        self.connection=psycopg2.connect(f'host=localhost dbname=test {usertext}')

    def __cursor(self):
        return self.connection.cursor()

    def __close(self):
        self.connection.close()

#################################### GUI window program END

class Loading:

    def __init__(self,app=None,db=None):
        self.setApp(app)
        if db is not None:
            self.setDB(db)
    
    def getApp(self):
        return self.application

    def setApp(self,app=None):
        self.application=app
    
    def getDB(self):
        return self.database

    def setDB(self,db=None):
        self.database=db

    def sqlite_onclick(self,e):
        window=SQLiteWindow()
        window.open()

    def pgsql_onclick(self,e):
        #print(self.getDB().pg_config())
        window=PgSQLWindow(self.getDB())
        window.open()
        
    def onclick_flask_run(self,e):
        config=self.getApp().loadConfig()
        self.uri=f'http://{config["host"]}:{config["port"]}'
        # print(url)
        if self.driver is not None:
            self.driver.quit()
        Thread(target=self.chrome_thread).start()
    
    def onclick_gunicorn_run(self,e):
        config=self.getApp().loadConfig()
        self.gunicorn_uri=f'http://{config["gunicorn"]["host"]}:{config["gunicorn"]["port"]}'
        self.guincorn_file=config['gunicorn']['file']
        Thread(target=self.gunicorn_thread).start()
        if self.driver is None:
            print('Please wait. open Chrome.')
            sleep(1)
        Thread(target=self.chrome_thread).start()

    def onclick_browser_run(self,e):
        driver=Chrome()

    def gunicorn_thread(self):
        self.uri=self.gunicorn_uri
        install=self.getApp().loadConfig()["install_path"]
        file=install+self.guincorn_file.replace('./','/')
        text=f'[gunicorn_get_start]:{self.uri}\n'
        print(text)
        response=None
        try:
            response=requests.get(self.uri)
            text+=f'[gunicorn_started::{response.status_code} OK]:{self.uri}\n'
        except requests.exceptions.ConnectionError:
            subprocess.call(f'{file}', shell=True)
            text+=f'[gunicorn_start::{response.status_code}] NG:{self.uri} {file}\n'
            sleep(1)
        # self.app_logging(text)
        print(text)
        
    def chrome_thread(self):
        url=self.uri
        try:
            response=requests.get(url)
            if response.status_code==200:
                if self.driver is not None:
                    self.driver.quit()
                self.driver=Chrome()
                self.driver.get(url)    
            else:
                print('+ program abort: Chrome.')
                exit()
        except requests.exceptions.ConnectionError:
            print(f'Connection refused.(url:{url})')
    
    def app_logging(self,text=None):
        doc_root=self.getApp().loadConfig()["doc_root"]
        app_log='/manage/logs/application_log'
        log=self.getApp().loadConfig()["doc_root"]+app_log
        with open(log,'a') as fp:
            fp.write(text)
        
    def run(self,app=None,db=None):
        
        config=self.getApp().loadConfig()

        window=tk.Tk()
        window.title('webapp explorer hub')

        sqlite_button=tk.Button(window,text='SQLite explorer')
        sqlite_button.bind('<1>',self.sqlite_onclick)

        # print(config['database']['type'])
        pgsql_button=tk.Button(window,text='Postgre SQL explorer')
        pgsql_button.bind('<1>',self.pgsql_onclick)
        if config['database']['type']!='pgsql':
            pgsql_button['state']=tk.DISABLED
        
        flask_button=tk.Button(window,text=f'flask({config["host"]}:{config["port"]})')
        flask_button.bind('<1>',self.onclick_flask_run)

        config=self.getApp().loadConfig()['gunicorn']
        gunicorn_button=tk.Button(window,text=f'Gunicorn({config["host"]}:{config["port"]})')
        gunicorn_button.bind('<1>',self.onclick_gunicorn_run)

        self.driver=None
        doc_button=tk.Button(window,text='Getting Start(Doc)')
        doc_button.bind('<1>',self.onclick_doc_run)
    
        # Layout
        sqlite_button.pack()
        pgsql_button.pack()
        flask_button.pack()
        gunicorn_button.pack()
        doc_button.pack()
        
        window.mainloop()

    def onclick_doc_run(self,e):
        sub_root=tk.Tk()
        sub_root.geometry('600x600')
        getting_start=self.getting_start()
        text=tk.Text(sub_root)
        text.insert('1.0',getting_start)
        text.pack()
        sub_root.mainloop()

    def getting_start(self):
        sharp='#'*64
        getting_start=f'''{sharp}
        [Homebrew]
            + Document
                - 
            + install the application(postgres,sqlite,nginx,python,etc...)
                $ brew search [application]
                $ brew install [application]
            <Example: postgres>
                $ brew search postgres
                $ brew install postgres
            + start application( change configuretion to application documents )
                $ brew services start [server application(nginx,postgres,etc...)]
    {sharp}
        [Python]
    {sharp}
            + set virtual env(Python 3.8)
                $ python -m venv [ venv directory ] 
                $ source ./[ venv directory ]/bin/activate
                - (Windows is /bin to ¥Sctipts)
            + Need to module install:
                $ pip install -r requirements.txt

            + Finish to Virtual ENV:
                $ deactivate

            + List the module(pip)
                $ pip list
    {sharp}
        [PostgreSQL]:
    {sharp}
        + install postgres : version management system apt-get etc...
        + (Search)
            $ which postgres
        
        + (console help)
            $ psql --help
        
        + (Start Service)
            + Linux/OSX
            $ service (start|restart|stop) postgres
            + OSX/Linux
            $ brew services (start|restart|stop) postgres
        
        + (console login)
            $ psql -d <database name>
                or
            $ psql -d <database name> -U "username" -p
    {sharp}
        [nginx]
        + (Search)
            $ which nginx

        + (Start Service)
            $ brew services (start|restart|stop) nginx

        + (console help)
            $ nginx -h
    {sharp}
        [This Application]
        + (Logfile):

            + (install log)
                - ./first_web_app/manage/logs/install.log

            + ( gunicorn_accesslog )
                - ./first_web_app/manage/logs/gunicorn_accesslog

            + ( gunicorn_errorlog )
                - ./first_web_app/manage/logs/gunicorn_errorlog

            + ( flask_access_log )
            + ( flask_error_log )

        + (application)
            + (start)
                # move current directory
                $ cd ./first_web_app/
                # input command + return.(Flask Load)
                $ python main.py
                    or 
                $ 

            + (document root)
                - ./first_web_app/ (default)
                    

                    - main.py(Flask Application)
                    - gunicorn_start
                        # start gunicorn @cli
                        $ ./gunicorn_start
            + (management file)
                - ./first_web_app/manage (default)
            + (static and template file)
                - ./first_web_app/static (default)
                - ./first_web_app/templates (default)
                    - main.html (based by Bootstrap)
        '''
        return getting_start
