import json,pprint,datetime

try:
    from multipledispatch import dispatch
except ModuleNotFound:
    ModuleNotFounds('multipledispatch')

__debug_mode=False

class Matrix:

    """
    - Matrix Class

        + Matrix()
            - Constractor
        + title('Sample Matrix Data')

        + property(key0='value0',key1='value1',....)
            return **kwargs
            - Matrix Property

        + column('A','B','C','D')
            - Set Column Name

        + add('a','b',1,)
            - Set Data
        
        + add_to_dict(A='a',B='b',C=1)
            -set Column & Data

        + update(0,'A','bc')
            or
        + update(index=0,column='A',value='bc')

        + delete(3)
            or
        + delete(index=2)

        + column_property(1,'A',(('key','value'),('key','value')))
            or
        + column_property(index=0,column='B',**option={key='value', date='2021-08-26',...})

        + save:
        + save_as_json()
        + as_json()

        example)
            mtrx=Matrix()
            mtrx.title('Sample Matrix')
            mtrx.property(filename='management.json',filetype='application/json',)

            # + add data :how to 01
            mtrx.column('index','id','key','value')
            mtrx.add(1,'column-id-a','test','データ')

            # + or
            # + add data :how to 02
            mtmx.add_to_dict(index=2,id='column-id-b',key='test1',value='データ1')

            # dump to Matrix Class Data
            # not argument == mtmx.dump('list') default 'list' data
            # + dump is not return
            mtmx.dump()

            # + or
            mtmx.dump('list')
            mtmx.dump('header')
            mtmx.dump('property')

            # + get is return
            mtmx.get(2) # => index number
            # + or
            mtmx.get() => all data('list')

    """
    __sheet__={
        'header':[],
        'list':[],
        'property':{},
    }

    __package__='__matrix__'

    def __init__(self):
        super().__init__()
        self.init()

    def create(self):
        pass
    
    def init(self,num=256):
        for i in range(num):
            self.__sheet__['header'].append(f'column-{i}')

    def column(self,*lists):
        for num in range(len(lists)):
            self.__sheet__['header'][num]=lists[num]
    
    def property(self, **kwargs):
        """
        + self.property(title='test')
            - title
            - description
            - registdate
            - update
            - filetype
            - filesize
        """
        try:
            self.__sheet__['property']['title']=kwargs['title']
        except KeyError:
            self.__sheet__['property']['title']=None

        try:
            self.__sheet__['property']['description']=kwargs['description']
        except KeyError:
            self.__sheet__['property']['description']=None

        try:
            self.__sheet__['property']['filetype']=kwargs['filetype']
        except KeyError:
            self.__sheet__['property']['filetype']=None

        self.__sheet__['property']['update']=datetime.datetime.now()
        
    def add(self,*lists):
        dic={}
        if len(self.__sheet__["header"])<len(lists):
            error_message=f"""index out of range.
    header: {self.__sheet__["header"]}
    list: {lists}
"""
            print(error_message)
            exit()

        for num in range(len(lists)):
            dic[f'{self.__sheet__["header"][num]}']=lists[num]
            
        self.__sheet__['list'].append(dic)

    def add_to_dict(self,**kwarg):
        self.__sheet__['list'].append(kwarg)
    
    def update(self,index=None,column=None,value=None):

        if index is None and type(index) is not int:
            print(f'+ {index} is "None Type" or "Type is not int"')
            exit()

        if column is None and type(column) is not str:
            print(f'+ {column} is "Not Found" or "Type is not str"')
            exit()

        try:
            self.__sheet__['list'][index][column]
        except KeyError:
            print(f'+ Error: {column} > name is not found.')
            exit()

        self.__sheet__['list'][index][column]=value
    
    def delete(self,index=None):

        if index is None and type(index) is not int:
            print('+ argument[index] is "None Type" or "Type is not int"')
            exit()

        if index < self.length():
            return self.__sheet__['list'].pop(index)
        
    def clear(self,key='list'):
        self.__sheet__['list'].clear()
    
    def dump(self,key='list',num=0):
        sheet=self.__sheet__
        
        try:
            sheet=eval(f'self.get_{key}(num)')
        except AttributeError:
            sheet=self.get_list()

        print(sheet)
    
    def get(self,index=None):
        lists=lists=self.__sheet__['list']

        if type(index) is int and index < len(lists):
            lists=self.__sheet__['list'][index]

        return lists

    def get_header(self,num=None):
        return self.__sheet__['header']

    def get_list(self,num=0):
        if num > 0:
            return self.__sheet__['list'][:num]
        return self.__sheet__['list']
    
    def get_property(self,property=None):
        if property is None:
            exit()
        try :
            return self.__sheet__['property'][property]
        except KeyError:
            print(f'{property} is Not Found.')
            print('property is title or description or filename or filepath or filetype or update or registdate')
            exit()
        return self.__sheet__['property']
    
    def length(self,name='list'):
        try :
            self.__sheet__[name]
        except KeyError:
            name='list'

        return len(self.__sheet__[name])
    
    def __save_as_json(self,filename='sample.json',data=None):
        if data is None and (type(data)==list or type(data)==dict):
            data=self.dump('list')
        elif type(data)==str:
            print('Error :Data Type is "str"')
            exit()

        with open(filename,'wt') as fp:
            json.dump(data,fp,ensure_ascii=False,indent=4)
            # fp.write(str(data))

    def __to_json(self,data=None):
        if data is None:
            data=self.dump('list')
        return json.dumps(data)

# Daicho
class Ledge(Matrix):
    def __init__(self):
        super().__init__()
        self.init(256)

# Data Stored text data.
# No Database Application
class StoredText(Matrix):
    def __init__(self):
        super().__init__()
        self.init(256)
    
    def sample(self):
        self.property(title='Sample Stored Text Data',filetype='text/plane')
        self.column('index','column01','column02')
        self.add(1,'testdata','testdata')
        print('save method is as_save_json()')
        print(self.__doc__)
        return self.get()

def Debug():
    st=Matrix()
    st.property(title='サンプルテーブル',description='概要',filename='prop.json',filetype='application/json')
    st.column('index','lang','country','name','age','sex','domain')
    for i in range(10):
        st.add(i,'ja','Japanese','Ryohei Suga')

    # st.add_to_dict(index=i,lang='ja',country='Japanese',name='Full Name',age=99)
    # st.save_as_json()
    # pprint.pprint(st.as_json())
    #st.update(index=0,key='lang',value='en')
    #st.update(0,'lang','in')
    print(st.delete(8))
    print(st.get(7))
    #st.clear()
    st.dump()
if __debug_mode:
    Debug()