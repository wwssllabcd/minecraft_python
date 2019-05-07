from mcpi.minecraft import Minecraft


def go_home(mc):
    mc.player.setPos(24.544259711177887,8.0,19.06017319194089)

def make_block(mc, blockId):
    pos = mc.player.getPos()
    pos.x +=1
    for i in range(10):
        mc.setBlock(pos.x+i, pos.y, pos.z, blockId)
        mc.setBlock(pos.x+i, pos.y+1, pos.z, blockId)
        mc.setBlock(pos.x+i, pos.y+2, pos.z, blockId)
        mc.setBlock(pos.x+i, pos.y+3, pos.z, blockId)


def make_cube(mc, length, blockId):
    pos = mc.player.getPos()
    pos.x+=1
    for x in range(length):
        for y in range(length):
            for z in range(length):
                mc.setBlock(pos.x+x, pos.y+y, pos.z+z, blockId)
   


mc = Minecraft.create()

#mc.postToChat("Hello world")
pos = mc.player.getPos()

print(pos)
x, y, z = mc.player.getPos()

#Teleport
#mc.player.setPos(x, y+1000, z)

#Set block
#mc.setBlock(x+1, y, z, 1)

#go_home(mc)

AIR=0
diamondOrg = 56
DIAMOND_BLOCK = 57
ironORg = 15
brickBlock = 45
blockId = diamondOrg # 紅磚

#make_block(mc, brickBlock)

make_cube(mc, 20, DIAMOND_BLOCK)

#go_home(mc)

