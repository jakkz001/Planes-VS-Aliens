import sys

import random

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien,AlienTwo,AlienThree,AlienMeteorolite,AlienBullet
from music import Music
from ufo import Ufo,UfoDrop
from score import Score

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init() #初始化
        self.game_start = False
        self.clock = pygame.time.Clock() #时钟，帧率
        self.settings = Settings() #创建settings类实例
        self.music = Music() #创建音乐类实例
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #窗口
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.score =Score(self)
        self.PLAYER_SHOOT = pygame.USEREVENT + 0
        self.ALIEN_ONE_CREAT = pygame.USEREVENT + 1
        self.ALIEN_TWO_CREAT = pygame.USEREVENT + 2
        self.ALIEN_THREE_CREAT = pygame.USEREVENT + 3
        self.METEOROLITE_CREAT = pygame.USEREVENT + 4
        self.ALIENTWO_SHOOT = pygame.USEREVENT + 5
        self.ALIENTHREE_SHOOT = pygame.USEREVENT + 6
        self.ALIEN_CREAT_STEPUPDATE = pygame.USEREVENT + 7
        self.UFO_CREAT = pygame.USEREVENT + 8
        pygame.time.set_timer(self.PLAYER_SHOOT, self.settings.ship_shoot_speed)
        pygame.time.set_timer(self.ALIEN_ONE_CREAT, self.settings.alien_creat_speed)
        pygame.time.set_timer(self.ALIEN_TWO_CREAT, 0)  #self.settings.alien_two_creat_speed
        pygame.time.set_timer(self.ALIEN_THREE_CREAT, 0)  #self.settings.alien_three_creat_speed
        pygame.time.set_timer(self.METEOROLITE_CREAT, 0)  #self.settings.meteorolite_creat_speed
        pygame.time.set_timer(self.UFO_CREAT, self.settings.ufo_creat_speed)
        pygame.time.set_timer(self.ALIENTWO_SHOOT,self.settings.alien_two_shoot_speed)
        pygame.time.set_timer(self.ALIENTHREE_SHOOT,self.settings.alien_three_shoot_speed)
        pygame.time.set_timer(self.ALIEN_CREAT_STEPUPDATE, self.settings.alien_creat_stepupdate)
        self.bullets = pygame.sprite.Group()
        self.ufos = pygame.sprite.Group()
        self.buffs =pygame.sprite.Group()
        self.bullets_alien_two = pygame.sprite.Group()
        self.bullets_alien_three = pygame.sprite.Group()
        self.bullets_three_alien = pygame.sprite.Group()
        #self.aliens_all = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.aliens_two = pygame.sprite.Group()
        self.aliens_three = pygame.sprite.Group()
        self.meteorolites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def drew_startmenu(self):
        '''绘制开始界面'''
        self.screen.fill(self.settings.bg_color)
        titlefont = pygame.font.Font('freesansbold.ttf',80)
        tipfont = pygame.font.Font('freesansbold.ttf',30)
        title = titlefont.render(f"Planes VS Aliens",True,(255,0,0))
        tip = tipfont.render(f"press the 'space' to start the game",True,(255,0,0))
        recttitle = title.get_rect()
        recttip = tip.get_rect()
        screen_rect = self.screen.get_rect()
        recttitle.center = screen_rect.center
        recttip.centerx = screen_rect.centerx
        recttip.centery = screen_rect.centery-100
        self.screen.blit(title,recttitle)
        self.screen.blit(tip,recttip)
        pygame.display.flip()

    def drew_endmenu(self):
        '''绘制结束界面'''
        self.screen.fill(self.settings.bg_color)
        titlefont = pygame.font.Font('freesansbold.ttf',80)
        tipfont = pygame.font.Font('freesansbold.ttf',30)
        title = titlefont.render(f"GAME OVER",True,(255,0,0))
        tip = tipfont.render(f"press the 'space' to restart the game",True,(255,0,0))
        scoretip = tipfont.render(f"your final score:{self.score.point}",True,(255,0,0))
        recttitle = title.get_rect()
        recttip = tip.get_rect()
        rectscore = scoretip.get_rect()
        screen_rect = self.screen.get_rect()
        recttitle.center = screen_rect.center
        recttip.centerx = screen_rect.centerx
        recttip.centery = screen_rect.centery-100
        rectscore.centerx = screen_rect.centerx
        rectscore.centery = screen_rect.centery-200
        self.screen.blit(title,recttitle)
        self.screen.blit(tip,recttip)
        self.screen.blit(scoretip,rectscore)
        pygame.display.flip()

    def update_step(self):
        '''每24s更新难度波数'''
        self.update_alien_one_step()
        self.update_alien_two_step()
        self.update_alien_three_step()
        self.update_meteorolite_step()
        self.settings.step += 1
        self.music.waves_update_music.play()

    def update_alien_one_step(self):
        '''更新一号外星飞船难度梯度'''
        if self.settings.step <= 5:
            self.settings.alien_creat_speed -= 400
        elif 5 < self.settings.step <= 10:
            self.settings.alien_creat_speed -= 200
            self.settings.alien_blood += 2
        elif 25 < self.settings.step <= 30:
            self.settings.alien_blood += 2
            self.settings.alien_speed -= 0.1
        elif 30 < self.settings.step <= 35:
            self.settings.alien_creat_speed -=200
        pygame.time.set_timer(self.ALIEN_ONE_CREAT, self.settings.alien_creat_speed)

    def update_alien_two_step(self):
        '''更新二号外星飞船难度梯度'''
        if 10 < self.settings.step <= 15:
            pygame.time.set_timer(self.ALIEN_TWO_CREAT, self.settings.alien_two_creat_speed)
        elif 15 < self.settings.step <= 20:
            self.settings.alien_two_creat_speed -= 200
            pygame.time.set_timer(self.ALIEN_TWO_CREAT, self.settings.alien_two_creat_speed)
        elif 20 < self.settings.step <= 25:
            self.settings.alien_two_creat_speed -= 200
            self.settings.alien_two_speed -= 0.1
            pygame.time.set_timer(self.ALIEN_TWO_CREAT, self.settings.alien_two_creat_speed)
        elif 25 < self.settings.step <= 30:
            self.settings.alien_two_creat_speed -= 200
            self.settings.alien_two_blood += 2
            self.settings.alien_two_shoot_speed -= 100
            pygame.time.set_timer(self.ALIEN_TWO_CREAT, self.settings.alien_two_creat_speed)
        elif 40 < self.settings.step <= 45:
            self.settings.alien_two_shoot_speed -= 100
            pygame.time.set_timer(self.ALIEN_TWO_CREAT, self.settings.alien_two_creat_speed)
        elif self.settings.step >45:
            pygame.time.set_timer(self.ALIEN_TWO_CREAT, self.settings.alien_two_creat_speed)

    def update_alien_three_step(self):
        '''更新三号外星飞船难度梯度'''
        if 25 < self.settings.step <= 30:
            pygame.time.set_timer(self.ALIEN_THREE_CREAT, self.settings.alien_three_creat_speed)
        elif 35 < self.settings.step <= 40:
            self.settings.alien_three_creat_speed -= 200
            pygame.time.set_timer(self.ALIEN_THREE_CREAT, self.settings.alien_three_creat_speed)
        elif 40 < self.settings.step <= 45:
            self.settings.alien_three_blood += 2
            self.settings.alien_three_speed -= 0.1
            pygame.time.set_timer(self.ALIEN_THREE_CREAT, self.settings.alien_three_creat_speed)
        elif self.settings.step >45:
            pygame.time.set_timer(self.ALIEN_THREE_CREAT, self.settings.alien_three_creat_speed)

    def update_meteorolite_step(self):
        '''更新陨石难度梯度'''
        if 25 < self.settings.step <= 30:
            pygame.time.set_timer(self.METEOROLITE_CREAT, self.settings.meteorolite_creat_speed)
        elif 35 < self.settings.step <= 40:
            self.settings.meteorolite_creat_speed -= 400
            pygame.time.set_timer(self.METEOROLITE_CREAT, self.settings.meteorolite_creat_speed)
        elif 40 < self.settings.step <= 45:
            self.settings.meteorolite_creat_speed -= 400
            self.settings.meteorolite_blood += 10
            self.settings.meteorolite_speed += 0.2
            pygame.time.set_timer(self.METEOROLITE_CREAT, self.settings.meteorolite_creat_speed)
        elif self.settings.step > 45:
            pygame.time.set_timer(self.METEOROLITE_CREAT, self.settings.meteorolite_creat_speed)

    def drew_step(self):
        '''显示波数'''
        fontobj = pygame.font.Font('freesansbold.ttf',32)
        surfacefont = fontobj.render(f"WAVES:{self.settings.step}",True,(255,0,0))
        rectfont = surfacefont.get_rect()
        screen_rect = self.screen.get_rect()
        rectfont.bottomright = screen_rect.bottomright
        self.screen.blit(surfacefont,rectfont)

    def _check_start_events(self):
        '''检测开始界面事件'''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_start = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def _check_end_events(self):
        '''检测结束界面事件'''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_start = False
                    self.ship.current_life = self.settings.initial_life
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def init_game(self):
        '''初始化游戏数据'''
        self.settings.step = 1
        pygame.time.set_timer(self.ALIEN_TWO_CREAT, 0)  #self.settings.alien_two_creat_speed
        pygame.time.set_timer(self.ALIEN_THREE_CREAT, 0)  #self.settings.alien_three_creat_speed
        pygame.time.set_timer(self.METEOROLITE_CREAT, 0)  #self.settings.meteorolite_creat_speed
        self.settings.alien_speed = 1.0 #飞船飞行速度
        self.settings.alien_two_speed = 2.0
        self.settings.alien_three_speed = 1.0
        self.settings.meteorolite_speed = 2.0
        self.settings.alien_creat_speed = 5000
        self.settings.alien_two_creat_speed = 5000
        self.settings.alien_three_creat_speed = 5000
        self.settings.meteorolite_creat_speed = 10000
        self.settings.alien_two_shoot_speed = 2000
        self.settings.alien_three_shoot_speed = 2000
        self.settings.alien_bullet_speed = 5.0
        self.settings.alien_creat_stepupdate = 24000
        self.settings.ufo_blood = 20
        self.settings.alien_blood = 10
        self.settings.alien_two_blood = 10
        self.settings.alien_three_blood = 20
        self.settings.meteorolite_blood = 50
        self.settings.bullet_harm = 10
        self.settings.ship_speed = 10.0
        self.settings.ship_shoot_speed = 700
        self.score.point = 0
        self.bullets.empty()
        self.ufos.empty()
        self.bullets_alien_two.empty()
        self.bullets_alien_three.empty()
        self.bullets_three_alien.empty()
        self.aliens.empty()
        self.aliens_two.empty()
        self.aliens_three.empty()
        self.meteorolites.empty()
        self.all_sprites.empty()

    def _check_keydown_events(self, event): #检测键盘按下按键的方法
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE: 
            pygame.quit()
            sys.exit()
            

    def _check_keyup_events(self, event): #检测键盘弹起按键的方法
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self): #侦听事件，如果是退出事件就退出
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == self.PLAYER_SHOOT:
                    self._fire_bullet()
                    self.music.player_shoot_music.play()
                elif event.type == self.ALIEN_ONE_CREAT:
                    self._create_fleet_one()
                elif event.type == self.ALIEN_TWO_CREAT:
                    self._create_fleet_two()
                elif event.type == self.ALIEN_THREE_CREAT:
                    self._create_fleet_three()
                elif event.type == self.METEOROLITE_CREAT:
                    self._create_meteorolite()
                elif event.type == self.ALIENTWO_SHOOT:
                    self._fire_bullet_alien_two()
                elif event.type == self.ALIENTHREE_SHOOT:
                    self._fire_bullet_alien_three()
                elif event.type == self.ALIEN_CREAT_STEPUPDATE:
                    self.update_step()
                elif event.type == self.UFO_CREAT:
                    self.add_ufo()

    def _fire_bullet(self):
        '''创建一颗子弹并添加至编组'''
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _fire_bullet_alien_two(self):
        '''创建一颗二号外星飞船子弹并添加至编组'''
        for alien in self.aliens_two:
            new_bullet_alien = AlienBullet(self,alien)
            self.bullets_alien_two.add(new_bullet_alien)

    def _fire_bullet_alien_three(self):
        '''创建一颗三号外星飞船子弹并添加至编组'''
        for alien in self.aliens_three:
            new_bullet_alien = AlienBullet(self,alien)
            self.bullets_alien_two.add(new_bullet_alien)

    def add_ufo(self):
        '''创建一个ufo'''
        new_ufo = Ufo(self)
        self.ufos.add(new_ufo)

    def _create_fleet_one(self):
        '''生成一号外星飞船'''
        current_x = random.randint(0,self.screen_width-250)
        alien = Alien(self)
        alien.x += current_x
        alien.rect.x += current_x
        #self.aliens_all.add(alien)
        self.aliens.add(alien)

    def _create_fleet_two(self):
        '''生成二号外星飞船'''
        current_x = random.randint(0,self.screen_width-250)
        alien = AlienTwo(self)
        alien.x += current_x
        alien.rect.x += current_x
        #self.aliens_all.add(alien)
        self.aliens_two.add(alien)

    def _create_fleet_three(self):
        '''生成三号外星飞船'''
        current_x = random.randint(0,self.screen_width-250)
        alien = AlienThree(self)
        alien.x += current_x
        alien.rect.x += current_x
        #self.aliens_all.add(alien)
        self.aliens_three.add(alien)

    def _create_meteorolite(self):
        '''生成陨石'''
        current_x = random.randint(0,self.screen_width-250)
        alien = AlienMeteorolite(self)
        alien.x += current_x
        alien.rect.x += current_x
        #self.aliens_all.add(alien)
        self.meteorolites.add(alien)

    def _update_screen(self):
        '''更新屏幕'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for bullet_alien in self.bullets_alien_two.sprites():
            bullet_alien.draw_bullet()

        for bullet_alien in self.bullets_alien_three.sprites():
            bullet_alien.draw_bullet()

        for ufo in self.ufos.sprites():
            ufo.blitme()

        self.ship.blitme()
        self.buffs.draw(self.screen)
        self.aliens.draw(self.screen)
        self.aliens_two.draw(self.screen)
        self.aliens_three.draw(self.screen)
        self.meteorolites.draw(self.screen)
        self.drew_step()
        self.score.update()
        pygame.display.flip() #让最近绘制的屏幕可见
        
    def _update_bullets(self):
        '''更新子弹位置并删除屏幕外的子弹'''
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_alien_bullets(self):
        '''删除屏幕外的外星子弹'''
        for bullet_alien in self.bullets_alien_two.copy():
            if bullet_alien.rect.top >= self.screen_height:
                self.bullets_alien_two.remove(bullet_alien)
        for bullet_alien in self.bullets_alien_three.copy():
            if bullet_alien.rect.top >= self.screen_height:
                self.bullets_alien_three.remove(bullet_alien)

    def _update_aliens(self):
        '''更新外星飞船位置并删除屏幕外的飞船'''
        self.aliens.update()
        for alien in self.aliens.copy():
            if alien.rect.top >= 1440:
                self.aliens.remove(alien)
        self.aliens_two.update()
        for alien in self.aliens_two.copy():
            if alien.rect.top >= 1440:
                self.aliens_two.remove(alien)
        self.aliens_three.update()
        for alien in self.aliens_three.copy():
            if alien.rect.top >= 1440:
                self.aliens_three.remove(alien)
        self.meteorolites.update()
        for alien in self.meteorolites.copy():
            if alien.rect.top >= 1440:
                self.meteorolites.remove(alien)

        self.buffs.update()

    def collision_detection(self):
        '''ufo伤害计算'''
        for ufo in self.ufos.sprites():
            hit_bullets =  pygame.sprite.spritecollide(ufo,self.bullets,True)
            if len(hit_bullets) > 0:
                ufo.current_blood -= self.settings.bullet_harm  #不能通过bullets来访问settings
            if ufo.current_blood <= 0 :
                buff = UfoDrop(self,ufo)
                self.buffs.add(buff)
                self.ufos.remove(ufo)
        
        '''飞船血量计算'''
        hit_ship = pygame.sprite.spritecollide(self.ship,self.bullets_alien_two,True) 
        if len(hit_ship) > 0 and self.ship.current_life > 0:
            self.ship.current_life -= 1
            self.music.player_hurt_music.play()
        col_ship = pygame.sprite.spritecollide(self.ship,self.aliens,True)
        if len(col_ship) > 0 and self.ship.current_life > 0:
            self.ship.current_life -= 1
            self.music.player_hurt_music.play()
        col_ship_two = pygame.sprite.spritecollide(self.ship,self.aliens_two,True)
        if len(col_ship_two) > 0 and self.ship.current_life > 0:
            self.ship.current_life -= 1
            self.music.player_hurt_music.play()

        buff_picked = pygame.sprite.spritecollide(self.ship,self.buffs,True)
        for buff in buff_picked:
            if buff.type == 1:
                self.settings.ship_speed += 1
                self.music.player_up_music.play()
            elif buff.type ==2:
                self.ship.current_life += 1
                self.music.player_up_music.play()
            elif buff.type ==3:
                if self.settings.ship_shoot_speed >=100:
                    self.settings.ship_shoot_speed -= 50
                    pygame.time.set_timer(self.PLAYER_SHOOT, self.settings.ship_shoot_speed)
                    self.music.player_up_music.play()
        
        for alien in self.aliens.sprites():
            '''一号外星飞船血量判断'''
            hit_bullets =  pygame.sprite.spritecollide(alien,self.bullets,True)
            if len(hit_bullets) > 0:
                alien.current_blood -= self.settings.bullet_harm  #不能通过bullets来访问settings
            if alien.current_blood <= 0 :
                self.aliens.remove(alien)
                self.score.point_bonus(self.settings.alien_bonus)

        for alien in self.aliens_two.sprites():
            '''二号飞船血量判断'''
            hit_bullets =  pygame.sprite.spritecollide(alien,self.bullets,True)
            if len(hit_bullets) > 0:
                alien.current_blood -= self.settings.bullet_harm  #不能通过bullets来访问settings
            if alien.current_blood <= 0 :
                self.aliens_two.remove(alien)
                self.score.point_bonus(self.settings.alien_two_bonus)

        for alien in self.aliens_three.sprites():
            '''三号飞船血量判断'''
            hit_bullets =  pygame.sprite.spritecollide(alien,self.bullets,True)
            if len(hit_bullets) > 0:
                alien.current_blood -= self.settings.bullet_harm  #不能通过bullets来访问settings
            if alien.current_blood <= 0 :
                self.aliens_three.remove(alien)
                self.score.point_bonus(self.settings.alien_three_bonus)

        for alien in self.meteorolites.sprites():
            '''陨石血量判断'''
            hit_bullets =  pygame.sprite.spritecollide(alien,self.bullets,True)
            if len(hit_bullets) > 0:
                alien.current_blood -= self.settings.bullet_harm  #不能通过bullets来访问settings
            if alien.current_blood <= 0 :
                self.meteorolites.remove(alien)
                self.score.point_bonus(self.settings.meteorolite_bonus)
        
    def run_game(self):
        '''游戏主循环'''
        self.add_ufo()
        while True:
            if self.game_start == False:
                self.init_game()
                self.drew_startmenu()
                self._check_start_events()
            else:
                self._check_events()
                if self.ship.current_life > 0:
                    self.ship.update()
                    self._update_bullets()
                    #self.aliens_two.update()
                    self.collision_detection()
                    self.bullets_alien_two.update()
                    self.ufos.update()
                    self._update_aliens()
                    self._update_screen()
                    self.clock.tick(60)
                    self._update_alien_bullets()


                    for ufo in self.ufos.copy():
                        if ufo.rect.left >= self.screen_width: 
                            self.ufos.remove(ufo)
                            self.add_ufo()    #刷新ufo，测试用
                        if len(self.ufos) == 0:   
                            self.add_ufo()  

                else:         #游戏结束
                    self.drew_endmenu()
                    self.music.player_lose_music.play(0)
                    pygame.time.set_timer(self.ALIEN_CREAT_STEPUPDATE, 0)
                    self._check_end_events()

            

if __name__ == '__main__':
    '''创建游戏实例并运行游戏'''
    ai = AlienInvasion()
    ai.run_game()


