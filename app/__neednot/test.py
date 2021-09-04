# /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,datetime,json

from cui import *

try:
    from app import *
except:
    print('Module File NotFound')
    print('% python __intaractive.py')
    exit()

# + Web Application: DOCUMENT_ROOT
# doc_root=doc_root

# Custumize
###################################################################################################
# + WebApplication Title:
# web_title=web_title

# + Python&Template File Name
# For Python
# PyFile=PyFile

# For HTML Template (by Bootstrap)
# TmplFile='main.html'

# + for database: type is sqlite or postgres sql(pgsql | psql)
#   - User Account: password is None OK.(but database security is no good, a lot of risk.)
#   - DatabaseUser=('<username>','<password>') or DatabaseUser=('<username>',None) or DatabaseUser=('<username>','')
#   - <password> is more than 8 charactors.
#   - For SQLite
#   - DatabaseUser=(None,None)
# DatabaseUser=('<db_user_account>','<db_access_passwd>')
# Database Type is sqlite or pgsql or psql.
# DatabaseType='sqlite' or DatabaseType='pgsql'
# mysql is not type.
# DatabaseType='pgsql'
# Database Name is Your database
# For SQLite(File): DatabaseName='<database_name>.db'
# DatabaseName='<database_name>'

# Default Database host & port
# DatabaseHost='localhost'
# DatabasePort=5432

# + Flask : Routing List Example.(Tuple List)
#FlaskRouting=(
#    {'path':'/', 'function':'index'},
#    {'path':'/doc', 'function':'document'},
#)



print(config_json)