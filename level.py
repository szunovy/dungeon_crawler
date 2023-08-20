import pygame
from settings import *
from block import Block, AnimatedBlock
from player import Player
from random import choice
from files_handling import load_images
from enemy import Enemy

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.background_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self): #TODO ZMIENIC NA WCZYTYWANIE Z AUTOMATU
        map_images = {
            'wall' : pygame.image.load('./assets/level/wall.png').convert_alpha(),
            'floor' : [pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_1.png').convert_alpha()),
                       pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_2.png').convert_alpha()),
                       pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_3.png').convert_alpha()),
                       pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_4.png').convert_alpha()),
                       pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_5.png').convert_alpha()),
                       pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_6.png').convert_alpha()),
                       pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_7.png').convert_alpha()),
                       pygame.transform.scale2x(pygame.image.load('./assets/frames/floor_8.png').convert_alpha()),
                       ],
            'doors' : [pygame.image.load('./assets/frames/doors_leaf_closed.png').convert_alpha(),
                       pygame.image.load('./assets/frames/doors_leaf_open.png').convert_alpha()],
            'wall_hole' : pygame.transform.scale2x(pygame.image.load('./assets/frames/wall_hole_1.png').convert_alpha()),
            'banner_blue' : pygame.transform.scale2x(
                pygame.image.load('./assets/frames/wall_banner_blue.png').convert_alpha()),
            'banner_red': pygame.transform.scale2x(
                pygame.image.load('./assets/frames/wall_banner_red.png').convert_alpha()),
            'banner_green': pygame.transform.scale2x(
                pygame.image.load('./assets/frames/wall_banner_green.png').convert_alpha()),
            'banner_yellow': pygame.transform.scale2x(
                pygame.image.load('./assets/frames/wall_banner_yellow.png').convert_alpha()),
        'lava_fountain' : [pygame.transform.scale2x(pygame.image.load('./assets/frames/wall_fountain_mid_red_anim_f0.png').convert_alpha()),
                        pygame.transform.scale2x(pygame.image.load('./assets/frames/wall_fountain_mid_red_anim_f1.png').convert_alpha()),
                        pygame.transform.scale2x(pygame.image.load('./assets/frames/wall_fountain_mid_red_anim_f2.png').convert_alpha()),
                        ],
            'skeleton': {'idle_L' : [], #todo do wywalenia
                           'idle_R' : [],
                           'run_R' : [],
                           'run_L' : [],
                           }
        }

        map_images['skeleton'] = load_images('enemies/skeleton') #todo do wywalenia

        for row_index, row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'w':
                    Block((x, y), [self.background_sprites, self.obstacle_sprites], map_images['wall'])
                if col in (' ','s', 'E'):  # draw floor when wall not present
                    Block((x, y), [self.background_sprites], choice(map_images['floor']))  # randomize
                if col == 'h':
                    Block((x, y), [self.background_sprites, self.obstacle_sprites], map_images['wall_hole'])
                if col == 'r':
                    Block((x, y), [self.background_sprites, self.obstacle_sprites], map_images['banner_red'])
                if col == 'g':
                    Block((x, y), [self.background_sprites, self.obstacle_sprites], map_images['banner_green'])
                if col == 'b':
                    Block((x, y), [self.background_sprites, self.obstacle_sprites], map_images['banner_blue'])
                if col == 'y':
                    Block((x, y), [self.background_sprites, self.obstacle_sprites], map_images['banner_yellow'])
                if col == 'd':
                    Block((x, y), [self.background_sprites, self.obstacle_sprites], map_images['doors'][0])
                if col == 's':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
                if col == 'l':
                    self.animated_block = AnimatedBlock((x, y), [self.background_sprites, self.obstacle_sprites], map_images['lava_fountain'])

                #potem do wruzcenia w osobnym pliku
                if col == 'E':
                    monster_type = 'skeleton'
                    Enemy((x,y),[self.visible_sprites],self.obstacle_sprites, map_images[monster_type], monster_type)


    def run(self):
        # update and draw the game
        self.background_sprites.draw(self.display_surface)
        self.background_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.enemy_update(self.player)
        # debug(self.player.direction)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.visible_sprites if
                         hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
