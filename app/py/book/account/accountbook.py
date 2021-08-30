def ModuleNotFounds(modulename=None):

    return f"""
    !Cauttion: {modulename} is Not Found.
    =====================================
    pip install {modulename}
            or
    pip -r requirements.txt
    =====================================
    - Read the .md File.
    """

try:
    from multipledispatch import dispatch
except ModuleNotFound:
    ModuleNotFounds('multipledispatch')


class Company:

    __company__={}

    def __init__(self,name=None):
        super()
    
    @classmethod
    def setName(cls,name=None):
        cls.__company__['name']=name
        if cls.__company__['name'] is None:
            print('Comapany name is Required.')
            return cls.__company__['name']
    
    @classmethod
    def create(cls,name=None):
        cls.setName(name)
    
    def regist(self,):
        super()
    
    @classmethod
    def gets(cls):
        return cls.__company__
    
    @dispatch(str)
    def insert(self):
        pass

class AccountBook(Company):
    
    """
        __accountbook__={
            'comapany':inherit_model_company,
            'list':{
                'document-number:index':{
                    'documents_id':index
                    'title':'title',
                    'object':[free],
                    'regist_date':'',
                    'update':''
                }
            }
        }
    """

    __accountbook__={}
    __package__='__accountbook__'

    def __init__(self):
        
        self.setList()
        self.__accountbook__['company']=Company.gets()
    
    @classmethod
    def create(cls,title=None):
        cls.__setList()
        id=cls.getId()
        cls.__accountbook__['company']=Company.gets()
        cls.__accountbook__['list'][id]={'id':id,'index':len(cls.__accountbook__['list'])}
        cls.__accountbook__['list'][id]['title']=title

    @classmethod
    def __setList(cls):
        try:
            cls.__accountbook__['list']
        except KeyError:
            cls.__accountbook__['list']={}

    @classmethod
    def getId(cls):
        return cls.__package__+str(len(cls.__accountbook__['list']))

    def appends(self,object=None,id=None):
        if type(object)==dict:
            if id is None:
                id=self.getId()
            self.__accountbook__['list'][id]['object']=object
    
    def setList(self):
        try:
            self.__accountbook__['list']
        except KeyError:
            self.__accountbook__['list']={}

    @classmethod
    def gets(cls):
        return cls.__accountbook__

    # dispatcher
    # multi method:
    #    - get
    #    - search
    #    - insert
    #    - add

    @dispatch()
    def add(self):
        pass

    # - get
    @dispatch()
    def get(self):
        return AccountBook.gets()
    
    @dispatch(object)
    def get(self,object):
        return AccountBook.__accountbook__['company']

    @dispatch(str)
    def get(self,id):
        return AccountBook.__accountbook__['list'][id]

    # - search
    @dispatch()
    def search(self):
        return """AccountBook.search(0)
            or
AccountBook.search('title')

        """
    
    @dispatch(int)
    def search(self,num):
        a_list=AccountBook.__accountbook__['list']
        for lists in a_list:
            if a_list[lists]['index']==num:
                return a_list[lists]
        return None
    
    @dispatch(str)
    def search(self,title):
        a_list=AccountBook.__accountbook__['list']
        for lists in a_list:
            if a_list[lists]['title'] in title:
                return a_list[lists]
        return None

class RegistBooks(AccountBook):
    __registbook__={}
    def __init__(self):
        super().__init__()
    
    @dispatch()
    def add(self):
        return None
    
    @dispatch(str)
    def add(self,value):
        pass
    
    @dispatch(str,str)
    def add(self,key,value):
        pass

    @dispatch(list)
    def add(self,lists):
        test=AccountBook.gets()
    
    @dispatch(tuple)
    def add(self,tuples):
        test=AccountBook.gets()

class ManagementLedge(AccountBook):
    __managementledge__={}
    def __init__(self):
        super().__init__()

def Debug():

    Company.create('◯×商事')

    AccountBook.create('〇〇台帳')
    AccountBook.create('Sample台帳02')

    RegistBooks.create('まる')

    print(RegistBooks.gets())
    print(RegistBooks.get(object=RegistBooks))
    print(RegistBooks.get(id='__accountbook__0'))

    # print(RegistBooks.search())
    print(RegistBooks.search(num=2))
    print(RegistBooks.search(title='Sample台帳02'))

Debug()
