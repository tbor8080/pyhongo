# /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,datetime,json
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd

__config__={}

def Dialog():
    __config__={}
    skip_to_enter='Skip to Enter >>'
    print('#'*32)
    print('# Setup to Web Application(auto generator).')
    print('# Installer is command line interface.')
    print('#'*32)
    q=input('+ Using GUI(Graphical User Interface)? >[Y/N] <Skip to Enter>:')
    default='./first_flask_app'
    if q.lower()=='y':
        root=tk.Tk()
        root.title('GUI Installer')
        root.geometry('480x480')
        layout=tk.Frame(root)

        doc_root_label=tk.Label(layout,text='Set document_root >>')
        doc_root_entry=tk.Entry(layout,text=default)
        doc_root_entry['state']=tk.DISABLED
        doc_root_entry.insert(tk.END,default)

        default='Automatic Create WebApp'
        web_title_label=tk.Label(layout,text='Set document_root >>')
        web_title_entry=tk.Entry(layout,text=default)
        web_title_entry['state']=tk.DISABLED
        web_title_entry.insert(tk.END,default)

        button=tk.Button(layout,text='Close',command=root.destroy)
        # layout
        doc_root_label.grid(column=0,row=0)
        doc_root_entry.grid(column=1,row=0)
        web_title_label.grid(column=0,row=1)
        web_title_entry.grid(column=1,row=1)
        button.grid(columnspan=2,row=2)
        layout.grid(row=0)
        root.mainloop()
    else:
        print('#'*32)
        __config__['current_directory']=os.path.dirname(__file__)
        print(f'++ Install directory > [ {__config__["current_directory"]} ]')
        # exit()
        __config__['doc_root']=input(f'+ Set document_root : default:{default} | {skip_to_enter}')
        # doc_root
        if __config__['doc_root']=='':
            __config__['doc_root']=default
        print(f'\t- Set to document root directory > [ {__config__["doc_root"]} ]')
        __config__['config']=__config__['doc_root']+'/manage/config.json'
        print(f'\t- Set to [config.json] path > [ {__config__["config"]} ]')
        __config__['app_json']='app.json'
        print(f'\t- Set to [app.json] path > [ {__config__["app_json"]} ]')
        __config__['app_py']='app.py'
        print(f'\t- Set to [app.py] path > [ {__config__["app_py"]} ]')

        __config__['web_title']=input(f'+ Set Title:')
        default='Automatic Create WebApp'
        if __config__['web_title']=='':
            __config__['web_title']=default
        print(f'\t- Set to web app title > [ {__config__["web_title"]} ]')

        __config__['PyFile']=input(f'+ Set Python File(default:main.py):( {skip_to_enter} )')
        # python file
        if __config__['PyFile']=='':
            __config__['PyFile']='main.py'
        print(f'\t- Set to python file > [{__config__["PyFile"]}]')

        __config__['TmplFile']=input(f'+ Set Template File ( default:main.html ):( {skip_to_enter} )')
        # template file
        if __config__['TmplFile']=='':
            __config__['TmplFile']='main.html'
        print(f'\t- Set to template filename > [{__config__["TmplFile"]}]')

        # database setup
        __config__['database']=input(f'+ Do you have to use database? :(Y/N) <{skip_to_enter} (Yes)>')
        if __config__['database'].lower()=='n' or __config__['database'].lower()=='no':
            __config__['database']=None

        elif __config__['database']=='' or __config__['database'].lower()=='y' or __config__['database'].lower()=='yes':
            
            # initialize
            __config__['database']={}

            print(f'++ Set Up Database:')

            default='sqlite'
            __config__['database']['type']=input(f'Use database type?]:(sqlite or pgsql)< {skip_to_enter}( {default} ) >')
            if __config__['database']['type']=='':
                __config__['database']['type']=default
            print(f'\t- Set to database type > [ {__config__["database"]["type"]} ]')

            # For SQLite
            if __config__['database']['type']=='sqlite':
                default='sample.db'
                __config__['database']['name']=input(f'Input: database file path:(default:{default})')
                if __config__['database']['name']=='':
                    __config__['database']['name']=default
                print(f'\t- Set to database name > [ {__config__["database"]["name"]} ]')

            # For PgSQL
            if __config__['database']['type']=='pgsql':

                # pgsql username
                default=None
                __config__['database']['user']=[]
                username=input(f'+ Input: database User Name:( {skip_to_enter}:(None) )')
                if username=='':
                    username=default
                __config__['database']['user'].append(username)
                while True:
                    if __config__['database']['user'][0] is None:
                        print('\t ** userneme is required.')
                        username=input(f'+ Input: database User Name:( {skip_to_enter}:(None) )')
                        if username=='':
                            username=None
                        __config__['database']['user'][0]=username
                    else:
                        break

                # pgsql password
                default=None
                passwd=input(f'+ Input: database User Password:( {skip_to_enter}:(None) )')
                if passwd=='':
                    passwd=str(default)
                text=''
                for w in range(len(passwd)):
                    if w==0:
                        text+=str(ord(passwd[w]))
                    else:
                        text+=f'-{str(ord(passwd[w]))}'

                passwd=text
                __config__['database']['user'].append(passwd)

                __config__['database']['user']=tuple(__config__['database']['user'])
                if __config__['database']['user'][0] is not None:
                    print(f'\t- Set to database user > [ {__config__["database"]["user"][0]},{__config__["database"]["user"][1]} ]')
                else:
                    print(f'\t- database user > [None]')

                # pgsql host
                default='localhost'
                __config__['database']['host']=input(f'+ Input: database host:({skip_to_enter}:{default})')
                if __config__['database']['host']=='':
                    __config__['database']['host']=default
                print(f'\t- Set to database host > [ {__config__["database"]["host"]} ]')

                # pgsql database name
                default='sample'
                __config__['database']['name']=input(f'+ Input: database name:(default:{default})')
                if __config__['database']['name']=='':
                    __config__['database']['name']=default
                print(f'\t- Set to database host > [ {__config__["database"]["name"]} ]')
                
                # pgsql port
                default=5432
                __config__['database']['port']=input(f'+ Input(option): database port:({skip_to_enter}{default})')
                if __config__['database']['port']=='':
                    __config__['database']['port']=default
                print(f'\t- Set to database port > [ {__config__["database"]["port"]} ]')

            # Switch handle
            __config__['switch']={
                'install':False,
                'flask':False,
                'gunicorn':False,
                'database':[False,__config__['database']['type']],
                'browser':[False,'chrome']
            }

            q=input(f'+ Do you need installer?>[Y/N]')
            if q.lower()=='y':
                __config__['switch']['install']=True
            print(f"\t- installer is run >{__config__['switch']['install']}")

            q=input(f'+ Do you need flask run?>[Y/N]')
            if q.lower()=='y':
                __config__['switch']['flask']=True
            print(f"\t- flask is run >{__config__['switch']['flask']}")

            if __config__['switch']['flask']:
                __config__['switch']['browser'][0]=True

            q=input(f'+ Do you need GUI window?>[Y/N]')
            if q.lower()=='y':
                __config__['switch']['database'][0]=True
            print(f"\t- {__config__['switch']['database'][1]} is run >{__config__['switch']['database'][0]}")            

        else:
            __config__['database']=None

    return __config__

