# /usr/bin/env python
# -*- coding: utf-8 -*-

class ForSQL:
    
    #
    """
    Database SQL Wrapper Base Class
    """
    __packege__='__database__'
    
    def __init__(self):
        self.scheme={}
        self.setDatabaseName(None)
    
    def getClassName(self):
        return self.__class__.__name__
    
    def getDoc(self):
        return self.__doc__
    
    def getScheme(self):
        return self.scheme

    def getDB(self):
        return self.dbname
    
    def setDatabaseName(self,dbname=None):
        self.dbname=dbname

    def createDatabaseName(self,dbname=None):
        self.setDatabaseName(dbname)

    def getTableName(self):
        return self.tblname

    def setTableName(self, tblname=''):
        if type(tblname) is str and len(tblname)>0:
            self.tblname=tblname
            self.scheme[self.tblname]=[]
            self.scheme[self.tblname].append({})
    
    def getTableScheme(self):
        return self.scheme[self.tblname]
    
    def setTable(self):
        self.scheme[self.tblname].append({})

    def appendColumn(self, columnname='', datatype='', const=None, primarykey=(None, False), unique=False):
        self.setTable()
        self.appendTableColName(columnname)
        self.appendTableColType(datatype)
        self.appendTableColConst(const)
        self.appendTableUnique(unique)
        if len(primarykey)>0:
            (name,auto)=primarykey
            self.appendPrimaryKey(name,auto)

    def appendTableColName(self, name=''):
        num=len(self.scheme[self.tblname])-1
        self.scheme[self.tblname][num]['name']=name

    def appendTableColType(self, types):
        num=len(self.scheme[self.tblname])-1
        self.scheme[self.tblname][num]['type']=types.upper()
    
    def appendTableColConst(self, const=None):
        num=len(self.scheme[self.tblname])-1
        if const is not None:
            self.scheme[self.tblname][num]['const']=const.upper()
    
    def appendTableUnique(self,key=False):
        num=len(self.scheme[self.tblname])-1
        if key:
            self.scheme[self.tblname][num]['unique']=key

    def appendPrimaryKey(self, colname=None, auto=False):
        num=len(self.scheme[self.tblname])-1
        self.scheme[self.tblname][num]['constraint']={}
        constList=['PRIMARY KEY','UNIQUE KEY','FOREIGN KEY']
        if colname is not None:
            self.scheme[self.tblname][num]['constraint']['column']=colname
        if auto:
            self.scheme[self.tblname][num]['constraint']['auto']='auto increment'.upper()
    
    # PRAGMA table_info('**Table Name**')
    # Table Column

    def createTableColumnListsCode(self,tblname=''):
        text=''
        if tblname!='':
            self.setTableName(tblname)
            text=f'PRAGMA table_info({self.getTableName()});'
        return text
    
    def getTableColumnLists(self, tblname=''):
        self.setTableName(tblname)
        conn=self.getConnection()
        cur=self.getCursor()
        cur.execute(self.createTableColumnListsCode(self.getTableName()))
        lists=cur.fetchall()
        conn.close()
        self.tblList=[]
        for i in range(len(lists)):
            self.tblList.append(lists[i][1])
            # print(lists[i][1])
    
    # code to select syntax
    def selectCode(self,columns=[],where={}):
        """
        SELECT tbl_name,sql from sqlite_master;
        SELECT * from sqlite_master
        WHERE tbl_name='{table_name}' AND type='table';
        # 
        PRAGMA table_info({COMPANY_DOCUMENT_LIST})

        """
        tblname=self.getTableName()
        text=''
        if tblname!='':
            text='SELECT '
            if len(columns)==0 and type(columns) is list:
                text+='*'
            elif len(columns)>0 and type(columns) is list:
                for i in range(0,len(columns)):
                    text+=columns[i]
                    text+=','
            text+=' from '
            text+=tblname
            text+=';'
        return text
    
    def __inserts(self,data=[]):
        """
        INSERT INTO {}
        VALUES
        (?,?,?,?,?),(?,?,?,?,?),(?,?,?,?,?)
        ;
        """
        tblname=self.getTableName()
        text='INSERT INTO {tablename} VALUES (?,?,?,?,?),()'
    
    def __update(self,data=(),where=[]):
        """
        UPDATE {COMPANY_DOCUMENT_LIST}

        SET {company_deploy}='{財務}'
        WHERE {document_name}='{TEST1}' AND {document_num}={19}; .... Loop
        ({'key':'value'},{'key':'value'}) => where[0]['key']
        """
        tblname=self.getTableName()
        (column,coldata)=data

        sql=f"""UPDATE {tblname}
        SET {column}=?
        """
        sql+="""
        WHERE 
        """

        # Loop: 
        for i in range(0,len(where)):
            for wh in where:
                sql+="""
                {wh}='{where[wh]}'
                """
        # Loop: 

        sql+="""
        ;
        """
        return sql

    def __delete(self,data={}):
        tblname=self.getTableName()
        text='DELETE from {tblname} WHERE id=""'

    # SQL Code ===========================================================================

    def getCreateDBCode(self):
        return f'''CREATE DATABASE {self.getDB()};'''

    def getCreateTableCode(self):
        text=''
        for sc in self.getScheme():
            tablename=sc
            
            primary_key={'column':None,'auto':None}
            length=self.getScheme()[tablename]
            maximize=len(length)-1
            
            text+=f'''
            CREATE TABLE '{tablename}'('''
            
            # print(maximize)

            for num in range(0, len(self.getScheme()[tablename])):
                scheme=self.getScheme()[tablename][num]
                print(scheme)
                (name,types,val)=None,None,None
                if 'name' in scheme:
                    name=scheme['name']
                if 'type' in scheme:
                    types=scheme['type']
                
                if 'const' in scheme:
                    val=scheme['const']

                if 'constraint' in scheme and 'column' in scheme['constraint']:
                    primary_key['column']=scheme['constraint']['column']

                if 'constraint' in scheme and 'auto' in scheme['constraint']:
                    primary_key['auto']=scheme['constraint']['auto']

                text+=f'''
                "{name}" {types} {val}'''
                if num < maximize:
                    text+=','

            if primary_key['column'] is not None and primary_key['column']!='':
                column=primary_key['column']
                text+=f',\n\t\tPRIMARY KEY("{column}"'

            if primary_key['auto'] is not None:
                auto=primary_key['auto']
                text+=f', {auto}'

            text+=''')
            );
            '''
        return text
    
    def getSelectCode(self,tblname='',columns=()):
        text=f'SELECT from {tblname}'
        return text
    
    def show(self,text):
        print(text)