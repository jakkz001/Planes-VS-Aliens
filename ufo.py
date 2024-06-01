import pygame
import random
from pygame.sprite import Sprite

class Ufo(Sprite):
    def __init__(self, ai_game):
        super(Ufo,self).__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.ufo_color_generate()
        #self.image = pygame.image.load('png/ufoBlue.png')
        self.rect = self.image.get_rect()
        self.current_blood = self.settings.ufo_blood
        self.rect.x = 0
        self.rect.y = random.uniform(0,600)
        
        
        self.x = float(self.rect.x)
    
    def ufo_color_generate(self):
        '''颜色随机生成'''
        color_random = random.randint(1,3)
        if color_random == 1:
            self.image = pygame.image.load('png/ufoBlue.png')
        elif color_random == 2:
            self.image = pygame.image.load('png/ufoGreen.png')
        elif color_random == 3:
            self.image = pygame.image.load('png/ufoRed.png')


    def update(self):
        '''向右移动ufo'''
        if self.rect.left<self.screen_rect.right:
            self.x += self.settings.ufo_speed
            self.rect.x = self.x
        

    def blitme(self):
        '''绘制ufo'''
        self.screen.blit(self.image, self.rect)

class UfoDrop(Sprite):
    def __init__(self, ai_game,ufo_game):
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.type =random.randint(1,3)

        self.ufo_drop_generate()
        self.rect = self.image.get_rect()

        self.rect.midtop = ufo_game.rect.midtop
        self.y = float(self.rect.y)

    
    def update(self):
        '''实现向下移动buff'''
        self.y += self.settings.ufo_drop_speed

        self.rect.y = self.y

    def ufo_drop_generate(self):
        '''根据掉落物的随即类型生成图像'''
        #color_random = random.randint(1,3)
        if self.type == 1:
            self.image = pygame.image.load('png/Power-ups/powerupRed_bolt.png')
        elif self.type == 2:
            self.image = pygame.image.load('png/Power-ups/powerupRed_shield.png')
        elif self.type == 3:
            self.image = pygame.image.load('png/Power-ups/powerupRed_star.png')


    