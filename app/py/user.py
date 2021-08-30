

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
    
    def get(self):
        return self.__user__

    def create(self,firstname=None,lastname=None,nickname=None):
        self.setName(firstname,lastname)

    def addProfile(self):
    
    def getClass(self):
        return self.__class__.__name__
    
    def getName(self):
        return self.__user__['name']

    def setName(self,firstname=None,lastname=None):
        self.__name=None
        if firstname is not None and lastname is not None:
            self.__user__['name']={'firstname':firstname,'lastname':lastname}
    
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

    def setPribate(self,privary=True):
        self.private=privacy

    def setLanguage(self,lang=None):
        if lang is not None:
            self.__language=lang
        else:
            print('Language Not Found Error!!')
            return None

class Password:

    __password__=''

    def __init__(self):
        pass
    
    def create(self):
        pass
    
    def get(self):
        pass
    

class Ryohei(User):
    def __init__(self):
        super().__init__()

class Login(User,Password):
    def __init__(self):
        super().__init__()

    def addUser(self,username=None):
        self.setId()

def Debug():
    if debug_mode:
        people=Ryohei().create('Ryohei','Suga')
        print(Ryohei().get())
    
Debug()