class AutoBrowser:
    def __init__(self):
        self.set_driver()

    def get_driver(self):
        return self.driver

    def set_driver(self,*option):
        self.set_options(option)
        self.driver=Chrome(options=option)

    def set_options(self,**args):
        return ChromeOptions(**args)
    
    def set_javascript(self,function=None,argument=(*argc,**argv),**kwargs):
        try:
            id=self.get_id(kwargs['target'])
        except:KeyError:
            print('id is Key Not Found.')

        return function(argument[0],argument[1])
    
    def get_target(self,id=None):
        try:
            return self.__element[id]
        except KeyError:
            print('Key Not Found.')
            return False

    def set_target(self,**id):
        for kw in id:
            self.__element[kw]=id[kw]
        
    def loged(self,file=None,data=None):
        with open(file,'a') as fp:
            fp.write(data)

def Debug():
    selen=AutoBrowser()
    selen.get_driver().get(url)
    selen.set_target(__elem_01='readable')
    selen.set_target(__elem_02='swich_to')
    selen.set_javascript(function=selen.sample,argument=((1,2,3),{title='a'},id=selen.get_target('__elem_01'))
    __elem_01=selen.get_target('__elem_01')
    javascript_code=f'''
    $('{__elem_01}').click(function(event){

    });
    '''
    