import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''管理飞船的类'''
    def __init__(self, ai_game):
        '''初始化飞船与位置'''
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.current_life = self.settings.initial_life

        '''加载飞船图像与外接矩形'''
        self.image = pygame.image.load('png/player.png')
        self.rect = self.image.get_rect()

        '''新飞船在屏幕中间'''
        self.rect.midbottom = self.screen_rect.midbottom
        
        '''飞船生命计数'''
        self.life_count_img = pygame.image.load('png/life.png')
        width, height = self.life_count_img.get_size()

        # 打印图像尺寸
        print("飞船宽度:", width)
        print("图飞船高度:", height)
        self.life_count_rect = self.life_count_img.get_rect()

        self.life_count_rect.x = 0
       
        self.life_count_rect.y = 0


        #打印生命值
        GREEN = (0,255,0)
        BLUE = (0,0,128)
        fontObj = pygame.font.Font('freesansbold.ttf',28)
        self.t = self.settings.initial_life
        self.xSurfaecObj = fontObj.render('x'+str(self.t),True,GREEN,self.settings.bg_color)
        
        self.xRectObj = self.xSurfaecObj.get_rect()
        self.xRectObj.center=(55,13)
  
        
        '''飞船移动坐标x存储浮点数'''
        self.x = float(self.rect.x)
        '''移动标志'''
        self.moving_right = False
        self.moving_left = False
    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.life_count_img,self.life_count_rect)
        self.screen.blit(self.xSurfaecObj,self.xRectObj)
        #self.screen.blit(self.X_img,self.X_rect)
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #更新生命值
        self.t = self.current_life 
        fontObj = pygame.font.Font('freesansbold.ttf',28)  
        GREEN = (0,255,0)  
        
        self.xSurfaecObj = fontObj.render('x'+str(self.t),True,GREEN,self.settings.bg_color)  
        #更新飞船坐标
        self.rect.x = self.x
    