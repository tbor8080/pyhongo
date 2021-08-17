from py.database import *
from py.webapp import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd
import sqlite3

from threading import Thread

try :
    import MySQLdb
except ModuleNotFoundError:
    # print('pip install mysqlclient')
    pass


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
        
    def config(self,host=None,port=None,dbname=None):
        self.setHost(host)
        self.setPort(port)
        self.setDatabaseName(dbname)

    def open(self):
        self.window()
    
    def window(self):
        root=tk.Tk()
        root.geometry('800x300')
        root.mainloop()

    def _onClick(self,e):
        pass
    
    def _onKeyboard(self,e):
        pass
    
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
        root=tk.Tk()
        self._root=root
        root.title('SQLite Exproler')
        root.geometry('1024x768')

        self.lists=[]
        self.file=None

        self.sqliteBrowser(root)
        # view result table name & column name
        self.sqlCodeFrame(root)
        
        # view result table name
        self.viewSQLTextAndListFrame(root)

        # view list: viewTableForSQL()
        self.viewTableFrame(root)

        self.setLayout()
        root.mainloop()
        
    
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

class Loading:

    def __init__(self,app=None):
        self.setApp(app)
    
    def getApp(self):
        return self.application

    def setApp(self,app=None):
        self.application=app

    def sqlite_onclick(self,e):
        window=SQLiteWindow()
        window.open()
        

    def onclick_flask_run(self,e):
        app=self.getApp()
        app.run()

    def run(self,app=None):
        #th_sqlite=Thread(target=self.sqlite_onclick)
        #th_flask=Thread(target=self.onclick_flask_run)
        #th_sqlite.start()
        #th_flask.start()

        sqlite_button_window=tk.Tk()
        sqlite_button=tk.Button(sqlite_button_window,text='sqlite exploer')
        sqlite_button.bind('<1>',self.sqlite_onclick)
        sqlite_button.pack()

        flask_button=tk.Button(sqlite_button_window,text='run the flask')
        flask_button.bind('<1>',self.onclick_flask_run)
        flask_button.pack()
        
        sqlite_button_window.mainloop()
