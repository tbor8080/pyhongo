# /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,datetime,json

debug_mode=True
if __name__=='app':
    debug_mode=False
# 
# + Web Application: DOCUMENT_ROOT
doc_root='./first_flask_app'

# Custumize
###################################################################################################
# + WebApplication Title:
web_title='sample'
# + Python&Template File Name
# For Python
PyFile='main.py'

# For HTML Template (by Bootstrap)
TmplFile='main.html'
###################################################################################################

DatabaseType='sqlite'
DatabaseName='test.db'
# + Flask : Routing List Example.(Tuple List)
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

