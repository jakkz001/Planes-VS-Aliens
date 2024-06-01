import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''代表单个外星飞船的类'''
    def __init__(self, ai_game):
        '''初始化外星飞船并设置初始位置'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('png/Enemies/enemyBlack1.png')
        self.rect = self.image.get_rect()
        self.current_blood = self.settings.alien_blood

        self.rect.x = self.rect.width  #这代表飞船右边缘为起点，避免飞船超出屏幕
        self.rect.y = 0                 #self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        '''向下移动外星人'''
        self.y += self.settings.alien_speed
        self.rect.y = self.y

        
class AlienTwo(Sprite):
    '''二号飞船'''
    def __init__(self, ai_game):
        '''初始化外星飞船并设置初始位置'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('png/Enemies/enemyBlack2.png')
        self.rect = self.image.get_rect()
        self.current_blood = self.settings.alien_two_blood

        self.rect.x = self.rect.width  #这代表飞船右边缘为起点，避免飞船超出屏幕
        self.rect.y = 0                 #self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_two_speed
        self.rect.y = self.y

class AlienThree(Sprite):
    '''三号飞船'''
    def __init__(self, ai_game):
        '''初始化外星飞船并设置初始位置'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('png/Enemies/enemyBlack4.png')
        self.rect = self.image.get_rect()
        self.current_blood = self.settings.alien_three_blood

        self.rect.x = self.rect.width  #这代表飞船右边缘为起点，避免飞船超出屏幕
        self.rect.y = 0                 #self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        '''运动到屏幕一半时静止'''
        if self.y < self.screen.get_rect().height/2:
            self.y += self.settings.alien_three_speed
            self.rect.y = self.y
        else:
            self.rect.y = self.y

class AlienMeteorolite(Sprite):
    '''陨石'''
    def __init__(self, ai_game):
        '''初始化外星飞船并设置初始位置'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('png/meteorBig.png')
        self.rect = self.image.get_rect()
        self.current_blood = self.settings.meteorolite_blood

        self.rect.x = self.rect.width  #这代表飞船右边缘为起点，避免飞船超出屏幕
        self.rect.y = 0                 #self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.meteorolite_speed
        self.rect.y = self.y

class AlienBullet(Sprite):
    '''外星飞船子弹'''
    def __init__(self,ai_game,alien_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('png/laserRed.png')
        self.rect = self.image.get_rect()
        #self.color = self.settings.bullet_color
        #self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = alien_game.rect.midtop
        self.y = float(self.rect.y) #子弹位置浮点数表示

    def update(self):
        '''实现向下移动子弹'''
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''绘制子弹'''
        self.screen.blit(self.image, self.rect)


        

    
        

