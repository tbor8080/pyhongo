from py.game.slot import *
import math
sl=Slot()
araru=[]

sl.probabilityOfSuccess()
length=[]
for i in range(0,50):
    source=f"""
    Limit:{sl.getLimit()}
    確率：{sl.getProbability()}
    slot : create > {sl.create()}
    slot : mode > {sl.getGameMode()}
    slot : leveron > {sl.leveron()}
    slot : game limit(単体) > {sl.getGameLimit()}
    """
    
    if sl.getGameLimit()==1280:
        length.append(source)
    # print(source)
# print(len(length),len(length)/50)
#sl.game()
sl.setGamelist()
print(sl.getGameProperty())