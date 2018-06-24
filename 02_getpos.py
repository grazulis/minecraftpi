from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# get position
x, y, z = mc.player.getPos()

#teleport
mc.player.setPos(x, y+100, z)