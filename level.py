import pygame
from settings import *
from block import Block
from player import Player
from random import choice

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

    def create_map(self):
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
        }



        for row_index, row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'w':
                    Block((x, y), [self.background_sprites, self.obstacle_sprites], map_images['wall'])
                if col in (' ','s'):  # draw floor when wall not present
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

    def run(self):
        # update and draw the game
        self.background_sprites.draw(self.display_surface)
        self.background_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        # debug(self.player.direction)