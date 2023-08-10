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
        }



        for row_index, row in enumerate(MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'w':
                    Block((x, y), [self.background_sprites, self.obstacle_sprites], map_images['wall'])
                if col in (' ','s'):  # draw floor when wall not present
                    Block((x, y), [self.background_sprites], choice(map_images['floor']))  # randomize floor
                if col == 's':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # update and draw the game
        self.background_sprites.draw(self.display_surface)
        self.background_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        # debug(self.player.direction)