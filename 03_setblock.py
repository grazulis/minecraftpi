from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

# set single block
x, y, z = mc.player.getPos()
mc.setBlock(x+3, y, z, block.STONE.id)

# set multiple blocks
stone = 1
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)