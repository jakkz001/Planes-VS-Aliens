import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('png/laserGreen.png')
        self.rect = self.image.get_rect()
        #self.color = self.settings.bullet_color
        #self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y) #子弹位置浮点数表示
        
    def update(self):
        '''实现向上移动子弹'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''绘制子弹'''
        self.screen.blit(self.image, self.rect)