def assave_app_json(**kwargs):
    (file,data)=(None,None)
    try:
        file=kwargs['file']
    except KeyError:
        file='app.json'
    try :
        data=kwargs['data']
    except KeyError:
        data={}
    
    with open(file,'wt') as fp:
        json.dump(data,fp,indent=4,ensure_ascii=False)

def is_file(file):
    if os.path.exists(file):
        return True
    return False

def get_app_json(**kwargs):
    file=None
    try:
        file=kwargs['file']
    except KeyError:
        file='app.json'
    if os.path.exists(file):
        with open(file,'rt') as fp:
            return json.loads(fp.read())

def assave_app_py(**kwargs):
    (file,data)=(None,None)
    try:
        file=kwargs['file']
    except KeyError:
        file='app.py'
    try:
        data=kwargs['data']
    except KeyError:
        data=None
    
    with open(file,'wt')as fp:
        fp.write(data)

def set_app_py(*args):
    sharp='#'*len('###################################################################################################')
    try:
        __config__=args[0]
    
        text=f"""# /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,datetime,json

debug_mode=True
if __name__=='app':
    debug_mode=False
# 
# + Web Application: DOCUMENT_ROOT
doc_root='{__config__['doc_root']}'

# Custumize
{sharp}
# + WebApplication Title:
web_title='{__config__['web_title']}'
# + Python&Template File Name
# For Python
PyFile='{__config__['PyFile']}'

# For HTML Template (by Bootstrap)
TmplFile='{__config__['TmplFile']}'
{sharp}
"""
        
        if type(__config__['database']) is dict:
            # print(type(__config__['database']))
            if __config__['database']['type']=='sqlite':
                text+=f"""
DatabaseType='{__config__['database']['type']}'
DatabaseName='{__config__['database']['name']}'
"""
            elif __config__['database']['type']=='pgsql':
                text+=f"""
DatabaseType='{__config__['database']['type']}'
DatabaseName='{__config__['database']['name']}'
DatabaseUser={__config__['database']['user']}
DatabaseHost='{__config__['database']['host']}'
DatabasePort={__config__['database']['port']}
"""

        text+="""# + Flask : Routing List Example.(Tuple List)
FlaskRouting=(
    {'path':'/', 'function':'index'},
)

def get_app_json(**kwargs):
    file=None
    try:
        file=kwargs['file']
    except KeyError:
        file='app.json'
    if os.path.exists(file):
        with open(file,'rt') as fp:
            return json.loads(fp.read())

config_json=get_app_json(file='app.json')

if debug_mode:
    print(config_json)

"""
        return text
    except ValueError:
        __config__['database']=None

    print('#'*64)

def module():
    json_file='app.json'
    py_file='app.py'
    if is_file(json_file):
        __config__=get_app_json(file=json_file)
        print(f'+ {json_file} is exists and installed file. this program finish!')
        answer=input(f'* Re-install: {json_file}？ (Y/N)')
        # Re-install
        if answer=='' or answer.lower()=='y':
            __config__=Dialog()
            assave_app_json(file=json_file,data=__config__)
            assave_app_py(file=py_file,data=set_app_py(__config__))
            print(f'+ {json_file} Re-install Success !!')
        else:
            print('Next...')
    else:
        __config__=Dialog()
        assave_app_json(file=json_file,data=__config__)
        assave_app_py(file=py_file,data=set_app_py(__config__))
        print(f'** install:{json_file}/{py_file} Success !!')

if __name__=='__main__' or __name__=='cui':
    module()
