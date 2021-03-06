from tkinter import *
import copy

class Platformer:

    player = None
    gravity = 10
    gravityIsOn = True
    collisionSprites = []
    collisionGraphics = []


    def __init__(self, window, grid, draw, action):
        self.window = window
        self.grid = grid
        self.draw = draw
        self.action = action

    def start(self): #TODO: FIX BUG LATER
        try:
            self.moveSpriteIfKeyPressed()
            self.doGravity()
        except:
            print("ERROR: Player does not exist.")

    def restart(self):
        self.collisionGraphics.clear()
        for x in range(self.grid.getHorizontalSize()):
            for y in range(self.grid.getVerticalSize()):
                for spr in self.grid.getSprites(x,y):
                    if spr.getName() == self.getPlayer().getName():
                        self.setPlayer(spr)
        for collSpr in self.collisionSprites:
            if spr.getName() == collSpr.getName():
                self.findAllColissionsInGrid(spr)

    def moveSpriteIfKeyPressed(self):
        if self.action.getKeyPressed() == 'd':
            self.draw.moveSprite(self.player, 10, 0)
        elif self.action.getKeyPressed() == 'a':
            self.draw.moveSprite(self.player, -10,0)

    def doGravity(self):
        self.draw.moveSprite(self.player, 0, self.gravity)
        x1, y1, x2, y2 = self.draw.graphic.bbox(self.player.getGraphic())
        overlaps = self.draw.graphic.find_overlapping(x1, y1, x2, y2)
        print(overlaps)
        for graphic in overlaps:
            if graphic in self.collisionGraphics:
                self.setGravity(0)
                break
            else:
                self.setGravity(10)

    def setPlayer(self, sprite):
        self.player = sprite

    def getPlayer(self):
        return self.player

    def addCollisionSprite(self, sprite):
        self.collisionSprites.append(sprite)
        self.findAllColissionsInGrid(sprite)

    def setGravity(self, gravity):
        self.gravity = gravity

    def findAllColissionsInGrid(self, sprite):
        for x in range(self.grid.getHorizontalSize()):
            for y in range(self.grid.getVerticalSize()):
                for spr in self.grid.getSprites(x, y):
                    if spr.getName() == sprite.getName():
                        self.collisionGraphics.append(spr.getGraphic())




