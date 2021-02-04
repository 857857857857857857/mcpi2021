from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random


x,y,z=mc.player.getTilePos()
for i in rang(20):
    r=random.randrange(1,5)
    
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x=x+4
         elif r==1:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x=x-4
         elif r==1:
        mc.setBlocks(x,y,z,x+,y,z+4,1)
        z=z+4
         if r==1:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z=z-4


for i in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+i
    
    for j in range(10):
        r=random.randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,r)






while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        
        if data==r:
            mc.postToChat('congratulation!')
            mc.setBlock(hit.pos,57)
            break
        
    elif data<r:
        mc.postToChat('bigger iD)
        
    elif data<r:
        mc.postToChat('samller iD)
        





myID=mc.getPlayerEntityId('CHARLESWANG')
mc.postToTitle(myID,'holle')




list2d=[[1,0,1,1,1,1,1]]
        [1,0,0,0,0,0,1]
        [1,0,1,1,1,0,1]
        [1,0,0,0,0,1,1]
        [1,0,1,1,0,0.1]
        [1,0,0,0,1,0,1]
        [1,1,1,1,1,0,1]

x,y,z=mc.player.getTilePos()
startx=x
startx=z

for j in range(4):
    for listld in list2d:
        
        for i in list1d:
            mc.setBlock(x,y,z,i)
            x=x+i
            
        x=startX
        z=z+1
    
    z=startZ
    y=y+i



























































































































































































































































