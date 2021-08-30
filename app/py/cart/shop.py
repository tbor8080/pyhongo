import os,sys,random,datetime

####################################
# Debug mode
debug_mode=True
####################################

def randseed(num=8):
    string=''
    if num > 0:
        for i in range(num):
            seed=random.randint(0,9)
            string+=str(seed)
    return string

class __Common__:

    def __init__(self):
        super()

    def className(self):
        return self.__class__.__name__
    
    def getNow(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def randomId(self,num=1):
        string=''
        chars=self.getChar()
        for i in range(num):
            seed=chars[random.randint(0,len(chars)-1)]
            string+=str(seed)
        return string
    
    def getChar(self):
        return 'abcdefghijklmnopqrstuvwxyz_0123456789'

class Shop(__Common__):
    """
    """

    __package__='__biz_shop__'
    __shop__={}

    def __init__(self,shopname=None):
        super().__init__()
        self.setShopName(shopname)
    
    def className(self):
        return self.__class__.__name__
    
    def create(self,tel=None,address=None):
    
        if self.__shopname is None:
            print('Shop Name is Required.')
            return None

        self.setTelephone(tel)
        self.setAddress(address)
        self.setShopId()

        shop={
            'num':len(self.get()),
            'id':self.getShopId(),
            'name':self.getShopName(),
            'telephone':self.getTelephone(),
            'address':self.getAddress(),
            'date':self.getRegistDate()
        }
        self.__shop__[self.getShopName()]=shop

    def get(self):
        return self.__shop__

    def getShopName(self):
        return self.__shopname

    def setShopName(self,name=None):
        if name is None and name=='':
            print('Shop Name is Required !')
            return None
        self.__shopname=name

    def getShopId(self):
        return self.__shopid

    def setShopId(self):
        prefix='Shop-'
        self.__shopid=prefix+str(len(self.get()))

    def getTelephone(self):
        return self.__phonenumber

    def setTelephone(self,number=None):
        self.__phonenumber=number

    def getAddress(self):
        return self.__address

    def setAddress(self,address=None):
        self.__address=address
    
    def getRegistDate(self):
        return super().getNow()
    
    
class Product(Shop):
    """"""
    __package__='__product__'
    __product__=[]

    def __init__(self,name=None):
        super().__init__()
        self.setProductName(name)
    
    def className(self):
        return self.__class__.__name__
    
    def get(self):
        return self.__product__
    
    def set(self):
        super()

    def create(self):

        if self.__productname is None:
            print('Product Name is Required !')
            return None
        else:
            self.setProductName(self.__productname)
        
        self.setProductId()

        product={
            'name':self.getProductName(),
            'productid':self.getProductId(),
            'date':self.getRegistDate(),
            }
        
        self.appendProduct(product)
        return self.get()

    def appendProduct(self,dic=None):
        if type(dic) is dict:
            self.__product__.append(dic)

    def getProductName(self):
        return self.__productname

    def setProductName(self,name=None):
        self.__productname=name
    
    def getProductId(self):
        return self.__productid

    def setProductId(self,id=None):
        self.__productid=super().randomId(len(super().getChar()))
    
    def getRegistDate(self):
        return super().getNow()

class Cart(Product):

    __cart__={}

    def __init__(self,name=None):
        super().__init__(name)
        print(super().__shop__)
        print(super().__product__)
    
    def add(self,user=None,product=None):
        try:
            self.__cart__['product'].append(product)
            self.__cart__['user'].append(user)
        except KeyError:
            self.__cart__['product']=[]

    def user(self):
        return self.__cart__['user']

    def setProduct(self):
        self.__setProductName()

    def __setProductName(self,name):
        pass

def Debug():
    print(f'This File is {__file__}.')

    Shop('楽天').create('090-xxxx-xxxx','東京都渋谷区')
    Shop('Yahoo').create()
    Shop('Line').create()

    Product('Test Product').create()
    
    Cart('Test Shop').create()

if debug_mode:
    Debug()
else:
    print(f'debug mode:{debug_mode}.')