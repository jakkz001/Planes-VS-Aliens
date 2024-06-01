import pygame

class Music:
    '''存储音效'''
    def __init__(self):
        self.player_shoot_music = pygame.mixer.Sound("Bonus/sfx_laser1.ogg") #
        self.player_shoot_music.set_volume(0.3)
        self.alien_shoot_music = pygame.mixer.Sound("Bonus/sfx_laser2.ogg")
        self.alien_shoot_music.set_volume(0.3)
        self.player_hurt_music = pygame.mixer.Sound("Bonus/sfx_shieldDown.ogg")
        self.player_hurt_music.set_volume(0.3)
        self.player_up_music = pygame.mixer.Sound("Bonus/sfx_shieldUp.ogg")
        self.player_up_music.set_volume(0.5)
        self.player_lose_music = pygame.mixer.Sound("Bonus/sfx_lose.ogg")
        self.player_lose_music.set_volume(0.5)
        self.waves_update_music = pygame.mixer.Sound("Bonus/sfx_twoTone.ogg")
        self.waves_update_music.set_volume(0.5)