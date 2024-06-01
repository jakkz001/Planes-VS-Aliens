class Settings:
    '''存储游戏中所有设置的类'''
    def __init__(self):
        #self.screen_width = 0
        #self.screen_height = 0  屏幕宽和高在主程序文件中，自动读取为全屏的宽和高
        self.bg_color = (94, 63, 107)

        #飞船设置
        self.ship_speed = 10.0
        self.ship_shoot_speed = 700

        self.ufo_speed = 5.0
        self.ufo_drop_speed = 5.0

        #子弹设置

        self.bullet_speed = 10.0 #子弹飞行速度
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #外星飞船设置
        self.alien_speed = 1.0 #飞船飞行速度/
        self.alien_two_speed = 2.0
        self.alien_three_speed = 1.0
        self.meteorolite_speed = 2.0
        self.alien_creat_speed = 5000 #/
        self.alien_two_creat_speed = 5000
        self.alien_three_creat_speed = 5000
        self.meteorolite_creat_speed = 10000
        self.alien_two_shoot_speed = 2000
        self.alien_three_shoot_speed = 2000
        self.alien_bullet_speed = 5.0
        self.alien_creat_stepupdate = 24000
        self.ufo_creat_speed = 120000
        self.step = 1

         #血量设置
        self.ufo_blood = 20
        self.alien_blood = 10
        self.alien_two_blood = 10
        self.alien_three_blood = 20
        self.meteorolite_blood = 50
        self.bullet_harm = 10
        #self.ship_life_count = 3
        self.initial_life = 3
        self.initial_point =0

        self.alien_bonus = 30
        self.alien_two_bonus = 50
        self.alien_three_bonus = 100
        self.meteorolite_bonus = 500