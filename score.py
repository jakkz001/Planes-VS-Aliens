import pygame
#fontObj = pygame.font.Font('freesansbold.ttf',28)
#RED =(255,0,0)
class Score:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        #fontobj = pygame.font.Font('freesansbold.ttf',28)
        self.point = self.settings.initial_point
        RED =(255,0,0)
        
        #self.pointSurfaecObj = fontobj.render(f"SCORE:{self.point}",True,(255,0,0))
        #self.pointRectObj = self.pointSurfaecObj.get_rect()
        #print("pingmu宽度:", self.screen_rect.right)
        #self.pointRectObj.right=self.screen_rect.right
        #print("字体宽度:", self.pointRectObj.left)
        #self.pointRectObj.top = 0
        #self.pointRectObj.topright = self.screen_rect.topright



    def update(self):
        fontobj = pygame.font.Font('freesansbold.ttf',28)
        RED =(255,0,0)
        self.pointSurfaecObj = fontobj.render(f"SCORE:{self.point}",True,(255,0,0))
        self.pointRectObj = self.pointSurfaecObj.get_rect()
        self.pointRectObj.topright = self.screen_rect.topright
        #self.pointSurfaecObj = fontobj.render(f"SCORE:{self.point}",True,(255,0,0))
        self.screen.blit(self.pointSurfaecObj,self.pointRectObj)


    def point_bonus(self,add_point):
        self.point += add_point