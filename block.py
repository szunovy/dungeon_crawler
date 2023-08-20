import pygame
from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

class AnimatedBlock(pygame.sprite.Sprite):
    def __init__(self, pos, groups, images):
        super().__init__(groups)

        self.images = images

        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.frame_index = 0
        self.animation_speed = 0.10


    def animation(self):

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images):
            self.frame_index = 0

        # set the image
        self.image = self.images[int(self.frame_index)]

    def update(self):
        self.animation()
