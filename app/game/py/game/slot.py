import os,sys,datetime,random
try:
    from multipledispatch import dispatch
except ModuleNotFound:
    print('module: multipledispatch not found.')
    print('pip install multipledispatch')

class Slot:
    __slot__={}
    def __init__(self):
        super().__init__()
        self.initilize()
        
    def initilize(self):
        self.probability=[]
        # self.appendProbability()
        self.setLimit()

    @dispatch()
    def create(self):
        limit=self.getLimit()
        self.setGameMode()
        self.setCounter()
        self.setGameLimit()
        return (limit,self.counter(),self.getGameLimit())

    def setCharacter(self,name=None,value=None):
        return (name,value)

    def counter(self):
        return self.game_count
    
    def setCounter(self,count=0):
        self.game_count=count
    
    def chance(self):
        return 2**2
    
    def getLimit(self):
        return self.__limit

    def setLimit(self, limit=(2**10*1.25)):
        self.__limit=limit

    def probabilityOfSuccess(self):
        try:
            self.probability
        except ValueError:
            self.probability=[]

        for i in range(1,17):
            num=float(1/(2**i)*100)
            self.appendProbability(num)

            if i > 1:
                num=100-float(1/(2**i)*100)
                length=len(str(num).replace('99.',''))
                if length < 8:
                    num=format(num,'.1f')
                    num=float(num)
                    if num<99.8:
                        self.appendProbability(num)
        
        self.getProbability().sort()
        return self.getProbability()

    def getProbability(self):
        return self.probability
    
    def appendProbability(self, num=None):
        self.probability.append(num)
    
    def leveron(self):
        ( limit, num, count )=self.getLimit(), random.randint(0, self.getLimit()), self.counter()
        if count < limit:
            flag=True
            self.setCounter(count+1)
        elif count==limit:
            self.setCounter()
    
    def getGameLimit(self):
        return self.game_limit
    
    def setGameLimit(self):
        # 当たり
        game_limit=random.randint(1,self.getLimit())
        if game_limit > 1024:
            game_limit=self.getLimit()
        self.game_limit=game_limit

    def setGamelist(self):
        limit=int(self.getLimit())
        #for game in range(limit):
        print('1/2.5',limit/2.5,'回','Replay',1)
        self.setGameProperty('Replay', 2.5,2)
        self.setGameProperty('Bell', 4.75,3)
        self.setGameProperty('WaterMelonA', 75,4)
        self.setGameProperty('CherryA', 80,5)
        self.setGameProperty('ChanceReplay', 128)
        self.setGameProperty('ChancePropA', 225)
        self.setGameProperty('ChancePropB', 400)
        self.setGameProperty('CherryB', 1024)
        self.setGameProperty('Hit', self.getGameLimit())
        self.setGameProperty('Freeze', 65536)

    def getGameProperty(self):
        return self.__property

    def setGameProperty(self,propname=None,prop=None,num=None):
        limit=int(self.getLimit())
        property_number=float(format(1/prop,'.8f'))
        string=f"""property :{propname} is 1/{prop}({property_number*100}%). 
        [{limit}*{format(property_number,'.8f')}={limit*(property_number)}]
        {limit}回中、約{format(limit/prop,'.8f')}回
        """
        print(string)
        property={
            "num":num,
            "propname":propname,
            "count":format(limit/prop,'.4f'),
            "limit":limit,
            "hit":self.getGameLimit(),
            "%":property_number*100
        }
        try:
            self.__property[f"{propname}"]=property
        except AttributeError:
            self.__property={}
            

    def game(self):
        self.setGamelist()
        # print(inputs)
        while True:
            input('<Press Enter>')
            
            if self.counter()==self.getGameLimit():
                print('当たり',self.counter())
                self.setCounter()
                break
            else:
                print('はずれ')
                self.leveron()
    
    def getGameMode(self):
        return self.__mode

    def setGameMode(self):
        self.__modes=['a','b','heaven-a','heaven-b']
        mode=random.randint(0,8)
        if mode <= 4:
            self.__mode=self.__modes[0]
        else:
            self.__mode=self.__modes[1]

    def gameModeUp(self):
        if self.__mode<len(self.__modes):
            self.__mode+=1
    
    def gameModeDown(self):
        self.__mode=0