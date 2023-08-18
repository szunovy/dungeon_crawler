import pygame
from os import walk

def load_images(object_type, animation_types):
    frames_to_return = {}
    for animation_set in animation_types:
        frames_to_return[animation_set] = []
        path = './assets/' + object_type + '/' + animation_set
        for _, __, frames_names in walk(path):
            for frame_name in frames_names:
                # all images in assets faces right so a flip is needed
                if animation_set[-1] == "L":
                    frame = pygame.transform.flip(pygame.image.load('./assets/frames/' + frame_name).convert_alpha(), 1, 0)
                else:
                    frame = pygame.image.load('./assets/frames/' + frame_name).convert_alpha()
                frames_to_return[animation_set].append(frame)
    return frames_to_return