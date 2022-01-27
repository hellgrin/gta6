# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
 
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        base.camLens.setFov(90)
        self.land.loadLand('land.txt')
        x,y = self.land.loadLand('land.txt')
        hero = Hero((x//2, y//2, 2), self.land)

game = Game()
game.run()