from mcpi.minecraft import Minecraft
mc=Minecraft.create()


while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat('X:'+str(x)+'Y:'+str(y)+'Z:'+str(z)) 


 x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,15)
mc.setBlock(x,y+1,z,15)
mc.setBlock(x,y+2,z,15)
mc.setBlock(x,y+3,z,15)
mc.setBlock(x,y+4,z,15)
mc.setBlock(x,y+5,z,15)






    

x,y,z=mc.player.getTilePos()
mc.setBlock(x+1,y,z,15)
mc.setBlock(x-1,y,z,15)
mc.setBlock(x,y,z+1,15)
mc.setBlock(x,y,z-1,15)
mc.setBlock(x+1,y,z+1,15)
mc.setBlock(x-1,y,z-1,15)
mc.setBlock(x+1,y,z-1,15)


#






x,y,z=mc.player.getTilePos()
mc.setBlocks(x+10,y,z+10,x+10,y,,z-10,15)










import random
import time
x,y,z=mc.player.getTilePos()

while True:
    r=random.randrange(0,16
    mc.setBlock(x+5,y,z+5,x-5,y,z-5,35r)                       
    time.sleep(0.2)