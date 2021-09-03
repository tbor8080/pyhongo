import os,sys,datetime,json,random

debug_mode=True

class User:
    """
        User Class:
            - firstname
            - lastname
            - firstname
            - firstname
            - nickname
            - sex
            - age
            - birthday
    """
    
    __package__='__user__'

    # Private
    
    __user__={}

    def __init__(self):
        pass
    
    def get(self,id=None,key=None):
        return self.__user__

        if type(id) is str and id in self.id_list(key):
            return self.__user__[id]
    
    def localize(self,lang='ja'):
        set.location=lang

    def add(self,firstname=None,lastname=None,nickname=None):
        self.setUserId()
        self.setIndex()
        self.setName(firstname,lastname)
        if nickname is None:
            nickname=f'user_{str(len(self.get()))}'
        self.setNickName(nickname)
        self.setPrivate(True)
        self.setKeys()

    def addProfile(self):
        pass
    
    def id_list(self,key=None):
        if key is None:
            return tuple(self.__user__.keys())
        return tuple(key.keys())
    
    def setKeys(self):
        key_list=self.__user__.keys()
        self.__list=tuple(key_list)

    def setIndex(self):
        self.__user__[self.getUserId()]['index']=len(self.__user__)

    def getUserId(self):
        return self.__uniqueid
    
    def setUserId(self):
        self.__uniqueid=f'__user_{UniqueId().get()}'
        self.__user__[self.__uniqueid]={'user_id':self.__uniqueid}
    
    def getClass(self):
        return self.__class__.__name__
    
    def getName(self):
        return self.__user__['name']

    def setName(self,firstname=None,lastname=None):
        self.__name=None
        if firstname is not None and lastname is not None:
            self.__user__[self.getUserId()]['name']={
                'firstname':self.shadow(firstname),
                'lastname':self.shadow(lastname),
            }

    def setNickName(self,nickname=None):
        if nickname is not None:
            self.__user__[self.getUserId()]['nickname']=self.shadow(nickname)
    
    def shadow(self,arg=None):
        (string,dummy)='',''
        for chars in range(len(arg)):
            if chars > 0:
                string+='-'
            seed=random.randint(0,7)
            string+=str(f'{ord(arg[chars])}:{seed}')
            dummy+=chr(ord(arg[chars])+seed)
        return {'*':'*'*len(arg),'charcode':string,'data':arg,'dummy':dummy,}
    
    def getSex(self):
        return self.__sex

    def setSex(self,sex=0):
        self.__sex=sex
    
    def getAge(self):
        return self.__age

    def setAge(self,age=None):
        self.__age=age

    def getBirthday(self):
        return self.__birthday

    def setBirthday(self,yyyy=1970,mm=1,dd=1):
        self.__birthday={'year':yyyy,'month':mm,'day':dd}
    
    def getPrivate(self):
        return self.private

    def setPrivate(self,privacy=True):
        self.__user__[self.getUserId()]['private']=privacy

    def setLanguage(self,lang=None):
        if lang is not None:
            self.__language=lang
        else:
            print('Language Not Found Error!!')
            return None

class Password:

    __password__={
        'text':None,
        'seed':'seed:abcdefghijklmnopqrstuvwxyz01234567890-_*',
    }

    def __init__(self):
        pass
    
    def create(self,password=None,num=8):
        if password is None:
            exit()
        if len(password)<num:
            print(f'Password length more than {num} Charactors.')
            exit()
        text+='*'*len(password)
        self.__password__['shadow']=text
        self.__password__['text']
    
    def get(self):
        pass
    
    def encrypt(self):
        random_num=ramdom.randint(0,len(self.__password__)-1)
    
    def shadow(self):
        pass
    
    def save(self,filename='user.json',data=None):
        with open(filename,'wt') as fp:
            json.dump(data,fp,indent=4,ensure_ascii=False)

class UniqueId:
    __alphabet='abcderghtjklmnopqrstuvwxyz01234567890_'
    def __init__(self):
        self.set()

    def set(self):
        char=''
        for i in range(16):
            num=random.randint(0,len(self.__alphabet)-1)
            char+=self.__alphabet[num]
        self.__unique=char

    def get(self):
        self.set()
        return self.__unique
    
    def encode(self):
        pass

class Login(User):
    def __init__(self):
        super().__init__()

class Login(User,Password):
    def __init__(self):
        super().__init__()

    def addUser(self,username=None):
        self.setId()

def Debug():
    if debug_mode:
        if len(User().get()) == 0:
            User().add('webapp','user')
            User().add('webapp','user')
            print(Login().get())
            Login().save(data=Login().get())
            pass
        with open('user.json','rt') as fp:
            data=json.load(fp)
        key=list(User().id_list(data))
        search_id='__user_rd1tog9gmtrt46tt'
        print(search_id in key,User().id_list(data))
    
Debug()