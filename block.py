import pygame
from settings import *

class Block(pygame.sprite.Sprite):  # static blocks
    '''Static block sprite class.'''
    def __init__(self, pos, groups, image):
        '''Inits static block class

        args:
            pos: tuple (x,y) with position of block
            groups: tuple of groups that sprite belongs to
            image: image of the created sprite
        '''
        super().__init__(groups)
        if type(image) is list:  # dealing with different types that could be input
            self.image = image[0]
        else:
            self.image = image
        self.rect = self.image.get_rect(topleft=pos)

class AnimatedBlock(pygame.sprite.Sprite):  #animated blocks
    '''Animated block sprite class'''
    def __init__(self, pos, groups, images):
        '''Inits static block class

        Args:
            pos: tuple (x,y) with position of block
            tuple: of groups that sprite belongs to
            list: of images for sprite animation
        '''
        super().__init__(groups)

        self.images = images

        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.frame_index = 0
        self.animation_speed = 0.10


    def animation(self):  # animates the sprite

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images):
            self.frame_index = 0

        # set the image
        self.image = self.images[int(self.frame_index)]

    def update(self):
        self.animation()
