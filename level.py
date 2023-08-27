import pygame
from settings import *
from block import Block, AnimatedBlock
from player import Player
from random import choice
from files_handling import load_images
from enemy import Enemy
from os import path
from enemy import Enemy

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.background_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        # sprite setup
        self.create_map()
        self.game_over = False


    def create_map(self):
        self.load_map_images()
        self.load_enemies_images()

        # map_images = {
        #     'wall' : pygame.image.load('./assets/level/wall.png').convert_alpha(),
        #     'floor' : [pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_1.png').convert_alpha()),
        #                pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_2.png').convert_alpha()),
        #                pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_3.png').convert_alpha()),
        #                pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_4.png').convert_alpha()),
        #                pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_5.png').convert_alpha()),
        #                pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_6.png').convert_alpha()),
        #                pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_7.png').convert_alpha()),
        #                pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_8.png').convert_alpha()),
        #                ],
        #     'doors' : [pygame.image.load('./assets/frames/doors_leaf_closed.png').convert_alpha(),
        #                pygame.image.load('./assets/frames/doors_leaf_open.png').convert_alpha()],
        #     'wall_hole' : pygame.transform.scale2x(pygame.image.load('./assets/frames/wall_hole_1.png').convert_alpha()),
        #     'banner_blue' : pygame.transform.scale2x(
        #         pygame.image.load('./assets/frames/wall_banner_blue.png').convert_alpha()),
        #     'banner_red': pygame.transform.scale2x(
        #         pygame.image.load('./assets/frames/wall_banner_red.png').convert_alpha()),
        #     'banner_green': pygame.transform.scale2x(
        #         pygame.image.load('./assets/frames/wall_banner_green.png').convert_alpha()),
        #     'banner_yellow': pygame.transform.scale2x(
        #         pygame.image.load('./assets/frames/wall_banner_yellow.png').convert_alpha()),
        # 'lava_fountain' : [pygame.transform.scale2x(pygame.image.load('./assets/frames/wall_fountain_mid_red_anim_f0.png').convert_alpha()),
        #                 pygame.transform.scale2x(pygame.image.load('./assets/frames/wall_fountain_mid_red_anim_f1.png').convert_alpha()),
        #                 pygame.transform.scale2x(pygame.image.load('./assets/frames/wall_fountain_mid_red_anim_f2.png').convert_alpha()),
        #                 ],
        #     'skeleton': {'idle_L' : [], #todo do wywalenia
        #                    'idle_R' : [],
        #                    'run_R' : [],
        #                    'run_L' : [],
        #                    }
        # }

        for row_index, row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'w':
                    Block((x, y), (self.background_sprites, self.obstacle_sprites), self.map_images['wall'])
                if col in (' ','s', 'E', 'O','C','B','W'):  # draw floor when wall not present
                    Block((x, y), (self.background_sprites,), choice(self.map_images['floor']))  # randomize
                if col == 'h':
                    Block((x, y), (self.background_sprites, self.obstacle_sprites), self.map_images['wall_hole'])
                if col == 'r':
                    Block((x, y), (self.background_sprites, self.obstacle_sprites), self.map_images['banner_red'])
                if col == 'g':
                    Block((x, y), (self.background_sprites, self.obstacle_sprites), self.map_images['banner_green'])
                if col == 'b':
                    Block((x, y), (self.background_sprites, self.obstacle_sprites), self.map_images['banner_blue'])
                if col == 'y':
                    Block((x, y), (self.background_sprites, self.obstacle_sprites), self.map_images['banner_yellow'])
                if col == 'd':
                    Block((x, y), (self.background_sprites, self.obstacle_sprites), self.map_images['doors'])
                if col == 's':
                    self.player = Player((x, y), (self.visible_sprites,), self.obstacle_sprites, self.enemy_sprites)
                if col == 'l':
                    self.animated_block = AnimatedBlock((x, y), (self.background_sprites, self.obstacle_sprites), self.map_images['lava_fountain'])

                #potem do wruzcenia w osobnym pliku
                if col == 'E':
                    enemy_type = 'skeleton'
                    Enemy((x,y),(self.visible_sprites, self.enemy_sprites),self.obstacle_sprites, self.enemy_images[enemy_type], enemy_type)
                if col == 'O':
                    enemy_type = 'orc'
                    Enemy((x,y),(self.visible_sprites, self.enemy_sprites),self.obstacle_sprites, self.enemy_images[enemy_type], enemy_type)
                if col == 'C':
                    enemy_type = 'chort'
                    Enemy((x,y),(self.visible_sprites, self.enemy_sprites),self.obstacle_sprites, self.enemy_images[enemy_type], enemy_type)
                if col == 'B':
                    enemy_type = 'big_demon'
                    Enemy((x,y),(self.visible_sprites, self.enemy_sprites),self.obstacle_sprites, self.enemy_images[enemy_type], enemy_type)
                if col == 'W':
                    enemy_type = 'wizzard'
                    self.enemy = Enemy((x,y),(self.visible_sprites, self.enemy_sprites),self.obstacle_sprites, self.enemy_images[enemy_type], enemy_type)


    def run(self):
        # update and draw the game
        self.check_player_hit()
        self.check_game_over()


        self.player.attack()
        self.background_sprites.draw(self.display_surface)
        self.background_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.enemy_update(self.player)


        self.print_info()
        self.check_enemy_hit()
        # debug(self.player.direction)


    def print_info(self):
        heart_img = pygame.image.load('./assets/level/UI/heart_bar_fixed.png')
        heart_img = pygame.transform.scale_by(heart_img, (0.5, 0.5))

        #health bar
        #pygame.draw.rect(screen, (255,0,0), pygame.Rect(32, 8, health * 3, 16))
        #pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(32, 8, 300, 16), 3)
        #my_font = pygame.font.SysFont('Comic Sans MS', 8)
        #text_surface = my_font.render(str(health) + '%', False, (255, 255, 255))
        #screen.blit(text_surface, ((300 + 32)/2, 10))
        # self.font = pygame.font.Font(font_path, text_size)
        my_font = pygame.font.Font(font_path, 35)
        text_surface = my_font.render('HEALTH:', False, (255, 255, 255))
        self.display_surface.blit(text_surface, (32, 4))

        from_area = pygame.Rect(0, 0, round(82 * self.player.hp/100), 32)
        self.display_surface.blit(heart_img, (125, 8), from_area)

        text_surface = my_font.render('WEAPON:' + self.player.weapon, False, (255, 255, 255))
        self.display_surface.blit(text_surface, (250, 4))

        text_surface = my_font.render('EXP:' + str(self.player.exp), False, (255, 255, 255))
        self.display_surface.blit(text_surface, (450, 4))

    def enemy_update(self, player):
        # enemy_sprites = [sprite for sprite in self.visible_sprites if
        #                  hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in self.enemy_sprites:
            enemy.enemy_update(player)

    def check_player_hit(self):
        if not self.player.invulnerable:
            for sprite in self.enemy_sprites:
                if sprite.rect.colliderect(self.player.rect):
                    self.player.get_damage(sprite)

    def check_enemy_hit(self):
        if self.player.attacking:
            for sprite in self.enemy_sprites:
                if sprite.rect.colliderect(self.player.sword):
                    if sprite.can_be_attacked:
                        sprite.get_damage(10, self.player, self.player.direction)

    def check_game_over(self):
        if self.player.hp <= 0:
            self.game_over = True
            print('Game Over')

    def load_enemies_images(self):
        self.enemy_images = {}
        subdir = 'enemies'
        for enemy_type in enemies_stats.keys():
            self.enemy_images[enemy_type] = load_images(path.join(subdir, enemy_type), 0)
        # self.enemy_images['skeleton'] = load_images(path.join(subdir,'skeleton'), 0)
        # self.enemy_images['orc'] = load_images(path.join(subdir,'skeleton'), 0)
        # self.enemy_images['chort'] = load_images(path.join(subdir,'chort'), 0)
        # self.enemy_images['big_demon'] = load_images(path.join(subdir,'big_demon'), 0)
        # self.enemy_images['wizzard'] = load_images('enemies/wizzard', 0)

    def load_map_images(self):
        self.map_images = {}
        self.map_images = load_images('level')